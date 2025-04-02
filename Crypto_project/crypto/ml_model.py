import os
import requests
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense

# MODEL_PATH = "prediction/lstm_model_{coin}.h5"

def get_historical_data(coin="bitcoin", days=365):
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
    params = {"vs_currency": "usd", "days": days, "interval": "daily"}
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if "prices" not in data:
        raise ValueError(f"Error of API the is no such key as prices: {data}")
    
    prices = data["prices"]
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)
    
    return df


def create_sequences(data, seq_length=10):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i : i + seq_length])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

         
def train_model(MODEL_PATH, coin="bitcoin"):
    # MODEL_PATH = "prediction/lstm_model_{coin}.h5"
    df = get_historical_data(coin, 365)
    scaler = MinMaxScaler()
    df["price_scaled"] = scaler.fit_transform(df[["price"]])
    
    seq_length = 10
    X, y = create_sequences(df["price_scaled"].values, seq_length)
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(seq_length, 1)),  
        LSTM(50, return_sequences=False),  
        Dense(25),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss=tf.keras.losses.MeanSquaredError())
    model.fit(X, y, epochs=20, batch_size=16, verbose=1)
    model.save(MODEL_PATH)
    return model, scaler

def predict_price(coin="bitcoin"):
    MODEL_PATH = f"prediction/lstm_model_{coin}.h5"
    if os.path.exists(MODEL_PATH):
        model = load_model(MODEL_PATH)
        df = get_historical_data(coin, 365)
        scaler = MinMaxScaler()
       
        df["price_scaled"] = scaler.fit_transform(df[["price"]])
    else:
        model, scaler = train_model(MODEL_PATH, coin)
        df = get_historical_data(coin, 365)
        df["price_scaled"] = scaler.fit_transform(df[["price"]])  

    seq_length = 10
    last_sequence = df["price_scaled"].values[-seq_length:].reshape(1, seq_length, 1)
    future_prices = []
    
    for _ in range(30):
        predicted = model.predict(last_sequence)
        future_prices.append(predicted[0][0])
        last_sequence = np.append(last_sequence[:, 1:, :], [[predicted[0]]], axis=1)
        
    future_prices = scaler.inverse_transform(np.array(future_prices).reshape(-1, 1)).flatten()
    
    return {
        "1day": future_prices[0],
        "1week": np.mean(future_prices[:7]),
        "1month": np.mean(future_prices)
    }

    