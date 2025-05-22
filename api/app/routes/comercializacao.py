from fastapi import APIRouter
from app.services.scraper import scrape_comercializacao
from app.models.schemas import ComercializacaoItem
from typing import List

router = APIRouter()

@router.get("/comercializacao", response_model=List[ComercializacaoItem])
def get_comercializacao():
    return scrape_comercializacao()
