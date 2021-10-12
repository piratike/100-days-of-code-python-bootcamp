# Code for Day 74

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

df_tesla = pd.read_csv('data/TESLA Search Trend vs Price.csv')
df_btc_search = pd.read_csv('data/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('data/Daily Bitcoin Price.csv')
df_unemployment = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-19.csv')
df_ue_2020 = pd.read_csv('data/UE Benefits Search vs UE Rate 2004-20.csv')

###################################################################################################

df_tesla.dropna(inplace=True)
df_btc_search.dropna(inplace=True)
df_btc_price.dropna(inplace=True)
df_unemployment.dropna(inplace=True)

df_tesla['MONTH'] = pd.to_datetime(df_tesla['MONTH'])
df_btc_search['MONTH'] = pd.to_datetime(df_btc_search['MONTH'])
df_btc_price['DATE'] = pd.to_datetime(df_btc_price['DATE'])
df_unemployment['MONTH'] = pd.to_datetime(df_unemployment['MONTH'])
df_ue_2020['MONTH'] = pd.to_datetime(df_ue_2020['MONTH'])

df_btc_price_monthly = df_btc_price.resample('M', on='DATE').mean()

###################################################################################################

# years = mdates.YearLocator()
# months = mdates.MonthLocator()
# years_fmt = mdates.DateFormatter('%Y')

# plt.figure(figsize=(14, 8), dpi=120)
# plt.title('Tesla Web Search vs Price', fontsize=18)
# plt.xticks(fontsize=14, rotation=45)

# ax1 = plt.gca()
# ax2 = ax1.twinx()

# ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

# ax1.set_ylim([0, 600])
# ax1.set_xlim([df_tesla['MONTH'].min(), df_tesla['MONTH'].max()])

# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)

# ax1.plot(df_tesla['MONTH'], df_tesla['TSLA_USD_CLOSE'], color='#E6232E', linewidth=3)
# ax2.plot(df_tesla['MONTH'], df_tesla['TSLA_WEB_SEARCH'], color='skyblue', linewidth=3)

# plt.show()

###################################################################################################

# years = mdates.YearLocator()
# months = mdates.MonthLocator()
# years_fmt = mdates.DateFormatter('%Y')

# plt.figure(figsize=(14, 8), dpi=120)
# plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
# plt.xticks(fontsize=14, rotation=45)

# ax1 = plt.gca()
# ax2 = ax1.twinx()

# ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=14)
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

# ax1.set_ylim([0, 15000])
# ax1.set_xlim([df_btc_price_monthly.index.min(), df_btc_price_monthly.index.max()])

# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)

# ax1.plot(df_btc_price_monthly.index, df_btc_price_monthly['CLOSE'], color='#F08F2E', linewidth=3, linestyle='--')
# ax2.plot(df_btc_price_monthly.index, df_btc_search['BTC_NEWS_SEARCH'], color='skyblue', linewidth=3, marker='o')

# plt.show()

###################################################################################################

# roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()

# years = mdates.YearLocator()
# months = mdates.MonthLocator()
# years_fmt = mdates.DateFormatter('%Y')

# plt.figure(figsize=(14, 8), dpi=120)
# plt.title('Monthly Search of "Unemplyment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
# plt.xticks(fontsize=14, rotation=45)

# ax1 = plt.gca()
# ax2 = ax1.twinx()

# ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
# ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

# ax1.set_ylim([3, 10.5])
# ax1.set_xlim([df_unemployment['MONTH'].min(), df_unemployment['MONTH'].max()])

# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)

# ax1.grid(color='grey', linestyle='--')

# ax1.plot(df_unemployment['MONTH'], roll_df['UNRATE'], color='purple', linewidth=3, linestyle='--')
# ax2.plot(df_unemployment['MONTH'], roll_df['UE_BENEFITS_WEB_SEARCH'], color='skyblue', linewidth=3, marker='o')

# plt.show()

###################################################################################################

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

plt.figure(figsize=(14, 8), dpi=120)
plt.title('Monthly US "Unemplyment Benefits" Web Search vs UNRATE incl 2020', fontsize=18)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

ax1.set_ylim([3, 10.5])
ax1.set_xlim([df_ue_2020['MONTH'].min(), df_ue_2020['MONTH'].max()])

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.grid(color='grey', linestyle='--')

ax1.plot(df_ue_2020['MONTH'], df_ue_2020['UNRATE'], color='purple', linewidth=3, linestyle='--')
ax2.plot(df_ue_2020['MONTH'], df_ue_2020['UE_BENEFITS_WEB_SEARCH'], color='skyblue', linewidth=3, marker='o')

plt.show()
