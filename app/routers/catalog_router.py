from fastapi import APIRouter, HTTPException
from app.models.catalog import Catalog
from app.services.catalog_service import CatalogService

router = APIRouter()
catalog_service = CatalogService()

@router.post("/")
def add_catalog(catalog: Catalog):
    try:
        created_catalog = catalog_service.add_catalog(catalog)
        return {"message": "Catalog added successfully", "catalog": created_catalog}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/search")
def search_catalogs(query: str):
    results = catalog_service.search_catalogs(query)
    return {"catalogs": results}
