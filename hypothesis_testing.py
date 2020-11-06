# Importing libraries
import pandas as pd
import numpy as np
import math
import os
from scipy import stats


# Read csv file into a pandas dataframe
data = pd.read_csv("cleaned_data.csv")


#seeing no of rows and cols, checking for empty values
data.shape
data.isna().any()


#view the rows and cols
data['cal'].value_counts()
data['thal'].value_counts()


#creating the contingency table
contingency_table=pd.crosstab(data.ca, data.thal, margins=True)


# Other hypotheses:
#contingency_table=pd.crosstab(data.fbs, data.target, margins=True)
#contingency_table=pd.crosstab(data.age, data.thal, margins=True)
#contingency_table=pd.crosstab(data.restecg, data.exang, margins=True)


print (contingency_table)


#calculating expected and showing observed values
Observed_Values = contingency_table.values 
#print("The observed Values:\n",Observed_Values)

e=stats.chi2_contingency(contingency_table)
Expected_Values = e[3]
#print("Expected Values :\n",Expected_Values)


no_of_rows=len(contingency_table.iloc[1:,0])
#print(no_of_rows)
no_of_columns=len(contingency_table.iloc[0,0:2])
#print(no_of_columns)
ddof=(no_of_rows-1)*(no_of_columns-1)
print("Degree of Freedom:",ddof)
alpha = 0.05


#calculating chi square statistic
from scipy.stats import chi2
chi_square=sum([(o-e)**2./e for o,e in zip(Observed_Values,Expected_Values)])
chi_square_statistic=chi_square[0]+chi_square[1]
#print("chi-square statistic:-",chi_square_statistic)


#calaculating critical value
critical_value=chi2.ppf(q=1-alpha,df=ddof)
#print('critical_value:',critical_value)


#calculating p-value
p_value=1-chi2.cdf(x=chi_square_statistic,df=ddof)
#print('p-value:',p_value)


print('Significance level: ',alpha)
print('Degree of Freedom: ',ddof)
print('chi-square statistic:',chi_square_statistic)
print('critical_value:',critical_value)
print('p-value:',p_value)


#result based on critical value
if chi_square_statistic>=critical_value:
    print("Reject H0,There is a relationship between the two")
else:
    print("Fail to reject H0,There is no relationship between the two")
    
    
#result based on p value    
if p_value<=alpha:
    print("Reject H0,There is a relationship between the two")
else:
    print("Fail to reject H0,There is no relationship between the two")