from fastapi import APIRouter
from app.services.scraper import scrape_processamento
from app.models.schemas import ProcessamentoItem
from typing import List

router = APIRouter()

@router.get("/processamento", response_model=List[ProcessamentoItem])
def get_processamento():
    return scrape_processamento()
