from fastapi import APIRouter, Query
from app.services.scraper import scrape_exportacao
from app.models.schemas import ExportacaoItem
from typing import List

router = APIRouter()

@router.get("/exportacao", response_model=List[ExportacaoItem])
def get_exportacao(ano: int = Query(2023, ge=1970, le=2023)):
    return scrape_exportacao()
