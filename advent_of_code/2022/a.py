import yfinance as yf

# Get stock data for a specific company
ticker = "AAPL"
stock_data = yf.Ticker(ticker)

# Print the stock's info
print(stock_data.info)

# Get the historical prices for the stock
historical_prices = stock_data.history(period="1y")
print(historical_prices)
