# Code for Day 77

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv('cost_revenue_dirty.csv')

# print(df.shape)
# print(df.isna().values.any())
# print(df.duplicated().values.any())
# print(df.info())

chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget', 'USD_Worldwide_Gross', 'USD_Domestic_Gross']

for column in columns_to_clean:

    for char in chars_to_remove:
        df[column] = df[column].astype(str).str.replace(char, '')

    df[column] = pd.to_numeric(df[column])

df['Release_Date'] = pd.to_datetime(df['Release_Date'])

###################################################################################################

# print(df.describe())
# print(df[df['USD_Production_Budget'] == 1100.00])
# print(df[df['USD_Production_Budget'] == 425000000.00])
# print(df[df['USD_Domestic_Gross'] == 0].sort_values('USD_Production_Budget', ascending=False))
# print(df[df['USD_Worldwide_Gross'] == 0].sort_values('USD_Production_Budget', ascending=False))

###################################################################################################

# print(df.loc[(df.USD_Domestic_Gross == 0) & (df.USD_Worldwide_Gross != 0)])
# print(df.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0'))

recolect_date = pd.Timestamp('2018-5-1')
not_released = df[df['Release_Date'] >= recolect_date]
df_clean = df.drop(not_released.index)

films_money_losers = df_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
# print(films_money_losers.shape[0] / df_clean.shape[0])

###################################################################################################

# plt.figure(figsize=(8, 4), dpi=200)

# ax = sns.scatterplot(
#     data=df_clean,
#     x='USD_Production_Budget',
#     y='USD_Worldwide_Gross',
#     hue='USD_Worldwide_Gross',
#     size='USD_Worldwide_Gross'
# )

# ax.set(
#     ylim=(0, 3000000000),
#     xlim=(0, 450000000),
#     ylabel='Revenue in $ billions',
#     xlabel='Budget in $100 millions',
# )

# plt.show()

# plt.figure(figsize=(8,4), dpi=200)

# with sns.axes_style('darkgrid'):
#     ax = sns.scatterplot(
#         data=df_clean,
#         x='Release_Date',
#         y='USD_Production_Budget',
#         hue='USD_Worldwide_Gross',
#         size='USD_Worldwide_Gross'
#     )

#     ax.set(
#         ylim=(0, 450000000),
#         xlim=(df_clean.Release_Date.min(), df_clean.Release_Date.max()),
#         xlabel='Year',
#         ylabel='Budget in $100 millions'
#     )

# plt.show()

datetime_indx = pd.DatetimeIndex(df_clean.Release_Date)
years = datetime_indx.year
decades = years // 10 * 10
df_clean['Decade'] = decades
# print(df_clean)

old_films = df_clean[df_clean.Decade <= 1960]
new_films = df_clean[df_clean.Decade > 1960]

# print(old_films)
# print(new_films)

###################################################################################################

# plt.figure(figsize=(8, 4), dpi=200)

# with sns.axes_style('whitegrid'):
#     sns.regplot(
#         data=old_films, 
#         x='USD_Production_Budget', 
#         y='USD_Worldwide_Gross',
#         scatter_kws = {'alpha': 0.4},
#         line_kws = {'color': 'black'}
#     )

# plt.show()

# plt.figure(figsize=(8, 4), dpi=200)

# with sns.axes_style('darkgrid'):
#     ax = sns.regplot(
#         data=new_films, 
#         x='USD_Production_Budget', 
#         y='USD_Worldwide_Gross',
#         color='#2f4b7c',
#         scatter_kws = {'alpha': 0.4},
#         line_kws = {'color': '#ff7c43'}
#     )

#     ax.set(
#         ylim=(0, 3000000000),
#         xlim=(0, 450000000),
#         ylabel='Revenue in $ billions',
#         xlabel='Budget in $100 millions'
#     ) 

# plt.show()

###################################################################################################

regression = LinearRegression()
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross'])
regression.fit(X, y)
# print(regression.intercept_, regression.coef_)
# print(regression.score(X, y))

regression_old = LinearRegression()
X = pd.DataFrame(old_films, columns=['USD_Production_Budget'])
y = pd.DataFrame(old_films, columns=['USD_Worldwide_Gross'])
regression_old.fit(X, y)
# print(regression_old.intercept_, regression_old.coef_)
# print(regression_old.score(X, y))
