from fastapi import APIRouter, Query
from app.services.scraper import scrape_importacao
from app.models.schemas import ImportacaoItem
from typing import List

router = APIRouter()

@router.get("/importacao", response_model=List[ImportacaoItem])
def get_importacao(ano: int = Query(2023, ge=1970, le=2023)):
    return scrape_importacao()
