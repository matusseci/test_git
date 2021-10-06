# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 11:33:46 2021

@author: Matúš Seči
"""

# Import libraries
import pandas as pd 
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Series (basically vectors in R) 
my_series = pd.Series([4.6, 2.1, -4.0, 3.0])
print(my_series) # prints: index, values, and data type 
print(my_series.values)

### DataFrames
## Dictionary -> DataFrames
scottish_hills = {'Ben Nevis': (1345, 56.79685, -5.003508),
                  'Ben Macdui': (1309, 57.070453, -3.668262),
                  'Braeriach': (1296, 57.078628, -3.728024),
                  'Cairn Toul': (1291, 57.054611, -3.71042),
                  'Sgòr an Lochain Uaine': (1258, 57.057999, -3.725416)}

df = pd.DataFrame(scottish_hills)

## Long format version
scottish_hills = {'Hill Name': ['Ben Nevis', 'Ben Macdui', 'Braeriach', 'Cairn Toul', 'Sgòr an Lochain Uaine'],
                  'Height': [1345, 1309, 1296, 1291, 1258],
                  'Latitude': [56.79685, 57.070453, 57.078628, 57.054611, 57.057999],
                  'Longitude': [-5.003508, -3.668262, -3.728024, -3.71042, -3.725416]}

df = pd.DataFrame(scottish_hills, columns=['Hill Name', 'Height', 'Latitude', 'Longitude'])

print(df)

## Exploring the dataframes
# Head
print(df.head(3))

# Tail
print(df.tail(3))

# Column
print(df['Hill Name']) # has to be specified by name, does not work with index
print(df.Height)

# iloc stands for Integer Location
print(df.iloc[0]) # displays the first row
print(df.iloc[0,0]) # displays the first element of the first row
print(df['Hill Name'][0])

# Filtering DataFrames
print(df.Height > 1300)
print(df[df.Height > 1300])

# Appending data to DFs
df['Region'] = ['Grampian', 'Cairngorm', 'Cairngorm', 'Cairngorm', 'Cairngorm']
print(df)

# Reading data from spreadsheets
df = pd.read_csv('scottish_hills.csv')
print(df.head(10))

# IMPORTANT DIFFERENCE WITH R: Indexing in Python starts at 0, not 1. 

# Sorting the dataframe
sorted_hills = df.sort_values(by=['Height'], ascending = False)
print(sorted_hills.head())


### Plotting with MatPlotLib
x = df.Height
y = df.Latitude

plt.scatter(x,y)
plt.show() # or save the plot by using plt.savefig('chart_name.png')


# Plot linear regression 
stats = linregress(x,y)

m = stats.slope
b = stats.intercept

# Change the default figure size
plt.figure(figsize=(10,10))

# Change the default marker for the scatter from circles to x's
plt.scatter(x, y, marker='x')

# Set the linewidth on the regression line to 3px
plt.plot(x, m * x + b, color="red", linewidth=3)

plt.xlabel("Height (m)", fontsize=20)
plt.ylabel("Latitude", fontsize=20)

# Set the font size of the number lables on the axes
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

print('\nr-value = ' + str(round(stats.rvalue, 2)) + '\np-value = ' + str(round(stats.pvalue, 2)))




























