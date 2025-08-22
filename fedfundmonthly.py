#Ostad Ahmad Mesbah
#MohammadAli Lotfi Kooshali
#Fridays 14:30 to 19:30

import pandas as pd
import yfinance as yf

GOLDdata = yf.download('GC=F', start='2001-01-01',end='2024-03-15')

GOLDdata.to_csv('GOLDdata.csv')

gold = pd.read_csv('GOLDdata.csv', index_col=0)
FFR = pd.read_csv('FEDFUNDS.csv', index_col=0)
combine = pd.concat([gold , FFR], axis=1)
combine.to_csv('GOLD-FFR.csv')

covariance = pd.read_csv('GOLD-FFR.csv', index_col=0)
Correlation = covariance.cov()
close = covariance['Close']
DFF = covariance['FEDFUNDS']
print(close.cov(DFF))

correlation = close.corr(DFF)
print(correlation)
