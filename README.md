# temperature-predictor
A simple tool to predict temperature.

# Objective
1. Average temperature
2. Minimum temperature
3. Maximum temperature
Given certain inputs.

# Dataset
Data used for this model was obtained from [Kaggle](https://www.kaggle.com/datasets/greegtitan/indonesia-climate).

# Flow
This model utilizes standard machine learning process, which are:
1. Data preparation
   - Merging `climate` and `station` dataset to obtaion `province_id` for every observations
   - Removing unnecessary columns, namely `station_name`, `region_name`, `latitude`, `longitude`, and `region_id`
   - Converting `date` into datetime and extracting `month` value from it
   - Deleting `date` column, this model will only use `month` value
   - Set a data defense strategy to ensure correct inputs
   - Split data into train, valid and test
   - Dump datasets into pickle
     
2. Data preprocessing
   - Impute `train_data`, float columns with median and others with new label called `unknown`
   - Do the same to `valid_data` and `test_data` only using `train_data` as base to avoid data leakage
   - Scale `train_data`
   - Do the same to `valid_data` and `test_data` only using `train_data` as base to avoid data leakage
   - Dump clean datasets into pickle
  
3. Model building
   - This model uses mean squared error (MSE) as metrics
   - This model uses Gradient Boosting as algorithm
   - Create baseline using mean
   - Fit Gradient Boosting to `train_data`
   - Predict using `train_data`
   - Do subsequent cross validation using `valid_data` and find best parameters
   - Fit Gradient Boosting to `train_data` using said parameters
   - Predict with both `train_data` and `test_data`
   - Repeat for all target outputs (this model intends to find three ouputs, which are average, minimum and maximum temperature)
   - Dump model into pickle using `pickle`

# Docker
1. Backend: runs on host=8000
2. Frontend: runs on streamlit with host=8501

# Cloud
Available through http://52.221.187.13:8501/

# Output
A model used to predict temperature. Based on `test_data`, this model gives result as stated below:

|         | MSE Baseline | MSE Train | MSE Test |
| --------|:------------:| :--------:| :-------:|
| Minumum | 4.924533     | 2.990025  | 3.049104 |
| Maximum | 5.148906     | 2.765183  | 2.328772 |
| Average | 3.466188     | 1.620189  | 1.659483 |
