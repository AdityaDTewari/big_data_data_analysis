# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 22:14:57 2019

@author: Aditya
"""
# dataframes
import pandas as pd

purchase_1 = pd.Series({'Name': 'Chris', 'Item Purchased': 'Dog Food', 'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod', 'Item Purchased': 'Bird Seed', 'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index = ['Store 1', 'Store 1', 'Store 2'])
df.head()

df.loc['Store 2']
df.loc['Store 1']
df.loc['Store 1', 'Cost']
df['Cost']
df.loc['Store 1']['Cost']
df.loc[:, ['Name', 'Cost']]

df.drop('Store 1') #no actual changes

copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
copy_df

del copy_df['Name']
copy_df

df['Location'] = None
df

costs = df['Cost']
costs

costs += 2
costs

df #origibal column changed as well

