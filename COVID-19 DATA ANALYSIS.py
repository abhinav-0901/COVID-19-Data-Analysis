#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
print('MODULES ARE IMPORTED')


# In[7]:


corona_dataset=pd.read_csv("Desktop/PYTHON_WORK/time_series_covid19_confirmed_global.csv")
corona_dataset.head(20)


# In[8]:


corona_dataset.shape


# In[15]:


corona_dataset


# In[16]:


corona_dataset_agg=corona_dataset.groupby("Country/Region").sum()


# In[19]:


corona_dataset_agg.head()

corona_dataset_agg.shape
# In[20]:


corona_dataset_agg.shape


# In[42]:


corona_dataset_agg.loc["India"].plot()

corona_dataset_agg.loc["Spain"].plot()
corona_dataset_agg.loc["China"].plot()
corona_dataset_agg.loc["Pakistan"].plot()
plt.legend()


# In[ ]:





# In[30]:


corona_dataset_agg.loc["India"].diff().plot()


# In[32]:


corona_dataset_agg.loc["India"].diff().max()


# In[33]:


corona_dataset_agg.loc["US"].diff().max()


# In[37]:


countries = list(corona_dataset_agg.index)
max_infected_rate=[]

for c in countries:
    max_infected_rate.append(corona_dataset_agg.loc[c].diff().max())

corona_dataset_agg["Max Infected Rate"]=max_infected_rate

corona_dataset_agg.head()


# In[40]:


corona_data=pd.DataFrame(corona_dataset_agg["Max Infected Rate"])
corona_data.head(10)


# In[43]:


WorldHappiness=pd.read_csv("Desktop/PYTHON_WORK/datasets_894_813759_2019.csv")
WorldHappiness.head(20)


# In[53]:


#WorldHappiness.drop(["Overall rank","Generosity","Perceptions of corruption","Score"],axis = 1, inplace = True)
WorldHappiness.head()
WorldHappiness.set_index("Country or region", inplace = True)


# In[ ]:





# In[ ]:





# In[54]:


data = corona_data.join(WorldHappiness, how = "inner")
data.head(20)


# In[55]:


data.corr()


# In[61]:


y=data['Max Infected Rate']
x=data['GDP per capita']
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))


# In[62]:


y=data['Max Infected Rate']
x=data['Social support']
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))


# In[63]:


y=data['Max Infected Rate']
x=data['Healthy life expectancy']
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))


# In[65]:


y=data['Max Infected Rate']
x=data['Freedom to make life choices']
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))

