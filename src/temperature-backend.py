# import library
from fastapi import FastAPI
from fastapi import Request
import pickle
import uvicorn
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import joblib

# init app
app = FastAPI()

# check status [GET]
@app.get("/")
async def hello():
    return "Hi there, Your API is UP!"

# load model function for Tn 
def load_model_tn():
    # load model
    with open("../model/tn_model.pkl", "rb") as file:
        model_tn = pickle.load(file)
    return model_tn

# load model function for Tx
def load_model_tx():
    # load model
    with open("../model/tx_model.pkl", "rb") as file:
        model_tx = pickle.load(file)
    return model_tx

# load model function for Tavg
def load_model_tavg():
    # load model
    with open("../model/tavg_model.pkl", "rb") as file:
        model_tavg = pickle.load(file)
    return model_tavg


# check model with api [GET]
@app.get("/check-model")
def check_model():
    # load model
    try:
        model_tn = load_model_tn()
        model_tx = load_model_tx()
        model_tavg = load_model_tavg()
        response = {
            "code": 200,
            "messages": "Model is ready!"
        }
    except Exception as e:
        response = {
            "code": 404,
            "messages": "Model is not ready. Please check your path or model.",
            "error": str(e)
        }
    return response


# predict with api [POST]
@app.post("/predict")
async def predict(request: Request):
    # get data from request
    data = await request.json()

    # put all input data into a variable
    predict = [
        data['RH_avg'],
        data['RR'],
        data['ss'],
        data['ff_x'],
        data['ddd_x'],
        data['ff_avg']
    ]

    for input in data["ddd_car"]:
        predict.append(input)
    
    predict.append(0) # to input value for unknown ddd_car in model

    for input in data['month']:
        predict.append(input)
    
    for input in data['province_id']:
        predict.append(input)
    
    predict = np.array(predict)
    predict = predict.reshape(1, -1)

    # load model
    model_tn = load_model_tn()
    model_tx = load_model_tx()
    model_tavg = load_model_tavg()
    
    # predict
    try:
        prediction_tn = round(model_tn.predict(predict)[0])
        prediction_tx = round(model_tx.predict(predict)[0])
        prediction_tavg = round(model_tavg.predict(predict)[0])

        # print(prediction)
        new_line = '\n'
        response = {
            "Code": 200,
            "Message": "Success",
            "Prediction_tavg": f"Average: {prediction_tavg}",
            "Prediction_tn": f"Minimum: {prediction_tn}",
            "Prediction_tx": f"Maximum: {prediction_tx}"
        }
    except Exception as e:
        response = {
            "Code": 404,
            "Message": "Failed",
            "Error": str(e)
        }

    # return response
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)




















