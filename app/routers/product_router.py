from fastapi import APIRouter, HTTPException
from app.models.product import Product
from app.services.product_service import ProductService

router = APIRouter()
product_service = ProductService()

@router.post("/")
def add_product(product: Product):
    try:
        created_product = product_service.add_product(product)
        return {"message": "Product added successfully", "product": created_product}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{product_id}")
def edit_product(product_id: int, product: Product):
    try:
        updated_product = product_service.edit_product(product_id, product)
        return {"message": "Product updated successfully", "product": updated_product}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{product_id}")
def delete_product(product_id: int):
    try:
        product_service.delete_product(product_id)
        return {"message": "Product deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/search")
def search_products(query: str):
    results = product_service.search_products(query)
    return {"products": results}
