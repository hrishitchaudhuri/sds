#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing libraries
import pandas as pd
import numpy as np
import statistics

heart_data = pd.read_csv("heart_dataset.csv")


# In[2]:


#imputing categorical variables with mode
mode_sex=statistics.mode(heart_data['sex'])
heart_data['sex'].fillna(mode_sex, inplace=True)

mode_fbs=statistics.mode(heart_data['fbs'])
heart_data['fbs'].fillna(mode_fbs, inplace=True)



# In[31]:



mode_exang=statistics.mode(heart_data['exang'])
heart_data['exang'].fillna(mode_exang, inplace=True)

mode_thal=statistics.mode(heart_data['thal'])
heart_data['thal'].fillna(mode_thal, inplace=True)


# In[32]:



mode_target=statistics.mode(heart_data['target'])
heart_data['target'].fillna(mode_target, inplace=True)

mode_cp=statistics.mode(heart_data['cp'])
heart_data['cp'].fillna(mode_cp, inplace=True)


# In[33]:


print(heart_data.head())


# In[34]:


#mean-


# In[35]:

#imputing normally distributed numerical variables with mean
mean_age=(heart_data['age']).median()
heart_data['age'].fillna(mean_age, inplace=True)


# In[36]:



# In[37]:

#imputing numerical variables with skewed distribution by median
median_trestbps=(heart_data['trestbps']).median()
heart_data['trestbps'].fillna(median_trestbps, inplace=True)


# In[38]:




# In[39]:


median_chol=(heart_data['chol']).median()
heart_data['chol'].fillna(median_chol, inplace=True)


# In[40]:


median_thalach=(heart_data['thalach']).median()
heart_data['thalach'].fillna(median_thalach, inplace=True)


# In[41]:


median_oldpeak=(heart_data['oldpeak']).median()
heart_data['oldpeak'].fillna(median_oldpeak, inplace=True)


# In[42]:


median_ca=(heart_data['ca']).median()
heart_data['ca'].fillna(median_ca, inplace=True)


# In[43]:




# In[44]:


# In[45]:


mean_slope=(heart_data['slope']).mean()
heart_data['slope'].fillna(mean_slope, inplace=True)


# In[46]:


median_restecg=(heart_data['restecg']).median()
heart_data['restecg'].fillna(median_restecg, inplace=True)


# In[47]:

#checking if there are any missing values 
heart_data.isnull().sum()


# In[48]:

#converting data back to csv format
heart_data.to_csv('cleaned_data.csv', header=True, index=False) 


# In[ ]:




