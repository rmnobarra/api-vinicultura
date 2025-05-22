# API Vitivinicultura

API para consulta de dados da vitivinicultura brasileira, com foco no Rio Grande do Sul, utilizando **scraping** dinâmico da plataforma da Embrapa.

## Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Uvicorn](https://www.uvicorn.org/)

## Instalação

```bash
git clone https://github.com/seu-usuario/api-vitivinicultura.git
cd api-vitivinicultura
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Documentação automática

Acesse a documentação gerada automaticamente:

- Swagger UI: [`http://localhost:8000/docs`](http://localhost:8000/docs)
- Redoc: [`http://localhost:8000/redoc`](http://localhost:8000/redoc)

---

## Endpoints da API

### `/producao?ano={ano}`

> Retorna os dados de produção de uvas no RS para o ano desejado.

Exemplo de resposta:

```json
{
  "ano": 2023,
  "dados": [
    {"produto": "Uva Isabel", "quantidade": "123456"}
  ]
}
```

Exemplo de chamada:

```bash
curl -X GET "http://localhost:8000/producao?ano=2023"
```

---

### `/processamento?ano={ano}`

> Retorna os dados de processamento de uvas no RS.

Exemplo de resposta:

```json
{
  "ano": 2023,
  "dados": [
    {"cultivar": "BRS Carmem", "quantidade": "98765"}
  ]
}
```

Exemplo de chamada:

```bash
curl -X GET "http://localhost:8000/processamento?ano=2023"
```

---

### `/comercializacao?ano={ano}`

> Retorna os dados de comercialização de vinhos e derivados.

Exemplo de resposta:

```json
{
  "ano": 2023,
  "dados": [
    {"produto": "Vinho de Mesa Tinto", "quantidade": "187016848"}
  ]
}
```

Exemplo de chamada:

```bash
curl -X GET "http://localhost:8000/comercializacao?ano=2023"
```

---

### `/importacao?ano={ano}`

> Dados de importações por país.

Exemplo de resposta:

```json
{
  "ano": 2024,
  "dados": [
    {"pais": "Chile", "quantidade_kg": "73111416", "valor_usd": "199874777"}
  ]
}
```

Exemplo de chamada:

```bash
curl -X GET "http://localhost:8000/importacao?ano=2024"
```

---

### `/exportacao?ano={ano}`

> Dados de exportações por país.

Exemplo de resposta:

```json
{
  "ano": 2024,
  "dados": [
    {"pais": "Paraguai", "quantidade_kg": "3705268", "valor_usd": "5121857"}
  ]
}
```

Exemplo de chamada:

```bash
curl -X GET "http://localhost:8000/exportacao?ano=2024"
```

---

## Observações

- Os dados vão de **1970 até 2023** (ou 2024, conforme aba da Embrapa).
- A API realiza scraping em tempo real — pode haver variação de latência.
- Para evitar sobrecarga, não abuse de chamadas em loop.

---

## Contato

Desenvolvido por @rmnobarra.

