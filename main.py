from config import API_KEY, API_SECRET
from binance.client import Client

def main():
    print("Fartcoin Trading Bot запускается...")
    client = Client(API_KEY, API_SECRET)
    print("Успешное подключение к Binance (тестовое)")

if __name__ == "__main__":
    main()
