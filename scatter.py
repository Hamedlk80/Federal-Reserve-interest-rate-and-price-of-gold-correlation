#Ostad Ahmad Mesbah
#MohammadAli Lotfi Kooshali
#Fridays 14:30 to 19:30

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

GOLDandFFR = pd.read_csv('GOLD-FFR2f.csv', index_col=1)
print(GOLDandFFR)
X = GOLDandFFR["Close"].values.reshape(-1,1)

Y = GOLDandFFR["DFF"].values.reshape(-1,1)

plt.subplot(2,1,1)
plt.scatter(D,X)
plt.plot(D,X)

plt.subplot(2,1,2)
plt.scatter(D,Y)
plt.plot(D,Y)

plt.show()