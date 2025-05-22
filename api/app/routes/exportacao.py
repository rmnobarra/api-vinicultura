from fastapi import APIRouter, Query
from app.services.scraper import scrape_exportacao
from app.models.schemas import ExportacaoResponse


router = APIRouter()

@router.get("/exportacao", response_model=ExportacaoResponse)
def get_exportacao(ano: int = Query(2023, ge=1970, le=2024)):
    """Retorna dados de exportação de vinhos de mesa por país."""
    dados = scrape_exportacao(ano)
    return {"ano": ano, "dados": dados} 
