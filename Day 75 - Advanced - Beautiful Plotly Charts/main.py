# Code for Day 75

import pandas as pd
import plotly.express as px

df_apps = pd.read_csv('apps.csv')

###################################################################################################

df_apps.drop(['Last_Updated', 'Android_Ver'], axis=1, inplace=True)
df_apps.dropna(inplace=True)
df_apps.drop_duplicates(subset=['App', 'Type', 'Price'], inplace=True)

###################################################################################################

# print(df_apps.sort_values('Rating', ascending=False))
# print(df_apps.sort_values('Size_MBs', ascending=False))
# print(df_apps.sort_values('Reviews', ascending=False))

###################################################################################################

# ratings = df_apps['Content_Rating'].value_counts()

# fig = px.pie(
#     labels=ratings.index,
#     values=ratings.values,
#     title='Content Rating',
#     names=ratings.index,
#     hole=0.6
# )

# fig.update_traces(textposition='outside', textinfo='percent+label')

# fig.show()

###################################################################################################

df_apps['Installs'] = df_apps['Installs'].astype(str).str.replace(',', '')
df_apps['Installs'] = pd.to_numeric(df_apps['Installs'])

df_apps['Price'] = df_apps['Price'].astype(str).str.replace('$', '')
df_apps['Price'] = pd.to_numeric(df_apps['Price'])

# print(df_apps[['App', 'Installs']].groupby('Installs').count())

df_apps = df_apps[df_apps['Price'] < 250]
df_apps['Revenue_Estimate'] = df_apps['Installs'].mul(df_apps['Price'])

# print(df_apps)

###################################################################################################

# top_10_category = df_apps['Category'].value_counts()[:10]

# bar = px.bar(
#     x=top_10_category.index,
#     y=top_10_category.values
# )

# bar.show()

category_installs = df_apps.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)

# h_bar = px.bar(
#     x=category_installs.Installs,
#     y=category_installs.index,
#     orientation='h',
#     title='Category Popularity'
# )

# h_bar.update_layout(
#     xaxis_title='Number of Downloads',
#     yaxis_title='Category'
# )

# h_bar.show()

# cat_number = df_apps.groupby('Category').agg({'App': pd.Series.count})
# cat_merged = pd.merge(cat_number, category_installs, on='Category', how='inner')
# cat_merged.sort_values('Installs', ascending=False)

# scatter = px.scatter(
#     cat_merged,
#     x='App',
#     y='Installs',
#     title='Category Concentration',
#     size='App',
#     hover_name=cat_merged.index,
#     color='Installs'
# )

# scatter.update_layout(
#     xaxis_title="Number of Apps (Lower=More Concentrated)",
#     yaxis_title="Installs",
#     yaxis=dict(type='log')
# )

# scatter.show()

###################################################################################################

# stack = df_apps['Genres'].str.split(';', expand=True).stack()
# num_genres = stack.value_counts()

# bar = px.bar(
#     x=num_genres.index[:15],
#     y=num_genres.values[:15],
#     title='Top Genres',
#     hover_name=num_genres.index[:15],
#     color=num_genres.values[:15],
#     color_continuous_scale='Agsunset'
# )

# bar.update_layout(
#     xaxis_title='Genre',
#     yaxis_title='Number of Apps',
#     coloraxis_showscale=False
# )

# bar.show()

###################################################################################################

df_free_vs_paid = df_apps.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})

# print(df_free_vs_paid.head())

# g_bar = px.bar(
#     df_free_vs_paid,
#     x='Category',
#     y='App',
#     title='Free vs Paid Apps by Category',
#     color='Type',
#     barmode='group'
# )

# g_bar.update_layout(
#     xaxis_title='Category',
#     yaxis_title='Number of Apps',
#     xaxis={'categoryorder':'total descending'},
#     yaxis=dict(type='log')
# )

# g_bar.show()

# box = px.box(
#     df_apps,
#     y='Installs',
#     x='Type',
#     color='Type',
#     notched=True,
#     points='all',
#     title='How Many Downloads are Paid Apps Giving Up?')

# box.update_layout(yaxis=dict(type='log'))

# box.show()

df_paid_apps = df_apps[df_apps['Type'] == 'Paid']

# box = px.box(
#     df_paid_apps, 
#     x='Category', 
#     y='Revenue_Estimate',
#     title='How Much Can Paid Apps Earn?'
# )

# box.update_layout(
#     xaxis_title='Category',
#     yaxis_title='Paid App Ballpark Revenue',
#     xaxis={'categoryorder':'min ascending'},
#     yaxis=dict(type='log')
# )

# box.show()

df_paid_apps.Price.median()

box = px.box(
    df_paid_apps,
    x='Category',
    y="Price",
    title='Price per Category'
)

box.update_layout(
    xaxis_title='Category',
    yaxis_title='Paid App Price',
    xaxis={'categoryorder':'max descending'},
    yaxis=dict(type='log')
)

box.show()
