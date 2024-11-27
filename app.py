from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import json
import time
import tkinter as tk
from tkinter import font as tkfont

url = 'https://www.xbox.com/pt-BR/xbox-game-pass/games#pcgames'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@name='clearFilters']")))
time.sleep(10) # ajustar com o possível tempo de carregamento dos elementos principais

# Pressionando botão de carregar mais até não estar mais disponivel.
while True:
    try:
        carregar_mais = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(.,'CARREGAR MAIS')]")))
        carregar_mais.click()
        time.sleep(1)
    except TimeoutException:
        time.sleep(2)
        break  # Quando não houver mais o botão "Carregar mais" disponivel, sair do loop. Isso Significa que todos os jogos estão sendo exibidos.

# Obtendo html
html = driver.page_source
driver.quit()  # Fechando o navegador após obter o HTML

# Analisando o html com o bs4.
soup = BeautifulSoup(html, 'html.parser')
# Encontrando todos os jogos disponiveis.
jogos = soup.select('div.gameDivsWrapper section.m-product-placement-item.f-size-medium.context-game.gameDiv')

# Criando listas para armazenar resultados.
informacoes_jogos = []
jogos_sem_preco = []
total_price = 0

# Iterando sob os itens encontrados para extrair informações.
for jogo in jogos:
    nome_jogo = jogo.find('h3', {'class': 'c-subheading-4 x1GameName'}).text
    preco_jogo = jogo.get('data-listprice')
    url_jogo = jogo.find('a', {'class': 'gameDivLink'})['href']

    # Salvar jogos com valores reais e jogos sem preço em listas separadas.
    if preco_jogo != '100000000': # Valor genérico associado quando um jogo não possui preço
        informacoes_jogos.append({
            'Nome': nome_jogo,
            'Preço': preco_jogo,
            'URL': url_jogo
        })
        if preco_jogo.isdigit():
            total_price += float(preco_jogo)
    else:
        jogos_sem_preco.append({
            'Nome': nome_jogo,
            'Preço': preco_jogo,
            'URL': url_jogo
        })

# Salvando dados armazenados nos arquivos json.
with open('produtos_xbox.json', 'w', encoding='utf-8') as f:
    json.dump(informacoes_jogos, f, ensure_ascii=False, indent=4)
with open('jogos_sem_preco.json', 'w', encoding='utf-8') as f:
    json.dump(jogos_sem_preco, f, ensure_ascii=False, indent=4)

print(f"Foram encontrados {len(informacoes_jogos)} jogos com preço, totalizando R$ {total_price:,.2f}")
print(f"{len(jogos_sem_preco)} jogos não possuem preço")
print(f"Total de jogos: {len(jogos)}")

# Calculando tempo de gamepass ativo em referência ao valor total dos jogos
valor_gamepass = 36 # valor considerado gamepass PC
qtd_meses = float(total_price) / valor_gamepass
qtd_anos = qtd_meses / 12

# print(f"Quantidade de tempo de gamepass ativo considerando o valor de: R$ {total_price:,.2f}")
print(f"Quantidade de tempo de gamepass ativo considerando o valor de: R$ 36,00")
print(f"{qtd_meses:.2f} meses ou {qtd_anos:.1f} anos")

# ETAPA EXCLUÍVEL, APENAS PARA DEMONSTRAÇÃO EM JANELA ---------------------------------------

# Criando janela personalizada
root = tk.Tk()
root.title("Resultado da Busca")

# Configurando o tamanho e posição da janela
window_width = 550
window_height = 230
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Criando fonte personalizada
custom_font = tkfont.Font(size=12)

# Criando e posicionando os labels com as informações
tk.Label(root,
        text=f"Foram encontrados {len(informacoes_jogos)} jogos com preço,totalizando R$ {total_price:,.2f}.",
        font=custom_font,
        pady=5).pack()

tk.Label(root,
        text=f"{len(jogos_sem_preco)} jogos não possuem preço.",
        font=custom_font,
        pady=5).pack()

tk.Label(root,
        text=f"Total de jogos: {len(jogos)}",
        font=custom_font,
        pady=5).pack()

tk.Label(root,
        # text=f"Quantidade de tempo de gamepass ativo considerando o valor de: R$ {total_price:,.2f}",
        text=f"Quantidade de tempo de gamepass ativo considerando o valor de: R$ 36,00",
        font=custom_font,
        pady=5).pack()

tk.Label(root,
        text=f"{qtd_meses:.2f} meses ou {qtd_anos:.1f} anos",
        font=custom_font,
        pady=5).pack()

# Botão OK para fechar a janela
tk.Button(root,
        text="OK",
        command=root.destroy,
        font=custom_font,
        width=10,
        pady=5).pack(pady=10)

# Mantendo a janela aberta
root.mainloop()

print("Dados salvos em: produtos_xbox.json e jogos_sem_preco.json")