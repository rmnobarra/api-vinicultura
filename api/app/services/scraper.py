import requests
from bs4 import BeautifulSoup

def scrape_producao():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    tabela = soup.find("table", class_="tb_base tb_dados")
    if not tabela:
        return []

    dados = []
    linhas = tabela.find("tbody").find_all("tr")
    
    for linha in linhas:
        colunas = linha.find_all("td")
        if len(colunas) >= 2:
            produto = colunas[0].get_text(strip=True)
            quantidade = colunas[1].get_text(strip=True)
            if quantidade and quantidade != "-":
                dados.append({
                    "produto": produto,
                    "quantidade": quantidade
                })
    return dados


def scrape_processamento():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    tabela = soup.find("table", class_="tb_base tb_dados")
    if not tabela:
        return []

    dados = []
    linhas = tabela.find("tbody").find_all("tr")

    for linha in linhas:
        colunas = linha.find_all("td")
        if len(colunas) >= 2:
            cultivar = colunas[0].get_text(strip=True)
            quantidade = colunas[1].get_text(strip=True)
            if quantidade and quantidade != "-":
                dados.append({
                    "cultivar": cultivar,
                    "quantidade": quantidade
                })

    return dados

def scrape_comercializacao():
    import requests
    from bs4 import BeautifulSoup

    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    tabela = soup.find("table", class_="tb_base tb_dados")
    if not tabela:
        return []

    dados = []
    linhas = tabela.find("tbody").find_all("tr")

    for linha in linhas:
        colunas = linha.find_all("td")
        if len(colunas) >= 2:
            produto = colunas[0].get_text(strip=True)
            quantidade = colunas[1].get_text(strip=True)
            if quantidade and quantidade != "-":
                dados.append({
                    "produto": produto,
                    "quantidade": quantidade
                })

    return dados


def scrape_importacao():
    import requests
    from bs4 import BeautifulSoup

    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    tabela = soup.find("table", class_="tb_base tb_dados")
    if not tabela:
        return []

    dados = []
    linhas = tabela.find("tbody").find_all("tr")

    for linha in linhas:
        colunas = linha.find_all("td")
        if len(colunas) >= 3:
            pais = colunas[0].get_text(strip=True)
            quantidade = colunas[1].get_text(strip=True)
            valor = colunas[2].get_text(strip=True)

            # Ignora linhas sem dados
            if quantidade == "-" and valor == "-":
                continue

            dados.append({
                "pais": pais,
                "quantidade_kg": quantidade,
                "valor_usd": valor
            })

    return dados


def scrape_exportacao():
    import requests
    from bs4 import BeautifulSoup

    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    tabela = soup.find("table", class_="tb_base tb_dados")
    if not tabela:
        return []

    dados = []
    linhas = tabela.find("tbody").find_all("tr")

    for linha in linhas:
        colunas = linha.find_all("td")
        if len(colunas) >= 3:
            pais = colunas[0].get_text(strip=True)
            quantidade = colunas[1].get_text(strip=True)
            valor = colunas[2].get_text(strip=True)

            # Ignora entradas sem dados
            if quantidade == "-" and valor == "-":
                continue

            dados.append({
                "pais": pais,
                "quantidade_kg": quantidade,
                "valor_usd": valor
            })

    return dados

