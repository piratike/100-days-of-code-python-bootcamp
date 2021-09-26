# Code for Day 71

import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')

# First 5 rows of the DataFrame and the last 5
#print(df.head(), df.tail())

# Rows and Columns of the DataFrame
#print(df.shape)

# Columns names
#print(df.columns)

# Check for NaN cells
#print(df.isna())

# Delete the last row
clean_df = df.dropna()
#print(clean_df.tail())

###################################################################################################

max_median_starting_salary = df['Starting Median Salary'].max()
id_max_median_starting_salary = df['Starting Median Salary'].idxmax()
major_with_max_median_starting_salary = df['Undergraduate Major'].loc[id_max_median_starting_salary]
#print(max_median_starting_salary, id_max_median_starting_salary, major_with_max_median_starting_salary)

# What college major has the highest mid-career salary? How much do graduates with this major earn?
max_mid_career_median_salary = df['Mid-Career Median Salary'].max()
id_max_mid_career_median_salary = df['Mid-Career Median Salary'].idxmax()
major_with_max_mid_career_median_salary = df['Undergraduate Major'].loc[id_max_mid_career_median_salary]
#print(major_with_max_mid_career_median_salary, max_mid_career_median_salary)

# Which college major has the lowest starting salary and how much do graduates earn after university?
min_starting_median_salary = df['Starting Median Salary'].min()
id_min_starting_median_salary = df['Starting Median Salary'].idxmin()
major_with_min_median_starting_salary = df['Undergraduate Major'].loc[id_min_starting_median_salary]
#print(major_with_min_median_starting_salary, min_starting_median_salary)

# Which college major has the lowest mid-career salary and how much can people expect to earn with this degree?
min_mid_career_median_salary = df['Mid-Career Median Salary'].min()
id_min_mid_career_median_salary = df['Mid-Career Median Salary'].idxmin()
major_with_min_median_starting_salary = df['Undergraduate Major'].loc[id_min_mid_career_median_salary]
#print(major_with_min_median_starting_salary, min_mid_career_median_salary)

###################################################################################################

major_risk = df['Mid-Career 90th Percentile Salary'].subtract(df['Mid-Career 10th Percentile Salary'])
df.insert(1, 'Spread', major_risk)
low_risk = df.sort_values('Spread')
#print(low_risk[['Undergraduate Major', 'Spread']].head())

# 5 Major with highest potential
highest_potential = df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
#print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())

# Degrees with highest spread
high_risk = df.sort_values('Spread', ascending=False)
#print(high_risk[['Undergraduate Major', 'Spread']].head())

# Degrees with highest difference
highest_potential = df.sort_values('Mid-Career Median Salary', ascending=False)
#print(highest_potential[['Undergraduate Major', 'Mid-Career Median Salary']].head())

###################################################################################################

grouped_count = df.groupby('Group').count()
grouped_mean = df.groupby('Group').mean()
#print(grouped_count)
#print(grouped_mean)

pd.options.display.float_format = '{:,.2f}'.format

#print(grouped_count)
#print(grouped_mean)
