from fastapi import APIRouter
from app.services.scraper import scrape_importacao
from app.models.schemas import ImportacaoItem
from typing import List

router = APIRouter()

@router.get("/importacao", response_model=List[ImportacaoItem])
def get_importacao():
    return scrape_importacao()
