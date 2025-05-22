from fastapi import APIRouter, Query
from app.services.scraper import scrape_comercializacao
from app.models.schemas import ComercializacaoResponse


router = APIRouter()

@router.get("/comercializacao", response_model=ComercializacaoResponse)
def get_comercializacao(ano: int = Query(2023, ge=1970, le=2023)):
    """Retorna dados de comercialização de vinhos e derivados no RS."""
    dados = scrape_comercializacao(ano)
    return {"ano": ano, "dados": dados} 