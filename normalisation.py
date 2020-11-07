import pandas as pd
import matplotlib.pyplot as pyplt
import matplotlib.mlab as mlab
import matplotlib as plt
import statistics as st
from math import pow
import math
import os

FILE_PATH=str(os.getcwd()) + '\Data\heart.csv'
df = pd.read_csv(FILE_PATH)
print(df)

#list of all the column headings
col_heads = df.columns
print(col_heads)

#dictionary containing column heading as key and mean of all values in that column as value
col_means = dict([(col, df[col].mean()) for col in col_heads])
print(col_means)

#dictionary containing column heading as key and variance of all values in that column as value
col_variances = dict([(col, pow(df[col].std(), 2)) for col in col_heads])
print(col_variances)

#normalisation/ standardisation of all numeric data (using cumulative distribution for z-scores)
normalized_data = []
for col in col_heads:
    row = [((X - col_means[col]) / pow(col_variances[col], 0.5)) for X in df[col].tolist()]
    normalized_data.append(row)
print(normalized_data)

df_normal = pd.DataFrame(normalized_data, columns = list(range(0,1025)))
df_normal = df_normal.transpose()
df_normal.columns = col_heads
print(df_normal)


# graphical visualisation of normalized data
def plot_histogram(df, col):
    feature = [i for i in df[col]]
    feature.sort()

    quart3 = feature[math.floor(0.75 * len(feature))]
    quart1 = feature[math.floor(0.25 * len(feature))]
    IQR = quart3 - quart1

    # Using Freedman-Diaconis Rule to calculate number of bins:
    bns = math.floor(2 * IQR / (len(feature) ** (1 / 3)))

    if (bns >= 5):
        bns = bns
    else:
        bns = 5

    df[col].hist(bins=bns)

    # add a best fit line to the graph
    line = mlab.normpdf(bns, col_means[col], pow(col_variances[col], 0.5))
    plt.plot(bns, line, 'r--')

    # title and axis labels
    pyplt.xlabel(col)
    pyplt.ylabel('Frequency')
    pyplt.title('Histogram for feature data')
    pyplt.show()


for columns in col_heads:
    plot_histogram(df_normal, columns)
