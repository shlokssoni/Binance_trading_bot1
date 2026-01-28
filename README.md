# Binance Futures Trading Bot (USDT-M)

A professional Python CLI application for placing orders on the **Binance Futures Testnet**. This project demonstrates a modular backend structure, secure key management, and robust error logging.

---

## Setup Instructions

### 1. Environment Setup
Clone the project and navigate to the directory. Create a virtual environment and install dependencies:
* `python -m venv venv`
* `venv\Scripts\activate` (On Windows)
* `pip install -r requirements.txt`

### 2. API Configuration
Create a file named **`api_key.env`** in the root directory and add your credentials:
```text
BINANCE_API_KEY="your_testnet_api_key"
BINANCE_SECRET_KEY="your_testnet_secret_key"

### 3.Usage Examples
Run these commands in your terminal to interact with the Testnet:

### Place a Market Order (Instant Buy)
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

### Place a Limit Order (Price-Specific Sell)
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 120000
