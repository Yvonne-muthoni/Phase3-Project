from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.category import Category
from display import CategoryModel
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/categories')
def categories():
    categories = Category.find_all()
    print(categories)

    return []
@app.post('/categories')
def save(data:CategoryModel):
   pass


@app.get('/products')
def get_products():
    return[{"name":"Expresso"}]

@app.post('/products')
def save_products(data):
    print(data)    