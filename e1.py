# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:37:54 2019

@author: Aditya
"""
# working on data series in
import pandas as pd
animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)
numbers = [1, 2, 3]
pd.Series(numbers)

# for data that is not available
animals = ['Tiger', 'Bear', None]
pd.Series(animals)
numbers = [1, 2, None]
pd.Series(numbers)

sports = {'Archery': 'Bhutan', 'Golf': 'Scotland', 'Sumo': 'Japan', 'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s

s.index

s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
s


# Querying a serries

sports = {'Archery': 'Bhutan', 'Golf': 'Scotland', 'Sumo': 'Japan', 'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s
s.iloc[3]
s.loc['Golf']

s = pd.Series([100.00, 120.00, 101.00, 3.00])
s

total = 0
for item in s:
    total += item
print(total)

# vectorization

import numpy as np
total = np.sum(s)
print(total)

s = pd.Series(np.random.randint(0, 1000, 10000))
s.head() #for first five
len(s)

# using cellular magic functions for jupyter
"""
just used to time and find out more efficient method

%%timeit -n 100
summary = 0
for item in s:
    summary += item

%%timeit -n 100
summary = 0
summary = np.sum(s)

"""

# vectorization

s += 2
s.head()

for label, value in s.iteritems():
    s.set_value(label, value+2)
s.head()

""" can check agoin using timeit """

s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
s

original_sports = pd.Series({'Archery': 'Bhutan', 'Golf': 'Scotland', 'Sumo': 'Japan', 'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia', 'Bardados', 'Pakistan', 'England'], index = ['Cricket', 'Cricket', 'Cricket', 'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)
