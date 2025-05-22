from fastapi import APIRouter, Query
from app.services.scraper import scrape_producao
from app.models.schemas import ProducaoItem
from typing import List

router = APIRouter()

@router.get("/producao", response_model=List[ProducaoItem])
def get_producao(ano: int = Query(2023, ge=1970, le=2023)):
    return scrape_producao()
