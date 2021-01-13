# Code for Squirrel Data Analysis of Day 25

import pandas

dataframe = pandas.read_csv('./Day 25 - Intermediate - CSV and Pandas/Squirrel Data Analysis/squirrels.csv')

grey_squirrels = len(dataframe[dataframe['Primary Fur Color'] == 'Gray'])
black_squirrels = len(dataframe[dataframe['Primary Fur Color'] == 'Black'])
cinnamon_squirrels = len(dataframe[dataframe['Primary Fur Color'] == 'Cinnamon'])

squirrels_by_colour = {
    'Fur Color': ['Gray', 'Black', 'Cinnamon'],
    'Count': [grey_squirrels, black_squirrels, cinnamon_squirrels]
}

new_dataframe = pandas.DataFrame(squirrels_by_colour)
new_dataframe.to_csv('./Day 25 - Intermediate - CSV and Pandas/Squirrel Data Analysis/squirrels_by_color.csv')
