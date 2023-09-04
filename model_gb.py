#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Import necessary libraries

import src.util as utils
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor


# In[9]:


# Load configuration file

config = utils.load_config()


# In[10]:


# Load dataset

def load_dataset(config_data: dict) -> pd.DataFrame:
    
    # Load every set of data
    x_train_clean = utils.pickle_load(config_data["train_clean_set_path"][0])
    y_train_clean = utils.pickle_load(config_data["train_clean_set_path"][1])
    
    x_valid_clean = utils.pickle_load(config_data["valid_clean_set_path"][0])
    y_valid_clean = utils.pickle_load(config_data["valid_clean_set_path"][1])

    x_test_clean = utils.pickle_load(config_data["test_clean_set_path"][0])
    y_test_clean = utils.pickle_load(config_data["test_clean_set_path"][1])

    # Return set of data
    return x_train_clean, y_train_clean, x_valid_clean, y_valid_clean, x_test_clean, y_test_clean


# In[11]:


x_train_clean, y_train_clean, x_valid_clean, y_valid_clean, x_test_clean, y_test_clean = load_dataset(config)


# In[12]:


x_train_clean.head()


# In[6]:


x_train_clean.columns


# In[22]:


x_train_clean.iloc[0]['ss']


# In[6]:


y_train_clean.head()


# In[7]:


x_valid_clean.head()


# In[8]:


y_valid_clean.head()


# In[9]:


x_test_clean.head()


# In[10]:


y_test_clean.head()


# **Baseline Scores**

# In[11]:


# Create a baseline

y_pred_baseline = y_train_clean.mean()
y_pred_baseline


# In[12]:


Tn_mse_train_baseline = mean_squared_error(y_train_clean['Tn'], y_pred_baseline['Tn'] * np.ones(len(y_train_clean)))
Tn_mse_test_baseline = mean_squared_error(y_test_clean['Tn'], y_pred_baseline['Tn'] * np.ones(len(y_test_clean)))

Tn_mse_train_baseline, Tn_mse_test_baseline


# In[13]:


Tx_mse_train_baseline = mean_squared_error(y_train_clean['Tx'], y_pred_baseline['Tx'] * np.ones(len(y_train_clean)))
Tx_mse_test_baseline = mean_squared_error(y_test_clean['Tx'], y_pred_baseline['Tx'] * np.ones(len(y_test_clean)))

Tx_mse_train_baseline, Tx_mse_test_baseline


# In[14]:


Tavg_mse_train_baseline = mean_squared_error(y_train_clean['Tavg'], y_pred_baseline['Tavg'] * np.ones(len(y_train_clean)))
Tavg_mse_test_baseline = mean_squared_error(y_test_clean['Tavg'], y_pred_baseline['Tavg'] * np.ones(len(y_test_clean)))

Tavg_mse_train_baseline, Tavg_mse_test_baseline


# **Gradient Boosting for Tn**

# In[17]:


grad_tree_Tn = GradientBoostingRegressor(random_state=123)


# In[18]:


grad_tree_Tn.fit(x_train_clean, y_train_clean['Tn'])


# In[19]:


y_pred_train_Tn = grad_tree_Tn.predict(x_train_clean)
y_pred_test_Tn = grad_tree_Tn.predict(x_test_clean)

mse_train_Tn = mean_squared_error(y_pred_train_Tn, y_train_clean['Tn'])
mse_test_Tn = mean_squared_error(y_pred_test_Tn, y_test_clean['Tn'])

mse_train_Tn, mse_test_Tn


# In[52]:


# Create GridSearch for Tn using such parameters as stated in config file
gb_tree_Tn_valid = GradientBoostingRegressor(random_state = 123)

# Run GridSearch
gb_tree_Tn_cv = GridSearchCV(estimator = gb_tree_Tn_valid,
                          param_grid = config['params'],
                          cv = 5,
                          scoring = "neg_mean_squared_error")


# In[21]:


# Fit the model using validation data

gb_tree_Tn_cv.fit(x_valid_clean, y_valid_clean['Tn'])


# In[22]:


# Find the best params
gb_tree_Tn_cv.best_params_


# In[23]:


# Find the best score
gb_tree_Tn_cv.best_score_


# In[25]:


# Refitting a random forest for Tn using the best parameters
gb_tree_Tn_final = GradientBoostingRegressor(n_estimators = gb_tree_Tn_cv.best_params_['n_estimators'],
                                learning_rate = gb_tree_Tn_cv.best_params_["learning_rate"],
                                random_state = 123)


# In[26]:


gb_tree_Tn_final.fit(x_train_clean, y_train_clean['Tn'])


# In[27]:


# Predict
y_pred_train_Tn_final = gb_tree_Tn_final.predict(x_train_clean)
y_pred_test_Tn_final = gb_tree_Tn_final.predict(x_test_clean)

# MSE
mse_train_Tn_final = mean_squared_error(y_train_clean['Tn'], y_pred_train_Tn_final)
mse_test_Tn_final = mean_squared_error(y_test_clean['Tn'], y_pred_test_Tn_final)

mse_train_Tn_final, mse_test_Tn_final


# **Gradient Boosting for Tx**

# In[28]:


grad_tree_Tx = GradientBoostingRegressor(random_state=123)


# In[29]:


grad_tree_Tx.fit(x_train_clean, y_train_clean['Tx'])


# In[30]:


y_pred_train_Tx = grad_tree_Tx.predict(x_train_clean)
y_pred_test_Tx = grad_tree_Tx.predict(x_test_clean)

mse_train_Tx = mean_squared_error(y_pred_train_Tx, y_train_clean['Tx'])
mse_test_Tx = mean_squared_error(y_pred_test_Tx, y_test_clean['Tx'])

mse_train_Tx, mse_test_Tx


# In[53]:


# Create GridSearch for Tx using such parameters as stated in config file
gb_tree_Tx_valid = GradientBoostingRegressor(random_state = 123)

# Run GridSearch
gb_tree_Tx_cv = GridSearchCV(estimator = gb_tree_Tx_valid,
                          param_grid = config['params'],
                          cv = 5,
                          scoring = "neg_mean_squared_error")


# In[32]:


# Fit the model using validation data

gb_tree_Tx_cv.fit(x_valid_clean, y_valid_clean['Tx'])


# In[33]:


# Find the best params
gb_tree_Tx_cv.best_params_


# In[34]:


# Find the best score
gb_tree_Tx_cv.best_score_


# In[35]:


# Refitting a random forest for Tavg using the best parameters
gb_tree_Tx_final = GradientBoostingRegressor(n_estimators = gb_tree_Tx_cv.best_params_['n_estimators'],
                                learning_rate = gb_tree_Tx_cv.best_params_["learning_rate"],
                                random_state = 123)


# In[36]:


gb_tree_Tx_final.fit(x_train_clean, y_train_clean['Tx'])


# In[37]:


# Predict
y_pred_train_Tx_final = gb_tree_Tx_final.predict(x_train_clean)
y_pred_test_Tx_final = gb_tree_Tx_final.predict(x_test_clean)

# MSE
mse_train_Tx_final = mean_squared_error(y_train_clean['Tx'], y_pred_train_Tx_final)
mse_test_Tx_final = mean_squared_error(y_test_clean['Tx'], y_pred_test_Tx_final)

mse_train_Tx_final, mse_test_Tx_final


# **Gradient Boosting for Tavg**

# In[38]:


grad_tree_Tavg = GradientBoostingRegressor(random_state=123)


# In[39]:


grad_tree_Tavg.fit(x_train_clean, y_train_clean['Tavg'])


# In[40]:


y_pred_train_Tavg = grad_tree_Tavg.predict(x_train_clean)
y_pred_test_Tavg = grad_tree_Tavg.predict(x_test_clean)

mse_train_Tavg = mean_squared_error(y_pred_train_Tavg, y_train_clean['Tavg'])
mse_test_Tavg = mean_squared_error(y_pred_test_Tavg, y_test_clean['Tavg'])

mse_train_Tavg, mse_test_Tavg


# In[54]:


# Create GridSearch for Tavg using such parameters as stated in config file
gb_tree_Tavg_valid = GradientBoostingRegressor(random_state = 123)

# Run GridSearch
gb_tree_Tavg_cv = GridSearchCV(estimator = gb_tree_Tavg_valid,
                          param_grid = config['params'],
                          cv = 5,
                          scoring = "neg_mean_squared_error")


# In[42]:


# Fit the model using validation data

gb_tree_Tavg_cv.fit(x_valid_clean, y_valid_clean['Tavg'])


# In[43]:


# Find the best params
gb_tree_Tavg_cv.best_params_


# In[44]:


# Find the best score
gb_tree_Tavg_cv.best_score_


# In[45]:


# Refitting a random forest for Tavg using the best parameters
gb_tree_Tavg_final = GradientBoostingRegressor(n_estimators = gb_tree_Tavg_cv.best_params_['n_estimators'],
                                learning_rate = gb_tree_Tavg_cv.best_params_["learning_rate"],
                                random_state = 123)


# In[46]:


gb_tree_Tavg_final.fit(x_train_clean, y_train_clean['Tavg'])


# In[47]:


# Predict
y_pred_train_Tavg_final = gb_tree_Tavg_final.predict(x_train_clean)
y_pred_test_Tavg_final = gb_tree_Tavg_final.predict(x_test_clean)

# MSE
mse_train_Tavg_final = mean_squared_error(y_train_clean['Tavg'], y_pred_train_Tavg_final)
mse_test_Tavg_final = mean_squared_error(y_test_clean['Tavg'], y_pred_test_Tavg_final)

mse_train_Tavg_final, mse_test_Tavg_final


# **Summary**

# In[48]:


# Summary with train and test using best parameters gained from Cross Validation

mse_baseline = [Tn_mse_train_baseline, Tx_mse_train_baseline, Tavg_mse_train_baseline]
mse_train = [mse_train_Tn_final, mse_train_Tx_final, mse_train_Tavg_final]
mse_test = [mse_test_Tn_final, mse_test_Tx_final, mse_test_Tavg_final]
indexes = ["Tn", "Tx", "Tavg"]

summary_df = pd.DataFrame({"MSE Baseline": mse_baseline,
                           "MSE Train": mse_train,
                           "MSE Test": mse_test},
                          index = indexes)
summary_df


# **Dump model into pickle files**

# In[ ]:


with open('tn_model.pkl', 'wb') as f:
    pickle.dump(gb_tree_Tn_final, f)
    f.close()


# In[ ]:


with open('tx_model.pkl', 'wb') as f:
    pickle.dump(gb_tree_Tx_final, f)
    f.close()


# In[ ]:


with open('tavg_model', 'rb') as f:
    cek = pickle.load(f)
    print(cek)

