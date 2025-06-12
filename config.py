import os

# Получение ключей из переменных окружения
API_KEY = os.getenv("BINANCE_API_KEY", "demo_key")
API_SECRET = os.getenv("BINANCE_API_SECRET", "demo_secret")
