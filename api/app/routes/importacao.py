from fastapi import APIRouter, Query
from app.services.scraper import scrape_importacao
from app.models.schemas import ImportacaoResponse


router = APIRouter()

@router.get("/importacao", response_model=ImportacaoResponse)
def get_importacao(ano: int = Query(2023, ge=1970, le=2024)):
    """Retorna dados de importação de vinhos de mesa por país."""
    dados = scrape_importacao(ano)
    return {"ano": ano, "dados": dados} 
