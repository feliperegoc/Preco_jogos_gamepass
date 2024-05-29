from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import json
import time

url = 'https://www.xbox.com/pt-BR/xbox-game-pass/games#pcgames'

driver = webdriver.Chrome()
driver.get(url)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@name='clearFilters']")))
time.sleep(20)

# Pressionando botão de carregar mais até não estar mais disponivel.
while True:
    try:
        carregar_mais = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(.,'CARREGAR MAIS')]")))
        carregar_mais.click()
        time.sleep(1)
    except TimeoutException:
        break  # Quando não houver mais o botão "Carregar mais" disponivel, sair do loop.

# Obtendo html
html = driver.page_source

# Analisando o html com o bs4.
soup = BeautifulSoup(html, 'html.parser')

# Encontrando todos os jogos disponiveis.
jogos = soup.select('div.gameDivsWrapper section.m-product-placement-item.f-size-medium.context-game.gameDiv')

print(f"{len(jogos)} jogos encontrados.")

# Criando listas para armazenar resultados.
informacoes_jogos = []
jogos_sem_preco = []

# Iterando sob os itens encontrados para extrair informações.
for jogo in jogos:
    nome_jogo = jogo.find('h3', {'class': 'c-subheading-4 x1GameName'}).text
    preco_jogo = jogo.get('data-listprice')
    url_jogo = jogo.find('a', {'class': 'gameDivLink'})['href']

    # Salvar jogos com valores reais e jogos sem preço em listas separadas.
    if preco_jogo != '100000000':
        informacoes_jogos.append({
            'Nome': nome_jogo,
            'Preço': preco_jogo,
            'URL': url_jogo
        })
    else:
        jogos_sem_preco.append({
            'Nome': nome_jogo,
            'Preço': preco_jogo,
            'URL': url_jogo
        })

print(f"Extraindo informações de {len(informacoes_jogos)} jogos com preço e {len(jogos_sem_preco)} jogos sem preço")

# Salvando dados armazenados nos arquivos json.
with open('produtos_xbox.json', 'w', encoding='utf-8') as f:
    json.dump(informacoes_jogos, f, ensure_ascii=False, indent=4)

with open('jogos_sem_preco.json', 'w', encoding='utf-8') as f:
    json.dump(jogos_sem_preco, f, ensure_ascii=False, indent=4)

print("Dados salvos em: produtos_xbox.json e jogos_sem_preco.json")