from fastapi import APIRouter, Query
from app.services.scraper import scrape_comercializacao
from app.models.schemas import ComercializacaoItem
from typing import List

router = APIRouter()

@router.get("/comercializacao", response_model=List[ComercializacaoItem])
def get_comercializacao(ano: int = Query(2023, ge=1970, le=2023)):
    return scrape_comercializacao()
