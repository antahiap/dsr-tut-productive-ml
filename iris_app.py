from fastapi import FastAPI, Request
from joblib import load
from pydantic import BaseModel

app = FastAPI()

clf = load('model/iris_hp_model.joblib')


class Prediction(BaseModel):
    prediction: int 

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/predict", response_model=Prediction)
def predict(req:Request):

    query_params =  req.query_params

    data = [
        query_params['sequallength'],
        query_params['sequalwidth'],
        # query_params['petallength'],
        # query_params['petalwidth']
    ]

    # call the model
    pred = clf.predict([data])

    return {'prediction': int(pred)}

