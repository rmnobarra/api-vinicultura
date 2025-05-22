# API Vitivinicultura

API para consulta de dados da vitivinicultura brasileira, com foco no Rio Grande do Sul, utilizando **scraping** dinâmico da plataforma da Embrapa.

## Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Uvicorn](https://www.uvicorn.org/)
- [OAuth2 + JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

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

- Swagger UI: [`http://localhost:8000/docs`](http://localhost:8000/docs)
- Redoc: [`http://localhost:8000/redoc`](http://localhost:8000/redoc)

---

## Autenticação

A API utiliza **JWT com OAuth2 (password flow)** para proteger os dados.

### Como obter o token

1. Acesse [`/docs`](http://localhost:8000/docs)
2. Clique no botão **Authorize**
3. Informe:
   - **username**: `admin`
   - **password**: `1234`
4. Clique em **Authorize** e **Close**

O token será utilizado automaticamente nas rotas protegidas.

### Obter token via curl

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=1234"
```

---

## Endpoints da API

### `/producao?ano={ano}`
> Retorna os dados de produção de uvas no RS para o ano desejado.

```bash
curl -H "Authorization: Bearer <TOKEN>" "http://localhost:8000/producao?ano=2023"
```

### `/processamento?ano={ano}`
> Retorna os dados de processamento de uvas no RS.

### `/comercializacao?ano={ano}`
> Retorna os dados de comercialização de vinhos e derivados.

### `/importacao?ano={ano}`
> Dados de importações por país.

### `/exportacao?ano={ano}`
> Dados de exportações por país.

---

## Observações

- Os dados vão de **1970 até 2023** (ou 2024, conforme aba da Embrapa).
- A API realiza scraping em tempo real — pode haver variação de latência.
- Para evitar sobrecarga, não abuse de chamadas em loop.

---

## Contato

Desenvolvido por @rmnobarra.