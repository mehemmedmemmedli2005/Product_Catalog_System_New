from typing import List
from app.models.catalog import Catalog

class CatalogService:
    def __init__(self):
        self.catalogs: dict[int, Catalog] = {}

    def add_catalog(self, catalog: Catalog) -> Catalog:
        if catalog.catalog_id in self.catalogs:
            raise ValueError("Catalog ID already exists.")
        self.catalogs[catalog.catalog_id] = catalog
        return catalog

    def search_catalogs(self, query: str) -> List[Catalog]:
        return [
            catalog for catalog in self.catalogs.values()
            if query.lower() in catalog.name.lower()
        ]
