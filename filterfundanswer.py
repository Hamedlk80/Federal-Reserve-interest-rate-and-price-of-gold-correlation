#Ostad Ahmad Mesbah
#MohammadAli Lotfi Kooshali
#Fridays 14:30 to 19:30

import pandas as pd
import yfinance as yf

GOLDdata = yf.download('GC=F', start='2001-01-01',end='2024-03-15')

GOLDdata.to_csv('GOLDdata.csv')

gold = pd.read_csv('GOLDdata.csv', index_col=0)
FFR = pd.read_csv('DFF.csv')
# Step 2: Convert the date column to datetime format
FFR['DATE'] = pd.to_datetime(FFR['DATE'])

# Step 3: Filter the DataFrame based on desired days (e.g., Mondays)
filtered_df = FFR[FFR['DATE'].dt.dayofweek.isin([0,1,2,3,4])]  # Exclude Saturday (5) and Sunday (6)

# Step 4: Save the filtered DataFrame to a new CSV file if desired
filtered_df.to_csv('filtered_file.csv', index=False)

ffr = pd.read_csv('filtered_file.csv',index_col=0)

combine = pd.concat([gold , ffr], axis=1)
#combine = combine.dropna()
combine.to_csv('GOLD-FFR3f.csv')
GOld = pd.read_csv('GOLD-FFR3f.csv')
GOld_cleaned = GOld.dropna()
GOld_cleaned.to_csv('GOLD-cleaned.csv',index=False)

covariance = pd.read_csv('GOLD-cleaned.csv', index_col=0)
Correlation = covariance.cov()
close = covariance['Close']
DFF = covariance['DFF']
print(close.cov(DFF))

correlation = close.corr(DFF)
print(correlation)

print(covariance.describe())