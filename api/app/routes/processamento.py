from fastapi import APIRouter, Query
from app.services.scraper import scrape_processamento
from app.models.schemas import ProcessamentoItem
from typing import List

router = APIRouter()

@router.get("/processamento", response_model=List[ProcessamentoItem])
def get_processamento(ano: int = Query(2023, ge=1970, le=2023)):
    return scrape_processamento()
