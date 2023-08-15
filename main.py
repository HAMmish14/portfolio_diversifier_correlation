import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Define stock symbols and date range
stock_symbols = ["GOOGL","MSFT"]
start_date = '2018-01-01'
end_date = '2022-12-31'

# Fetch historical stock price data for multiple stocks
stock_data = yf.download(stock_symbols, start=start_date, end=end_date)

# Calculate 50-day and 200-day moving averages for each stock
#for symbol in stock_symbols:
 #   stock_data[f'{symbol}_50_MA'] = stock_data['Close', symbol].rolling(window=50).mean()
  #  stock_data[f'{symbol}_200_MA'] = stock_data['Close', symbol].rolling(window=200).mean()

# Plot stock prices and moving averages for all stocks
plt.figure(figsize=(12, 6))
for symbol in stock_symbols:
    plt.plot(stock_data.index, stock_data['Close', symbol], label=f'{symbol} Stock Price')
   #plt.plot(stock_data.index, stock_data[f'{symbol}_50_MA'], label=f'{symbol} 50-day MA')
    #plt.plot(stock_data.index, stock_data[f'{symbol}_200_MA'], label=f'{symbol} 200-day MA')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Prices and Moving Averages')
plt.legend()
plt.show()
correlation_matrix = stock_data.pct_change().corr(method="pearson")

# Plot correlation heatmap
plt.figure(figsize=(25, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Stock Price Correlation Heatmap')
plt.show()


for i in range(len(stock_symbols)):
    for j in range(i + 1, len(stock_symbols)):
        plt.figure(figsize=(8, 6))
        plt.scatter(stock_data.iloc[:, i], stock_data.iloc[:, j], alpha=0.7)
        plt.title(f'{stock_symbols[i]} vs {stock_symbols[j]}')
        plt.xlabel(stock_symbols[i] + ' Price')
        plt.ylabel(stock_symbols[j] + ' Price')
        plt.show()