# Code for Day 78

import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('nobel_prize_data.csv')

# print(df.shape)
# print(df.info())
# print(df['year'].min())
# print(df['year'].max())
# print(df.duplicated().values.any())
# print(df.isna().values.any())
# print(df.isna().sum())

# columns_searched = ['year','category', 'laureate_type', 'birth_date','full_name', 'organization_name']
# print(df.loc[df['birth_date'].isna()][columns_searched])

df['birth_date'] = pd.to_datetime(df['birth_date'])
fractions = df['prize_share'].str.split('/', expand=True)
df['share_pct'] = pd.to_numeric(fractions[0]) / pd.to_numeric(fractions[1])

###################################################################################################

sex = df['sex'].value_counts()
fig = px.pie(
    labels=sex.index,
    values=sex.values,
    title='Percentage of Male vs Female Winners',
    names=sex.index,
    hole=0.4
)

fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
# fig.show()

# print(df[df['sex'] == 'Female'].sort_values('year', ascending=True)[:3])
# print(df[df.duplicated(subset=['full_name'], keep=False)])

prizes_per_category = df['category'].value_counts()
bar = px.bar(
    x=prizes_per_category.index,
    y=prizes_per_category.values,
    color=prizes_per_category.values,
    color_continuous_scale='Aggrnyl',
    title='Number of Prizes Awarded per Category'
)

bar.update_layout(
    xaxis_title='Nobel Prize Category',
    yaxis_title='Number of Prizes',
    coloraxis_showscale=False
)

# bar.show()

# print(df[df['category'] == 'Economics'].sort_values('year')[:3])

prizes_per_category_men_women = df.groupby(['category', 'sex'], as_index=False).agg({'prize': pd.Series.count})
prizes_per_category_men_women.sort_values('prize', ascending=False, inplace=True)
# print(prizes_per_category_men_women)

bar_split = px.bar(
    x=prizes_per_category_men_women.category,
    y=prizes_per_category_men_women.prize,
    color=prizes_per_category_men_women.sex,
    title='Number of Prizes Awarded per Category split by Men and Women')

bar_split.update_layout(
    xaxis_title='Nobel Prize Category', 
    yaxis_title='Number of Prizes'
)

# bar_split.show()

###################################################################################################

prize_per_year = df.groupby(by='year').count()['prize']
moving_average = prize_per_year.rolling(window=5).mean()
yearly_avg_share = df.groupby(by='year').agg({'share_pct': pd.Series.mean})
share_moving_average = yearly_avg_share.rolling(window=5).mean()

# plt.figure(figsize=(9, 6), dpi=150)
# plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
# plt.yticks(fontsize=14)

# plt.xticks(
#     ticks=np.arange(1900, 2021, step=5), 
#     fontsize=14, 
#     rotation=45
# )

# ax1 = plt.gca()
# ax2 = ax1.twinx()
# ax2.invert_yaxis()
# ax1.set_xlim(1900, 2020)

# ax1.scatter(
#     x=prize_per_year.index, 
#     y=prize_per_year.values, 
#     c='dodgerblue',
#     alpha=0.7,
#     s=100
# )

# ax1.plot(
#     prize_per_year.index, 
#     moving_average.values, 
#     c='crimson', 
#     linewidth=3
# )

# ax2.plot(
#     prize_per_year.index,
#     share_moving_average.values,
#     c='grey',
#     linewidth=3
# )

# plt.show()

###################################################################################################

top_countries = df.groupby(['birth_country_current'], as_index=False).agg({'prize': pd.Series.count})
top_countries.sort_values(by='prize', inplace=True)
top20_countries = top_countries[-20:]

h_bar = px.bar(
    x=top20_countries.prize,
    y=top20_countries.birth_country_current,
    orientation='h',
    color=top20_countries.prize,
    color_continuous_scale='Viridis',
    title='Top 20 Countries by Number of Prizes'
)

h_bar.update_layout(
    xaxis_title='Number of Prizes', 
    yaxis_title='Country',
    coloraxis_showscale=False
)

# h_bar.show()

df_countries = df.groupby(['birth_country_current', 'ISO'], as_index=False).agg({'prize': pd.Series.count})
df_countries.sort_values('prize', ascending=False)

world_map = px.choropleth(
    df_countries,
    locations='ISO',
    color='prize', 
    hover_name='birth_country_current', 
    color_continuous_scale=px.colors.sequential.matter
)

world_map.update_layout(coloraxis_showscale=True)

# world_map.show()

cat_country = df.groupby(['birth_country_current', 'category'], as_index=False).agg({'prize': pd.Series.count})
cat_country.sort_values(by='prize', ascending=False, inplace=True)
merged_df = pd.merge(cat_country, top20_countries, on='birth_country_current')
merged_df.columns = ['birth_country_current', 'category', 'cat_prize', 'total_prize'] 
merged_df.sort_values(by='total_prize', inplace=True)

cat_cntry_bar = px.bar(
    x=merged_df.cat_prize,
    y=merged_df.birth_country_current,
    color=merged_df.category,
    orientation='h',
    title='Top 20 Countries by Number of Prizes and Category'
)

cat_cntry_bar.update_layout(
    xaxis_title='Number of Prizes', 
    yaxis_title='Country'
)

# cat_cntry_bar.show()

prize_by_year = df.groupby(by=['birth_country_current', 'year'], as_index=False).count()
prize_by_year = prize_by_year.sort_values('year')[['year', 'birth_country_current', 'prize']]
cumulative_prizes = prize_by_year.groupby(by=['birth_country_current', 'year']).sum().groupby(level=[0]).cumsum()
cumulative_prizes.reset_index(inplace=True) 

l_chart = px.line(
    cumulative_prizes,
    x='year', 
    y='prize',
    color='birth_country_current',
    hover_name='birth_country_current'
)

l_chart.update_layout(
    xaxis_title='Year',
    yaxis_title='Number of Prizes'
)

# l_chart.show()

###################################################################################################

top20_orgs = df.organization_name.value_counts()[:20]
top20_orgs.sort_values(ascending=True, inplace=True)

org_bar = px.bar(
    x=top20_orgs.values,
    y=top20_orgs.index,
    orientation='h',
    color=top20_orgs.values,
    color_continuous_scale=px.colors.sequential.haline,
    title='Top 20 Research Institutions by Number of Prizes'
)

org_bar.update_layout(
    xaxis_title='Number of Prizes', 
    yaxis_title='Institution',
    coloraxis_showscale=False
)

# org_bar.show()

top20_org_cities = df.organization_city.value_counts()[:20]
top20_org_cities.sort_values(ascending=True, inplace=True)

city_bar2 = px.bar(
    x=top20_org_cities.values,
    y=top20_org_cities.index,
    orientation='h',
    color=top20_org_cities.values,
    color_continuous_scale=px.colors.sequential.Plasma,
    title='Which Cities Do the Most Research?'
)

city_bar2.update_layout(
    xaxis_title='Number of Prizes', 
    yaxis_title='City',
    coloraxis_showscale=False
)

# city_bar2.show()

top20_cities = df.birth_city.value_counts()[:20]
top20_cities.sort_values(ascending=True, inplace=True)

city_bar = px.bar(
    x=top20_cities.values,
    y=top20_cities.index,
    orientation='h',
    color=top20_cities.values,
    color_continuous_scale=px.colors.sequential.Plasma,
    title='Where were the Nobel Laureates Born?'
)

city_bar.update_layout(
    xaxis_title='Number of Prizes', 
    yaxis_title='City of Birth',
    coloraxis_showscale=False
)

# city_bar.show()

country_city_org = df.groupby(
    by=['organization_country', 'organization_city', 'organization_name'], 
    as_index=False
).agg({'prize': pd.Series.count})
country_city_org = country_city_org.sort_values('prize', ascending=False)

burst = px.sunburst(
    country_city_org, 
    path=['organization_country', 'organization_city', 'organization_name'], 
    values='prize',
    title='Where do Discoveries Take Place?',
)

burst.update_layout(
    xaxis_title='Number of Prizes', 
    yaxis_title='City',
    coloraxis_showscale=False
)

# burst.show()

###################################################################################################

birth_years = df.birth_date.dt.year
df['winning_age'] = df.year - birth_years

# print(df.nlargest(n=1, columns='winning_age'))
# print(df.nsmallest(n=1, columns='winning_age'))

# plt.figure(figsize=(8, 4), dpi=200)

# sns.histplot(
#     data=df,
#     x=df.winning_age,
#     bins=30
# )

# plt.xlabel('Age')
# plt.title('Distribution of Age on Receipt of Prize')

# plt.show()

# plt.figure(figsize=(8,4), dpi=200)

# with sns.axes_style("whitegrid"):
#     sns.regplot(
#         data=df,
#         x='year',
#         y='winning_age',
#         lowess=True,
#         scatter_kws={'alpha': 0.4},
#         line_kws={'color': 'black'}
#     )

# plt.show()

# plt.figure(figsize=(8,4), dpi=200)

# with sns.axes_style("whitegrid"):
#     sns.boxplot(
#         data=df,
#         x='category',
#         y='winning_age'
#     )

# plt.show()

# with sns.axes_style('whitegrid'):
#     sns.lmplot(
#         data=df,
#         x='year', 
#         y='winning_age',
#         row = 'category',
#         lowess=True, 
#         aspect=2,
#         scatter_kws = {'alpha': 0.6},
#         line_kws = {'color': 'black'}
#     )

# plt.show()

with sns.axes_style("whitegrid"):
    sns.lmplot(
        data=df,
        x='year',
        y='winning_age',
        hue='category',
        lowess=True, 
        aspect=2,
        scatter_kws={'alpha': 0.5},
        line_kws={'linewidth': 5}
    )

plt.show()
