import requests

TELEGRAM_TOKEN = "7699731028:AAFfg5DPAY4r8JrF_sW2b5VKMPihwHgxu3w"
TELEGRAM_CHAT_ID = "5071558424"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"Ошибка Telegram: {response.text}")
    except Exception as e:
        print(f"Ошибка отправки в Telegram: {e}")
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
    send_telegram_message("🚀 Fartcoin Trading Bot запущен!")
    client = Client(api_key='', api_secret='', testnet=True)
    print("Успешное подключение к Binance (тестовое)")
    while True:
        # Здесь можно вставить основную логику
        time.sleep(30)

# --- Запуск бота и сервера параллельно ---
if __name__ == '__main__':
    Thread(target=run_server).start()
    run_bot()
