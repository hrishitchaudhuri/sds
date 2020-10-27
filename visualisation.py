#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

import math
import os

FILE_PATH=str(os.getcwd()) + '\Data\heart.csv'

heart_data=pd.read_csv(FILE_PATH)

# Preview first 5 rows to verify data load. 
# print(heart_data.head())

"""

Possible hypothesis idea:
    REMEMBER: 'target' --> contains verifiable data. 
    
    What factors relate to the likelihood of exercise causing an angina?
    Check against:
        a. Age
        b. Sex
        c. Cholesterol Levels
        
        NOTE: Fasting blood sugar levels could also correlate to diabetes (?)

"""

# Age-Based Distribution
"""
ages=[i for i in heart_data['age']]
ages.sort()

quart3=ages[math.floor(0.75*len(ages))]
quart1=ages[math.floor(0.25*len(ages))]

IQR=quart3-quart1

# Using Freedman-Diaconis Rule to calculate number of bins:
bns=math.floor(2*IQR/(len(ages)**(1/3)))

heart_data['age'].hist(bins=bns)

# FDR generates too few bins (2). Therefore, by judgment, we will set it to bins=5
heart_data['age'].hist(bins=5)
"""

# Sex-Based Distribution
"""
males=sum([1 for i in heart_data['sex'] if i==1])
females=sum([1 for i in heart_data['sex'] if i==0])

sex=['Males', 'Females']
sex_pos=[0, 1]
sex_counts=[males, females]

style.use('ggplot')
plt.bar(sex_pos, sex_counts, color='blue')
plt.title('Sex Distribution of Dataset')
plt.ylabel('Count')
plt.xticks(sex_pos, sex)
plt.show()
"""
# Therefore, dataset is skewed towards males. 

# Boxplot: Check how presence of heart disease affects each.
# sns.boxplot(x='target',y='chol',data=heart_data) # 1 = male; 0 = female
# sns.boxplot(x='target', y='trestbps', data=heart_data) # Shows outliers. 
# sns.boxplot(x='target', y='thalach', data=heart_data)
# sns.boxplot(x='target', y='oldpeak', data=heart_data)

# NOTE: 0 is an incorrect value. Impute all features with thal=0
# sns.boxplot(x='thal', y='oldpeak', data=heart_data)
# sns.boxplot(x='thal', y='thalach', data=heart_data)
# sns.boxplot(x='thal', y='trestbps', data=heart_data)
# sns.boxplot(x='thal', y='chol', data=heart_data)

# Fasting Blood Sugar: > 120 mg/dl
"""
fbs=[sum([1 for i in heart_data['fbs'] if i==1]), sum([1 for i in heart_data['fbs'] if i==0])]
fbs_cols=['Greater than 120 mg/dl', 'Less than 120 mg/dl']
fbs_pos=[0, 1]

style.use('ggplot')
plt.bar(fbs_pos, fbs)
plt.title("Fasting Blood Sugar")
plt.ylabel("Count")
plt.xticks(fbs_pos, fbs_cols)
plt.show()
"""

# Rest ECG Results
# # # Categorized into Normal, Abnormal, and Hyper.
# # # More information: https://www.hindawi.com/journals/cmmm/2017/8272091/tab1/
"""
ecg=[sum([1 for i in heart_data['restecg'] if i==0]), sum([1 for i in heart_data['restecg'] if i==1]), sum([1 for i in heart_data['restecg'] if i==2])]
ecg_cols=['Normal', 'Abnormal', 'Hyper']
ecg_pos=[0, 1, 2]

style.use('ggplot')
plt.bar(ecg_pos, ecg)
plt.title("Resting ECG Results")
plt.ylabel("Count")
plt.xticks(ecg_pos, ecg_cols)
plt.show()
"""
# NOTE: Although 'Hyper' has comparatively lower values, it is not outlying since it is expected that 
# fewer patients will display 'hyper' values. 

# Exercise Induced Anginas
# # # Has high chances of being correlated to the numerical quantities. If handling correlation, make sure
# # # this is tested properly. 
"""
exas=[sum([1 for i in heart_data['exang'] if i==1]), sum([1 for i in heart_data['exang'] if i==0])]
exas_cols=['Induced Angina', 'No Anginas']
exas_pos=[0, 1]

style.use('ggplot')
plt.bar(exas_pos, exas)
plt.title("Exercise Induced Anginas")
plt.ylabel("Count")
plt.xticks(exas_pos, exas_cols)
plt.show()
"""

# Slop of Peak ST Segment
# # # Categorized into Up, Flat and Down
"""
slp=[sum([1 for i in heart_data['slope'] if i==0]), sum([1 for i in heart_data['slope'] if i==1]), sum([1 for i in heart_data['slope'] if i==2])]
slp_cols=['Up', 'Flat', 'Down']
slp_pos=[0, 1, 2]

style.use('ggplot')
plt.bar(slp_pos, slp)
plt.title("Resting ECG Results")
plt.ylabel("Count")
plt.xticks(slp_pos, slp_cols)
plt.show()
"""