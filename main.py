import argparse
import logging
from client_wrapper import BinanceBot


logging.basicConfig(
    filename='trading.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
   
    parser = argparse.ArgumentParser(description="Binance Trading Bot CLI")
    
    parser.add_argument("--symbol", required=True, help="e.g., BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

   
    bot = BinanceBot()

    print(f"\n--- Sending {args.type} {args.side} Order ---")
    
   
    response = bot.place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    if "error" in response:
        print(f"FAILED: {response['error']}")
        logging.error(f"Order Failed: {response['error']}")
    else:
      
        print(f"SUCCESS!")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        logging.info(f"Order Placed Successfully: {response}")

if __name__ == "__main__":

    main()
