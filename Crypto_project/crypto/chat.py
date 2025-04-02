
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
import sqlite3
from pycoingecko import CoinGeckoAPI

TOKEN = '*************'
conn = sqlite3.connect('crypto_signal.db', check_same_thread=False)
cursor = conn.cursor()


cg = CoinGeckoAPI()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tracked_coins (
                    user_id INTEGER,
                    crypto_id TEXT,
                    crypto_name TEXT,
                    last_price REAL,
                    PRIMARY KEY(user_id, crypto_id),
                    FOREIGN KEY(user_id) REFERENCES users(user_id))''')
conn.commit()

def get_top_100_cryptos():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {'vs_currency': 'usd', 'order': 'market_cap_desc', 'per_page': 100, 'page': 1}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return []

    data = response.json()

    if isinstance(data, list):
        return [(coin['id'], coin['name']) for coin in data]
    else:
        print("Error: Received unexpected data format")
        return []


def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id 
    username = update.message.from_user.username  
    cursor.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
    conn.commit()

    update.message.reply_text("Welcome! Use /track to track cryptocurrencies or /untrack to remove.")

def track(update: Update, context: CallbackContext):
    cryptos = get_top_100_cryptos()
    keyboard = [[InlineKeyboardButton(name, callback_data=f"track:{coin_id}")] for coin_id, name in cryptos]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Select a cryptocurrency to track:', reply_markup=reply_markup)

def untrack(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    cursor.execute("SELECT crypto_id, crypto_name FROM tracked_coins WHERE user_id=?", (user_id,))
    tracked = cursor.fetchall()

    if not tracked:
        update.message.reply_text("You are not tracking any cryptocurrencies.")
        return

    keyboard = [[InlineKeyboardButton(name, callback_data=f"untrack:{crypto_id}")] for crypto_id, name in tracked]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Select a cryptocurrency to remove:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id  
    action, coin_id = query.data.split(":") 

    if action == "track":
        cryptos = get_top_100_cryptos()
        crypto_name = next((name for id, name in cryptos if id == coin_id), None)
        
        coin_data = cg.get_price(ids=coin_id, vs_currencies='usd')
        last_price = coin_data[coin_id]['usd']

        cursor.execute("INSERT OR REPLACE INTO tracked_coins (user_id, crypto_id, crypto_name, last_price) VALUES (?, ?, ?, ?)",
                       (user_id, coin_id, crypto_name, last_price))
        conn.commit()
        query.edit_message_text(text=f'You are now tracking {crypto_name}.')

    elif action == "untrack":
        cursor.execute("DELETE FROM tracked_coins WHERE user_id=? AND crypto_id=?", (user_id, coin_id))
        conn.commit()
        query.edit_message_text(text="Cryptocurrency removed from tracking.")

    query.answer()

def check_price_changes(context: CallbackContext):
    cursor.execute("SELECT user_id, crypto_id, crypto_name, last_price FROM tracked_coins")
    tracked_coins = cursor.fetchall()

    for user_id, crypto_id, crypto_name, last_price in tracked_coins:
        
        # Используем pycoingecko для получения цены
        coin_data = cg.get_price(ids=crypto_id, vs_currencies='usd')
        current_price = coin_data[crypto_id]['usd']

        price_change = abs((current_price - last_price) / last_price) * 100
        if price_change > 2:
            context.bot.send_message(chat_id=user_id,
                                     text=f'{crypto_name} price changed by {price_change:.2f}%!\n'
                                          f'Old: ${last_price:.2f} → New: ${current_price:.2f}')

            cursor.execute("UPDATE tracked_coins SET last_price=? WHERE user_id=? AND crypto_id=?",
                           (current_price, user_id, crypto_id))
            conn.commit()

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('track', track))
    app.add_handler(CommandHandler('untrack', untrack))
    app.add_handler(CallbackQueryHandler(button))

    job_queue = app.job_queue
    job_queue.run_repeating(check_price_changes, interval=60, first=10)  

    app.run_polling()

if __name__ == '__main__':
    main()
