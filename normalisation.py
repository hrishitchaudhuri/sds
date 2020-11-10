import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import statistics as st
from math import pow
import math
import os
import numpy as np
from scipy.stats import norm

FILE_PATH=str(os.getcwd()) + '\Data\heart.csv'
df = pd.read_csv(FILE_PATH)

#list of all the column headings
col_heads = df.columns

#dictionary containing column heading as key and mean of all values in that column as value
col_means = dict([(col, df[col].mean()) for col in col_heads])
print("Means of respective columns: ", col_means)

#dictionary containing column heading as key and variance of all values in that column as value
col_variances = dict([(col, pow(df[col].std(), 2)) for col in col_heads])
print("Variances of respective columns: ",col_variances)

#normalisation/ standardisation of all numeric data (using cumulative distribution for z-scores)
normalized_data = []
for col in col_heads:
    row = [((X - col_means[col]) / pow(col_variances[col], 0.5)) for X in df[col].tolist()]
    normalized_data.append(row)

df_normal = pd.DataFrame(normalized_data, columns = list(range(0,1025)))
df_normal = df_normal.transpose()
df_normal.columns = col_heads

#graphical visualisation of normalized data 
def plot_normal(df, col):
    feature=[i for i in df[col]]
    feature.sort()
    
    plt.plot(feature, norm.pdf(feature, 0, 1), color = 'green', label = 'Normal curve')

    # title and axis labels
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.title('Normal curve (bell shaped) for feature data')
    
    plt.show()

#normal plots for normalized data in each column
for columns in col_heads:
    plot_normal(df_normal, columns)

#find the categorical variables from the histograms
categorical_vars = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal', 'target']

#plot normal curves only for continuous variables
for columns in col_heads:
    if(columns not in categorical_vars):
        plot_normal(df_normal, columns)

#age, trestbps, chol and thalach are approximately normally distributed, trestbps and chol having slightly extended tails
