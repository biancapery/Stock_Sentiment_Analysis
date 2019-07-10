# EDA for S&P 500 data from https://www.kaggle.com/camnugent/sandp500/downloads/sandp500.zip/4
import pandas as pd
import numpy as np
import seaborn as sns
import random

path = "/Users/biancapery/data/s_and_p_500_data/all_stocks_5yr.csv"
stock_data = pd.read_csv(path, sep=",")

# initial EDA
stock_data.shape
print("Columns:", list(stock_data.columns)) # Columns: date, open, high, low, close, volume, Name
stock_data.info()
stock_data["date"] = pd.to_datetime(stock_data["date"])
cols = ["open", "high", "low", "close", "volume"]
cols_data = stock_data[cols]
cols_data.min(), cols_data.max()
cols_data.describe()
# sns.lineplot(cols_data["high"][0:10])

# look at companies
companies = stock_data["Name"].unique()
companies
random_sample = stock_data.sample(n=20, random_state=321)

# create smaller random sample
random_names = list(random_sample["Name"])
random_sample["Name"].iloc[0]
random_stock_data = [stock_data[stock_data["Name"] == random_sample["Name"].iloc[i]] for i in range(20)]
random_stock_data[0:10]
# Kroger Co., Kellogg, NVIDIA Corporation,
len(companies)
