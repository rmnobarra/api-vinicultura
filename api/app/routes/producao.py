from fastapi import APIRouter, Query
from app.services.scraper import scrape_producao
from app.models.schemas import ProducaoResponse

router = APIRouter()

@router.get("/producao", response_model=ProducaoResponse)
def get_producao(ano: int = Query(2023, ge=1970, le=2023)):
    """Retorna dados de produção vitivinícola do RS."""
    dados = scrape_producao(ano)
    return {"ano": ano, "dados": dados} 
