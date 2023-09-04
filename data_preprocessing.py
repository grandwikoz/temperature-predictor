#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Import necessary libraries

import src.util as utils
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import numpy as np


# In[7]:


# Load configuration file

config = utils.load_config()


# In[8]:


# Load dataset

def load_dataset(config_data: dict) -> pd.DataFrame:
    # Load every set of data
    x_train = utils.pickle_load(config_data["train_set_path"][0])
    y_train = utils.pickle_load(config_data["train_set_path"][1])
    
    x_valid = utils.pickle_load(config_data["valid_set_path"][0])
    y_valid = utils.pickle_load(config_data["valid_set_path"][1])

    x_test = utils.pickle_load(config_data["test_set_path"][0])
    y_test = utils.pickle_load(config_data["test_set_path"][1])

    # Concatenate x and y for faster preprocessing
    train_set = pd.concat([x_train, y_train], axis = 1)
    valid_set = pd.concat([x_valid, y_valid], axis = 1)
    test_set = pd.concat([x_test, y_test], axis = 1)

    
    # Return set of data
    return train_set, valid_set, test_set


# In[9]:


train_set, valid_set, test_set = load_dataset(config)


# In[10]:


train_set.info()


# In[11]:


valid_set.info()


# In[12]:


test_set.info()


# In[13]:


# change non-float null into 'unknown' and float null into median for train data
def impute_train_missing(df):
    columns = list(df.columns.values)
    for column in columns:
        try:
            if df[column].dtypes.name == 'float64':
                median = df[column].median()
                df[column] = df[column].fillna(median)
                
            if df[column].dtypes.name == 'int64':
                df[column] = df[column].fillna('unknown')
                
            else:
                df[column] = df[column].fillna('unknown')
    
        except:
            pass


# In[14]:


train_set_clean = train_set.copy()
impute_train_missing(train_set_clean)


# In[15]:


train_set_clean.info()


# In[16]:


# change non-float null into 'unknown' and float null into median for valid and test data using train data
def impute_valid_test_missing(train_df, imputed_df):
    columns = list(imputed_df.columns.values)
    for column in columns:
        try:
            if imputed_df[column].dtypes.name == 'float64':
                median = train_df[column].median()
                imputed_df[column] = imputed_df[column].fillna(median)
                
            if imputed_df[column].dtypes.name == 'int64':
                imputed_df[column] = imputed_df[column].fillna('unknown')
            
            else:
                imputed_df[column] = imputed_df[column].fillna('unknown')
    
        except:
            pass


# In[17]:


valid_set_clean = valid_set.copy()
impute_valid_test_missing(train_df = train_set, imputed_df = valid_set_clean)


# In[18]:


valid_set_clean.info()


# In[19]:


test_set_clean = test_set.copy()
impute_valid_test_missing(train_df = train_set, imputed_df = test_set_clean)


# In[20]:


test_set_clean.info()


# In[21]:


def train_scaler(train_data, scaler = None):
    """
    Standardizing train data
    :param x: <pandas DataFrame> data
    :param scaler: <sklearn object> scaler, default None
    :return x_scaled: <pandas Dataframe> standardized data
    :param scaler: <sklearn object> scaler, default None
    """
    if scaler != None:
        pass
    else:
        # Buat & fit encoder
        scaler = StandardScaler()
        scaler.fit(train_data)

    # Tranform data
    train_data_scaled = scaler.transform(train_data)
    train_data_scaled = pd.DataFrame(train_data_scaled,
                            columns = train_data.columns,
                            index = train_data.index)
    
    return train_data_scaled, scaler


# In[22]:


numerical_cols = ['RH_avg', 'RR', 'ss', 'ff_x', 'ddd_x', 'ff_avg']


# In[23]:


# standardizing numerical columns in train data using StandardScaler

train_set_clean[numerical_cols], scaler = train_scaler(train_data = train_set_clean[numerical_cols])
train_set_clean.head()


# In[24]:


def valid_test_scaler(data, scaler):  
    # Standardizing test data using train data parameter
    test_data_scaled = scaler.transform(data)
    test_data_scaled = pd.DataFrame(test_data_scaled, columns = data.columns, index = data.index)
    
    
    return test_data_scaled


# In[25]:


# standardizing numerical columns in valid data using StandardScaler

valid_set_clean[numerical_cols] = valid_test_scaler(data = valid_set_clean[numerical_cols], scaler=scaler)
valid_set_clean.head()


# In[26]:


# standardizing numerical columns in test data using StandardScaler

test_set_clean[numerical_cols] = valid_test_scaler(data = test_set_clean[numerical_cols], scaler=scaler)
test_set_clean.head()


# In[27]:


train_set_clean.info()


# In[28]:


valid_set_clean.info()


# In[29]:


test_set_clean.info()


# In[30]:


x_train_clean = train_set_clean[config["input"]]
y_train_clean = train_set_clean[config["output"]]

x_valid_clean = valid_set_clean[config["input"]]
y_valid_clean = valid_set_clean[config["output"]]

x_test_clean = test_set_clean[config["input"]]
y_test_clean = test_set_clean[config["output"]]


# In[31]:


x_train_clean = pd.get_dummies(x_train_clean, columns=['ddd_car','province_id', 'month'], dtype=float)
x_valid_clean = pd.get_dummies(x_valid_clean, columns=['ddd_car','province_id', 'month'], dtype=float)
x_test_clean = pd.get_dummies(x_test_clean, columns=['ddd_car','province_id', 'month'], dtype=float)


# In[32]:


x_train_clean.info()


# In[33]:


x_valid_clean.info()


# In[34]:


x_test_clean.info()


# In[35]:


utils.pickle_dump(x_train_clean, config["train_clean_set_path"][0])
utils.pickle_dump(y_train_clean, config["train_clean_set_path"][1])

utils.pickle_dump(x_valid_clean, config["valid_clean_set_path"][0])
utils.pickle_dump(y_valid_clean, config["valid_clean_set_path"][1])

utils.pickle_dump(x_test_clean, config["test_clean_set_path"][0])
utils.pickle_dump(y_test_clean, config["test_clean_set_path"][1])


# In[ ]:




