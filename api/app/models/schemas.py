from pydantic import BaseModel


class ProducaoItem(BaseModel):
    produto: str
    quantidade: str

class ProcessamentoItem(BaseModel):
    cultivar: str
    quantidade: str

class ComercializacaoItem(BaseModel):
    produto: str
    quantidade: str

class ImportacaoItem(BaseModel):
    pais: str
    quantidade_kg: str
    valor_usd: str


class ExportacaoItem(BaseModel):
    pais: str
    quantidade_kg: str
    valor_usd: str
