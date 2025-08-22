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

FFR.to_csv('Golddata2.csv')

#combine = pd.concat([gold , FFR], axis=1)
#combine.to_csv('GOLD-FFR.csv')

#covariance = pd.read_csv('GOLD-FFR.csv', index_col=0)
