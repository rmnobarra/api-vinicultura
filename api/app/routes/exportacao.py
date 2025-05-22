from fastapi import APIRouter
from app.services.scraper import scrape_exportacao
from app.models.schemas import ExportacaoItem
from typing import List

router = APIRouter()

@router.get("/exportacao", response_model=List[ExportacaoItem])
def get_exportacao():
    return scrape_exportacao()
