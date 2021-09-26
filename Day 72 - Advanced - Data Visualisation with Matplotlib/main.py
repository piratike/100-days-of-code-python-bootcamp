# Code for Day 72

from numpy.core.fromnumeric import mean
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

# DataFrame info
#print(df.head(), df.tail(), df.shape, df.count())

# Get entries per programming languague and entries per programming languague and month
#print(df.groupby('TAG').sum(), df.groupby('TAG').count())

# Convert string to Datetimes
df['DATE'] = pd.to_datetime(df['DATE'])

###################################################################################################

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
#print(reshaped_df.head(), reshaped_df.tail(), reshaped_df.shape, reshaped_df.columns, reshaped_df.count())
reshaped_df.fillna(0, inplace=True)

###################################################################################################

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column], linewidth=3, label=reshaped_df[column].name)

plt.legend(fontsize=16)
#plt.show()

###################################################################################################

roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)
plt.show()
