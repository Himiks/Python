Python crypto project 
This is a cryptocurrency tracker web application built with Django as the backend and Bootstrap + Chart.js for the frontend. The application integrates data from various cryptocurrency APIs CoinGecko and performs machine learning analysis on the data using popular Python libraries such as Scikit-Learn, Pandas, and NumPy. Users can track cryptocurrency prices and receive notifications via a Telegram bot when significant price changes occur.

Features
Cryptocurrency Tracking: Track up to 10 the most popular cryptocurrencies with real-time price updates from CoinGecko API.

Machine Learning Analysis: Perform ML-based analysis on cryptocurrency price trends using Scikit-Learn, Pandas, and NumPy.

Data Visualization: Use Chart.js integrated with JavaScript to display cryptocurrency price trends and analysis on interactive graphs.

Telegram Notifications: Receive alerts via a Telegram bot when tracked cryptocurrencies experience significant price changes.

SQLite Database: Stores user preferences, tracked cryptocurrencies, and other necessary data for the application.


Tech Stack
Backend: Django

Frontend: CSS, HTML, JavaScript, Chart.js

Machine Learning: Scikit-Learn, Pandas, NumPy

Database: SQLite

API: CoinGecko API

Notifications: Telegram bot (using python-telegram-bot library)


Installation
To run this project locally, follow these steps:

git clone https://github.com/Himiks/Crypto_project.git
cd Crypto?project

pip install -r requirements.txt


python manage.py makemigrations
python manage.py migrate



python manage.py runserver