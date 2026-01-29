import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv("api_key.env") 

class BinanceBot:
    def __init__(self):
        api_key = os.getenv('BINANCE_API_KEY')
        api_secret = os.getenv('BINANCE_SECRET_KEY')
        
        self.client = Client(api_key, api_secret, testnet=True)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type.upper() == 'MARKET':
                return self.client.futures_create_order(
                    symbol=symbol.upper(),
                    side=side.upper(),
                    type='MARKET',
                    quantity=quantity
                )
            elif order_type.upper() == 'LIMIT':
                return self.client.futures_create_order(
                    symbol=symbol.upper(),
                    side=side.upper(),
                    type='LIMIT',
                    timeInForce='GTC',
                    quantity=quantity,
                    price=price
                )
        except Exception as e:

            return {"error": str(e)}
