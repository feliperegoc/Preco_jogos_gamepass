# Xbox Game Pass - Valor total dos jogos

Este script Python realiza web scraping no site do Xbox Game Pass para calcular o valor total dos jogos disponíveis na plataforma, comparando com o valor mensal da assinatura. O objetivo é demonstrar, por curiosidade, quanto custaria comprar todos os jogos individualmente em comparação com o valor da assinatura mensal.

## 🎮 Funcionalidades

- Web scraping da página do Xbox Game Pass
- Coleta de preços de todos os jogos disponíveis
- Cálculo do valor total dos jogos
- Comparação com o valor mensal do Game Pass (R$ 36,00)
- Interface gráfica para exibição dos resultados
- Exportação dos dados para arquivos JSON

## 📋 Pré-requisitos

- Python 3.6 ou superior
- Google Chrome instalado

## 📦 Bibliotecas Necessárias

```bash
pip install selenium
pip install beautifulsoup4
pip install tkinter
```

## 💻 Uso

1. Execute o script:
```bash
python app.py
```

2. O script irá:
   - Abrir uma janela do Chrome automaticamente
   - Acessar a página do Xbox Game Pass
   - Coletar informações de todos os jogos
   - Exibir uma janela com os resultados
   - Gerar arquivos JSON com os dados coletados

## 📊 Dados Gerados

O script gera dois arquivos JSON:
- `produtos_xbox.json`: Lista de jogos com preços
- `jogos_sem_preco.json`: Lista de jogos sem preço disponível

## 📝 Informações Exibidas

- Quantidade total de jogos encontrados
- Número de jogos com preço disponível
- Valor total dos jogos
- Tempo equivalente de Game Pass (em meses e anos)
- Comparação com o valor mensal de R$ 36,00

## ⚠️ Observações Importantes

- É necessário ter uma conexão estável com a internet
- O tempo de execução pode variar dependendo da velocidade da conexão
- O script aguarda 10 segundos para carregamento inicial da página (ajustável se necessário)
- O Chrome será aberto e fechado automaticamente durante a execução
- Os resultados são salvos mesmo após fechar a janela de exibição

## 🔧 Possíveis Ajustes

No código, você pode modificar:
- `time.sleep(10)`: Tempo de espera para carregamento inicial
- `valor_gamepass = 36`: Valor da mensalidade do Game Pass
- Personalização da interface gráfica (tamanho, fonte, etc.)

## 🖥️ Interface Gráfica

A janela de resultados exibe:
- Total de jogos encontrados
- Jogos com e sem preço
- Valor total em Reais
- Equivalência em tempo de Game Pass
- Botão OK para fechar a janela
