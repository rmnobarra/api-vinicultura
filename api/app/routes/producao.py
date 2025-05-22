from fastapi import APIRouter
from app.services.scraper import scrape_producao
from app.models.schemas import ProducaoItem
from typing import List

router = APIRouter()

@router.get("/producao", response_model=List[ProducaoItem])
def get_producao():
    return scrape_producao()
