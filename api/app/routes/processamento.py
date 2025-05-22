from fastapi import APIRouter, Query
from app.services.scraper import scrape_processamento
from app.models.schemas import ProcessamentoResponse

router = APIRouter()

@router.get("/processamento", response_model=ProcessamentoResponse)
def get_processamento(ano: int = Query(2023, ge=1970, le=2023)):
    """
    Retorna dados de processamento de uvas para o ano especificado.

    - **ano**: entre 1970 e 2023. Por padrão, retorna 2023.
    """
    dados = scrape_processamento(ano)
    return {"ano": ano, "dados": dados}
