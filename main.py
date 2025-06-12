from flask import Flask
from threading import Thread
import time
from binance.client import Client

# --- Flask сервер для Render ---
app = Flask(__name__)

@app.route('/')
def home():
    return 'Fartcoin bot работает'

def run_server():
    app.run(host='0.0.0.0', port=10000)

# --- Трейдинг бот ---
def run_bot():
    print("Fartcoin Trading Bot запускается...")
    client = Client(api_key='', api_secret='', testnet=True)
    print("Успешное подключение к Binance (тестовое)")
    while True:
        # Здесь можно вставить основную логику
        time.sleep(30)

# --- Запуск бота и сервера параллельно ---
if __name__ == '__main__':
    Thread(target=run_server).start()
    run_bot()
