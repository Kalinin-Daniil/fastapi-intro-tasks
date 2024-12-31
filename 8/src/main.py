from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class ProductSpecifications(BaseModel):
    size: str = Field(..., example="M")
    color: str = Field(..., example="Red")
    material: str = Field(..., example="Cotton")

class Product(BaseModel):
    id: int = None 
    name: str = Field(..., example="T-Shirt")
    price: float = Field(..., gt=0) 
    specifications: ProductSpecifications

class ProductResponse(BaseModel):
    message: str
    product: Product

class ProductsResponse(BaseModel):
    products: List[Product]

@app.post("/product", response_model=ProductResponse)
async def add_product(product: Product):
    global product_id_counter

    product.id = product_id_counter
    product_list.append(product)
    product_id_counter += 1

    return {"message": "Product added successfully", "product": product}

@app.get("/products", response_model=ProductsResponse)
async def get_products():
    return {"products": product_list} 
# END
