# Code for Day 73

import pandas as pd
import matplotlib.pyplot as plt

colors = pd.read_csv('data/colors.csv')
unique_colors = colors['name'].nunique()
trans_colors = colors.groupby('is_trans').count()
other_trans_colors = colors['is_trans'].value_counts()

#print(unique_colors)
#print(trans_colors)
#print(other_trans_colors)

###################################################################################################

# In which year were the first LEGO sets released and what were these sets called?

sets = pd.read_csv('data/sets.csv')
first_set_year = sets['year'].min()
id_first_set = sets['year'].idxmin()
first_set_name = sets['name'].loc[id_first_set]

#print(first_set_year, first_set_name)

# How many different products did the LEGO company sell in their first year of operation?

sets_first_year = sets[sets['year'] == first_set_year]

#print(sets_first_year)

# What are the top 5 LEGO sets with the most number of parts? 

sets_sorted = sets.sort_values('num_parts', ascending=False).head()

#print(sets_sorted)

###################################################################################################

sets_by_year = sets.groupby('year').count()

#print(sets_by_year['set_num'])

#plt.plot(sets_by_year.index[:-2], sets_by_year['set_num'][:-2])
#plt.show()

###################################################################################################

themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns={'theme_id':'nr_themes'}, inplace=True)
#plt.plot(themes_by_year.index[:-2], themes_by_year['nr_themes'][:-2])
#plt.show()

###################################################################################################

#ax1 = plt.gca()
#ax2 = ax1.twinx()

#ax1.plot(sets_by_year.index[:-2], sets_by_year['set_num'][:-2], color='g')
#ax2.plot(themes_by_year.index[:-2], themes_by_year['nr_themes'][:-2], color='b')

#ax1.set_xlabel('Year')
#ax1.set_ylabel('Number of Sets', color='green')
#ax2.set_ylabel('Number of Themes', color='blue')

#plt.show()

###################################################################################################

parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
#plt.scatter(parts_per_set.index[:-2], parts_per_set['num_parts'][:-2])
#plt.show()

###################################################################################################

themes = pd.read_csv('data/themes.csv')
set_theme_count = sets['theme_id'].value_counts()
set_theme_count = pd.DataFrame({
    'id': set_theme_count.index,
    'set_count': set_theme_count.values
})
merged_df = pd.merge(set_theme_count, themes, on='id')

plt.figure(figsize=(14,10))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merged_df['name'][:10], merged_df.set_count[:10])
plt.show()
