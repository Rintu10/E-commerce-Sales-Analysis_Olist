#Importing data
import pandas as pd
import numpy as np
import yfinance as yf

#download data From Yahoo Finance site
df = yf.download(
    tickers='TCS.NS',
    start='2020-01-01',
    end='2025-07-31',
    interval='1d')

df2 = yf.download(
    tickers='INFY.NS',
    start='2020-01-01',
    end='2025-07-31',
    interval='1d')

df3 = yf.download(
    tickers='RELIANCE.NS',
    start='2020-01-01',
    end='2025-07-31',
    interval='1d')

#saving the data to CSV files
df.to_csv(r"D:\DataSet\TCS_Financial_Data.csv", index=True)
df2.to_csv(r"D:\DataSet\INFY_Financial_Data.csv", index=True) 
df3.to_csv(r"D:\DataSet\RELIANCE_Financial_Data.csv", index=True)
