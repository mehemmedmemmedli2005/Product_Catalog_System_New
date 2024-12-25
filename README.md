# Product_Catalog_System_New
This project implements a REST API for a Product Catalog System using FastAPI and OOP principles. The API allows users to manage products and their associated catalogs.

# Features

*Add Product with its associated catalog.*

*Edit Product details.*

*Delete Product.*

*Search Products or Catalogs by name or ID.*

*Manage Catalogs (add and search).*

# Folder Structure
product_catalog_system/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── product.py
│   │   ├── catalog.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── product_service.py
│   │   ├── catalog_service.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── product_router.py
│   │   ├── catalog_router.py
│   ├── main.py
├── requirements.txt

#  Project Details

# Models

Product:

product_id: Unique identifier for the product.

name: Name of the product.

catalog_id: Identifier for the associated catalog.

description: Optional description of the product.

price: Price of the product.

Catalog:

catalog_id: Unique identifier for the catalog.

name: Name of the catalog.

Services

ProductService: Handles CRUD operations for products.

CatalogService: Handles catalog operations.

Routers

Product Router: Defines product-related API endpoints.

Catalog Router: Defines catalog-related API endpoints.
