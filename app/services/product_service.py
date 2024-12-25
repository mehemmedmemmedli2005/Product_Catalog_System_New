from typing import List, Optional
from app.models.product import Product

class ProductService:
    def __init__(self):
        self.products: dict[int, Product] = {}

    def add_product(self, product: Product) -> Product:
        if product.product_id in self.products:
            raise ValueError("Product ID already exists.")
        self.products[product.product_id] = product
        return product

    def edit_product(self, product_id: int, updated_product: Product) -> Product:
        if product_id not in self.products:
            raise ValueError("Product not found.")
        self.products[product_id] = updated_product
        return updated_product

    def delete_product(self, product_id: int):
        if product_id not in self.products:
            raise ValueError("Product not found.")
        del self.products[product_id]

    def search_products(self, query: str) -> List[Product]:
        return [
            product for product in self.products.values()
            if query.lower() in product.name.lower() or query.lower() in str(product.catalog_id).lower()
        ]
