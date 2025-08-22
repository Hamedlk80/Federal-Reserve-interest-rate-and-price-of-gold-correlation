#Ostad Ahmad Mesbah
#MohammadAli Lotfi Kooshali
#Fridays 14:30 to 19:30

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

GOLDandFFR = pd.read_csv('GOLD-FFR2f.csv', index_col=0)

X = GOLDandFFR["Close"].values.reshape(-1,1)

Y = GOLDandFFR["DFF"].values.reshape(-1,1)

plt.subplot(1,3,1)
plt.title("Real Data")
plt.plot(X)
plt.plot(Y)

plt.subplot(1,3,2)
plt.title("MinMax")
scaler = MinMaxScaler()
scaler.fit(X)
y1 = scaler.fit_transform((X))
plt.plot(y1, color='y')

scaler.fit(Y)
y2 = scaler.transform((Y))
plt.plot(y2, color='r')

plt.subplot(1,3,3)
plt.title("Standard")
scaler = StandardScaler()
scaler.fit(X)
y1 = scaler.fit_transform((X))
plt.plot(y1, color='g')
scaler.fit(Y)
y2 = scaler.transform((Y))
plt.plot(y2, color='b')


print('هنگامی که نرخ بهره بانکی در آمریکا افزایش می یابد، سرمایه گذاران علاقه بیشتری را به سرمایه گذاری بر روی دلار آمریکا نشان می دهند. این جذابیت دلار، سبب می شود تا تقاضا برای خرید طلا کاهش یابد. کاهش تقاضای خرید طلا نیز به نوبه خود، سبب کاهش ارزش این فلز گرانبها خواهد شد.')

plt.show()

