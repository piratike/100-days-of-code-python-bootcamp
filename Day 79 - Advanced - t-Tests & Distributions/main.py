# Code for Day 79

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.express as px
import numpy as np
import seaborn as sns
from scipy import stats
from datetime import datetime

df_yearly = pd.read_csv('annual_deaths_by_clinic.csv')
df_monthly = pd.read_csv('monthly_deaths.csv')

df_monthly.date = pd.to_datetime(df_monthly.date)

# print(df_yearly.shape)
# print(df_yearly.info())
# print(df_yearly.duplicated().values.any(), df_yearly.isna().values.any())

# print(df_monthly.shape)
# print(df_monthly.info())
# print(df_monthly.duplicated().values.any(), df_monthly.isna().values.any())
# print(df_monthly.describe())

# print(df_yearly.deaths.sum() / df_yearly.births.sum())

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y') 

plt.figure(figsize=(8, 5), dpi=150)
plt.title('Total Number of Monthly Births and Deaths', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('Births', color='skyblue', fontsize=18)
ax2.set_ylabel('Deaths', color='crimson', fontsize=18)

ax1.set_xlim([df_monthly.date.min(), df_monthly.date.max()])
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.grid(color='grey', linestyle='--')

ax1.plot(
    df_monthly.date, 
    df_monthly.births, 
    color='skyblue', 
    linewidth=3
)

ax2.plot(
    df_monthly.date, 
    df_monthly.deaths, 
    color='crimson', 
    linewidth=2, 
    linestyle='--'
)

# plt.show()

###################################################################################################

line_births = px.line(
    df_yearly, 
    x='year', 
    y='births',
    color='clinic',
    title='Total Yearly Births by Clinic'
)

# line_births.show()

line_deaths = px.line(
    df_yearly, 
    x='year', 
    y='deaths',
    color='clinic',
    title='Total Yearly Deaths by Clinic'
)

# line_deaths.show()

df_yearly['pct_deaths'] = df_yearly.deaths / df_yearly.births

clinic_1 = df_yearly[df_yearly.clinic == 'clinic 1']
avg_clinic_1 = clinic_1.deaths.sum() / clinic_1.births.sum() * 100
clinic_2 = df_yearly[df_yearly.clinic == 'clinic 2']
avg_clinic_2 = clinic_2.deaths.sum() / clinic_2.births.sum() * 100

# print(avg_clinic_1, avg_clinic_2)

line_pct = px.line(
    df_yearly, 
    x='year', 
    y='pct_deaths',
    color='clinic',
    title='Proportion of Yearly Deaths by Clinic'
)

# line_pct.show()

###################################################################################################

df_monthly['pct_deaths'] = df_monthly.deaths / df_monthly.births
handwashing_start = datetime(1846, 6, 1)
before_handwashing = df_monthly[df_monthly.date < handwashing_start]
after_handwashing = df_monthly[df_monthly.date >= handwashing_start]

bw_rate = before_handwashing.deaths.sum() / before_handwashing.births.sum() * 100
aw_rate = after_handwashing.deaths.sum() / after_handwashing.births.sum() * 100
# print(bw_rate, aw_rate)

roll_df = before_handwashing.set_index('date')
roll_df = roll_df.rolling(window=6).mean()
# print(roll_df)

plt.figure(figsize=(14,8), dpi=200)
plt.title('Percentage of Monthly Deaths over Time', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
plt.ylabel('Percentage of Deaths', color='crimson', fontsize=18)

ax = plt.gca()
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
ax.set_xlim([df_monthly.date.min(), df_monthly.date.max()])

plt.grid(color='grey', linestyle='--')

ma_line, = plt.plot(
    roll_df.index, 
    roll_df.pct_deaths, 
    color='crimson', 
    linewidth=3, 
    linestyle='--',
    label='6m Moving Average'
)

bw_line, = plt.plot(
    before_handwashing.date, 
    before_handwashing.pct_deaths,
    color='black', 
    linewidth=1, 
    linestyle='--', 
    label='Before Handwashing'
)

aw_line, = plt.plot(
    after_handwashing.date, 
    after_handwashing.pct_deaths, 
    color='skyblue', 
    linewidth=3, 
    marker='o',
    label='After Handwashing'
)

plt.legend(handles=[ma_line, bw_line, aw_line], fontsize=18)
# plt.show()

###################################################################################################

avg_prob_before = before_handwashing.pct_deaths.mean() * 100
avg_prob_after = after_handwashing.pct_deaths.mean() * 100
mean_diff = avg_prob_before - avg_prob_after
times = avg_prob_before / avg_prob_after

# print(avg_prob_after, avg_prob_before, mean_diff, times)

df_monthly['washing_hands'] = np.where(df_monthly.date < handwashing_start, 'No', 'Yes')

box = px.box(
    df_monthly, 
    x='washing_hands', 
    y='pct_deaths',
    color='washing_hands',
    title='How Have the Stats Changed with Handwashing?'
)

box.update_layout(
    xaxis_title='Washing Hands?',
    yaxis_title='Percentage of Monthly Deaths'
)

# box.show()

hist = px.histogram(
    df_monthly, 
    x='pct_deaths', 
    color='washing_hands',
    nbins=30,
    opacity=0.6,
    barmode='overlay',
    histnorm='percent',
    marginal='box'
)

hist.update_layout(
    xaxis_title='Proportion of Monthly Deaths',
    yaxis_title='Count'
)

# hist.show()

plt.figure(dpi=200)

sns.kdeplot(
    before_handwashing.pct_deaths, 
    shade=True,
    clip=(0, 1)
)

sns.kdeplot(
    after_handwashing.pct_deaths, 
    shade=True,
    clip=(0, 1)
)

plt.title('Est. Distribution of Monthly Death Rate Before and After Handwashing')
plt.xlim(0, 0.40)
# plt.show()

t_stat, p_value = stats.ttest_ind(a=before_handwashing.pct_deaths, b=after_handwashing.pct_deaths)
print(t_stat, p_value)
