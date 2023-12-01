import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from webscraper import data

stocks = pd.read_csv('sp500_index.csv')

#Set values for columns
x = np.array(stocks[['Date']]).reshape(-1, 1)
y = np.array(stocks[['S&P500']]).reshape(-1, 1)
change = np.array(stocks[['Change']]).reshape(-1, 1) * 10

#Import sklearn and create variable for linear regression
from sklearn.linear_model import LinearRegression
reg = LinearRegression()

#Plotting
plt.plot(stocks['S&P500'], stocks['Change'])
plt.show()

plt.plot(stocks['Date'], stocks['S&P500'])
plt.show()

#Fitting
reg.fit(y,change)
weight = float(data.text.replace(',',''))
print(reg.predict([[weight]]))