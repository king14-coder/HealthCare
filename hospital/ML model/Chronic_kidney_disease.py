import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Kidneydisease/kidney_disease.csv')
# print(df)
columns = pd.read_csv('Kidneydisease/data_description.txt')
print(columns)

# First we seperate the attributes
columns = pd.read_csv('Kidneydisease/data_description.txt',sep='-')
columns=columns.reset_index()

# Here we can change change the names of attributes
columns.columns=['cols','new_columns']
print(columns)

# we can change all the names simultaneously with this
df.columns = columns['new_columns'].values
print(df)