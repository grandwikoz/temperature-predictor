#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries

import pandas as pd
import src.util as utils
from sklearn.model_selection import train_test_split


# In[2]:


# Load configuration file

config = utils.load_config()


# In[3]:


# Load dataset

climate = pd.read_csv(config["dataset_path_climate"])
province = pd.read_csv(config["dataset_path_province"])
station = pd.read_csv(config["dataset_path_station"])


# In[4]:


climate.head()


# In[5]:


province.head()


# In[6]:


station.head()


# In[7]:


# Merging data to show province_id for every observation in climate

dataset = pd.merge(climate, station, on='station_id', how='left')
dataset = dataset.drop(['station_name', 'region_name', 'latitude', 'longitude', 'region_id'], axis=1)
dataset.head()


# In[8]:


dataset.info()


# In[9]:


dataset.isnull().sum()/len(climate)


# In[10]:


# Changing 'date' type into datetime

dataset['date'] = pd.to_datetime(dataset['date'], format='%d-%m-%Y')
dataset.info()


# In[11]:


# Adding a column consisting month value with int type

dataset['month'] = dataset['date'].dt.month


# In[12]:


# Drop date and station column
dataset = dataset.drop(['date', 'station_id'], axis=1)


# In[13]:


dataset.head()


# In[14]:


dataset.info()


# In[15]:


# Check data types
def check_data(input_data, config):
    
    assert input_data.select_dtypes("int").columns.to_list() == config["int_columns"], "an error occurs in int column(s)."
    assert input_data.select_dtypes("float").columns.to_list() == config["float_columns"], "an error occurs in float column(s)."
    assert input_data.select_dtypes("object").columns.to_list() == config["object_columns"], "an error occurs in object column(s)."


# In[16]:


check_data(dataset, config)


# In[17]:


x = dataset[config["input"]].copy()
y = dataset[config["output"]].copy()


# In[18]:


x.head()


# In[19]:


y.head()


# In[20]:


# Splitting data into train and test

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 123)


# In[21]:


# Splitting test data into validation and test

x_valid, x_test, y_valid, y_test = train_test_split(x_test, y_test, test_size = 0.2, random_state = 123)


# In[22]:


utils.pickle_dump(dataset, config["dataset_path"])

utils.pickle_dump(x_train, config["train_set_path"][0])
utils.pickle_dump(y_train, config["train_set_path"][1])

utils.pickle_dump(x_valid, config["valid_set_path"][0])
utils.pickle_dump(y_valid, config["valid_set_path"][1])

utils.pickle_dump(x_test, config["test_set_path"][0])
utils.pickle_dump(y_test, config["test_set_path"][1])


# In[23]:


cek = utils.pickle_dump(y_test, config["test_set_path"][1])


# In[24]:


cek.


# In[ ]:




