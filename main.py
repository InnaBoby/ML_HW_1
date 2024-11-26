
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, List
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


@app.get("/")
async def predict_price(file: Union [Item, Items]):
     content = await file.read()
     df = pd.read_csv(pd.compat.StringIO(content.decode('utf-8')))
     with open('/content/Lasso.pkl', 'rb') as f:
         pipe = pickle.load(f)
     df = data_preproc(df)    
     if type(df) == Items:
         return Prediction(pipe.predict(df))
     elif type(df) == Item:
         return Prediction(pipe.predict(pd.DataFrame(df).T))
     else:
         return 'Не корректный формат данных' 
    



# @app.post("/predict_item")
# def predict_item(item: Item) -> float:
#     return ...


# @app.post("/predict_items")
# def predict_items(items: List[Item]) -> List[float]:
#     return ...
     
