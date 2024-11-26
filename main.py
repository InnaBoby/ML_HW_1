
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


@app.post("/predict_item", response_model=Prediction)
def predict_item(item: Item) -> float:
    df = pd.DataFrame([el.dict() for el in item.objects])
    with open('Lasso.pkl', 'rb') as f:
        pipe = pickle.load(f)
    df = data_preproc(df) 
    preds = pipe.predict(df)
    return Prediction(preds)     
      

@app.post("/predict_items")
def predict_items(items: List[Item]) -> List[float]:
    df = pd.DataFrame([el.dict() for el in item.objects])
    with open('Lasso.pkl', 'rb') as f:
        pipe = pickle.load(f)
    df = data_preproc(df) 
    preds = pipe.predict(df)
    return Prediction(preds)   
