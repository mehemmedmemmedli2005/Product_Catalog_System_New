from pydantic import BaseModel

class Catalog(BaseModel):
    catalog_id: int
    name: str
