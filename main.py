import requests

TELEGRAM_TOKEN = ""
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

    try:
        client = Client(api_key='', api_secret='', testnet=True)
        client.API_URL = 'https://testnet.binance.vision/api'  # Добавь это, если testnet не работает
        send_telegram_message("✅ Подключение к Binance Testnet успешно.")
    except Exception as e:
        send_telegram_message(f"❌ Ошибка подключения к Binance: {e}")
        return

    while True:
        try:
            # Пример запроса к балансу или рынку
            prices = client.get_symbol_ticker(symbol="BTCUSDT")
            message = f"💹 Цена BTCUSDT: {prices['price']}"
            print(message)
            send_telegram_message(message)
        except Exception as e:
            send_telegram_message(f"⚠️ Ошибка при получении цены: {e}")

        time.sleep(6000)  # каждые 60 сек

# --- Запуск бота и сервера параллельно ---
if __name__ == '__main__':
    Thread(target=run_server).start()
    run_bot()
