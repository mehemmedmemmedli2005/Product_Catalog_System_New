from fastapi import FastAPI
from app.routers import product_router, catalog_router

app = FastAPI()

# Register routers
app.include_router(product_router.router, prefix="/products", tags=["Products"])
app.include_router(catalog_router.router, prefix="/catalogs", tags=["Catalogs"])

@app.get("/")
def root():
    return {"message": "Welcome to the Product Catalog API"}
