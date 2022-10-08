import logging
import pandas as pd
import yfinance as yf

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

'''
In this program we will extract the data for last 90 days on which NSE was active.
i.e. The final CSV file will contain last 90 closing price for all stocks except for those
    that are delisted or temporarily suspended. These Symbols will be saved in a different
    CSV File.
'''

# Getting Stock Symbols from the CSV file.
with open("List of Stocks and their Symbols.csv", 'r') as stock_list:
    data = pd.read_csv(stock_list)
symbols = [(x[1].strip() + '.NS') for x in data.values]

'''
We download data from 1st May, 2022 and take the last 90 entries.
so we get the last 90 entries
'''
data = yf.download(symbols, '2022-05-01', progress=False)['Adj Close'][-90:]
failed_symbols = pd.DataFrame({'Failed': list(yf.shared._ERRORS.keys())})

# Saving the data to CSV file.
data.to_csv('last_90_days_record.csv')
failed_symbols.to_csv('Failed to Gater Records.csv', index=False)
