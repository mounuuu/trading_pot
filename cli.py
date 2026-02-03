from bot.client import TradingClient
from bot.orders import OrderManager

def main():
    client = TradingClient()
    client.connect()

    orders = OrderManager()
    orders.place_order("BTCUSDT", 1)

if __name__ == "__main__":
    main()