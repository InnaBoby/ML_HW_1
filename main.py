
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd
import pickle
from data_preprocess import data_preproc
from castom_transform import castom_transform

app = FastAPI()


class Item(BaseModel):
    name: str
    year: int
    selling_price: int
    km_driven: int
    fuel: str
    seller_type: str
    transmission: str
    owner: str
    mileage: str
    engine: str
    max_power: str
    torque: str
    seats: float


class Items(BaseModel):
    objects: List[Item]



class Prediction(BaseModel):
    predictions: List[float]


@app.get("/")
async def welcome_message():
    return {"message": "Hello!! Welcome to my first API!"}


@app.post("/predict_item")
def predict_item(name : str,
                 year : int,
                 km_driven	: int,
                 fuel : str,
                 seller_type : str,
                 transmission : str, 
                 owner : str,
                 mileage : str, 
                 engine : str, 
                 max_power : str, 
                 torque : str, 
                 seats : float) -> float:
    data = {'name' : name, 'year' : year, 'km_driven' : km_driven, 'fuel' : fuel, 'seller_type' : seller_type,
            'transmission' : transmission, 'owner' : owner, 'mileage' : mileage, 'engine' : engine, 'max_power' : max_power, 
            'torque' : torque, 'seats' : seats}
    df = pd.DataFrame(data=data)
    with open('Lasso.pkl', 'rb') as f:
        pipe = pickle.load(f)
    df = data_preproc(df) 
    preds = pipe.predict(df)
    return Prediction(preds)     
      

@app.post("/predict_items")
def predict_items(name : List[str],
                 year : List[int],
                 km_driven	: List[int],
                 fuel : List[str],
                 seller_type : List[str],
                 transmission : List[str], 
                 owner : List[str],
                 mileage : List[str], 
                 engine : List[str], 
                 max_power : List[str], 
                 torque : List[str], 
                 seats : List[float]) -> List[float]:
    data = {'name' : name, 'year' : year, 'km_driven' : km_driven, 'fuel' : fuel, 'seller_type' : seller_type,
            'transmission' : transmission, 'owner' : owner, 'mileage' : mileage, 'engine' : engine, 'max_power' : max_power, 
            'torque' : torque, 'seats' : seats}
    df = pd.DataFrame(data=data)
    with open('Lasso.pkl', 'rb') as f:
        pipe = pickle.load(f)
    df = data_preproc(df) 
    preds = pipe.predict(df)
    return Prediction(preds)   
