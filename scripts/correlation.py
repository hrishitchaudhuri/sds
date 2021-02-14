#/usr/bin/env python3

import pandas as pd
from numpy import mean
from numpy import std
from numpy import cov
from matplotlib import pyplot as plt

def loaddata(filename):
	global hcd
	# Read the input data file
	hcd = pd.read_csv(filename)

def init_corrout():
	global corrout
	# Initialize 2-dimensional correlation output matrix
	corrout = []
	new = []
	for i in range(0, len(hcd.columns)):
		new = [0.0 for i in range(len(hcd.columns))]
		corrout.append(new)
		new = []

'''
from scipy.stats import pearsonr

# Alternate method using pearsonr from scipy.stats to get the correlation
# The 2 columns to be correlated

col = 0
for data1_col in hcd.columns:
    col = col + 1
    for data2_col in hcd.columns[col:]:
       cordata1 = [i for i in hcd[data1_col]]
       cordata2 = [i for i in hcd[data2_col]]
       corr, _ = pearsonr(cordata1, cordata2)

       print('Pearsons correlation for %s with %s: %.3f' % (data1_col, data2_col, corr))
'''

# pearsons correlation
def my_pearsonr(x, y):
	cor = cov(x, y) / (std(x) * std(y))
	return cor[0][1]

# File path
FILE_NAME='./Data/cleaned_data.csv'

# Calling function loaddata to read the file
loaddata(FILE_NAME)

# Calling function init_corrout to get the 2-dimensional output matrix
init_corrout()


# Printing the correlation values
row = 0
for data1_col in hcd.columns:
    col = 0
    for data2_col in hcd.columns:
        cordata1 = [i for i in hcd[data1_col]]
        cordata2 = [i for i in hcd[data2_col]]
        corr = my_pearsonr(cordata1, cordata2)
        corrout[row][col] = corr;
        col += 1

        print('Pearsons correlation for %s with %s: %.3f' % (data1_col, data2_col, corr))
    row += 1

# Plot the correlations as a bar graph
colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'b' ]

col = -1
for rowdata in corrout:
	col += 1
	plt.bar(hcd.columns, rowdata, color=colours[col], align='center')
	plt.title("Heart Correlation with '%s'" %(hcd.columns[col]))
	plt.ylabel('Correlation')
	plt.show()

