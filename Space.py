'''
Locating International Space Station on a graph in python using plotly
'''

#!/usr/bin/env python
# coding: utf-8

# In[5]:


import  pandas as pd
import plotly.express as px


# In[6]:


url = 'http://api.open-notify.org/iss-now.json'


# In[7]:


df = pd.read_json(url)


# In[8]:


df


# In[9]:


df['latitude'] = df.loc['latitude','iss_position']
df['longitude'] = df.loc['longitude','iss_position']
df.reset_index(inplace=True)


# In[10]:


df


# In[11]:


df = df.drop(['index','message'], axis=1)


# In[12]:


df


# In[13]:


fig = px.scatter_geo(df, lat='latitude',
                    lon= 'longitude')

fig.show()


# In[ ]:




