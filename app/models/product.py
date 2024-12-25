from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    product_id: int
    name: str
    catalog_id: int
    description: Optional[str] = None
    price: float
