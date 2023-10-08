import pandas as pd
import yfinance as yf

# Lista de símbolos das ações da Bovespa que você deseja incluir na carteira ingênua
acoes = ['ITUB4.SA', 'PETR4.SA', 'VALE3.SA', 'BBDC4.SA', 'ABEV3.SA']

# Defina o período de tempo desejado (por exemplo, de 2020-01-01 a 2021-12-31)
inicio = '2020-01-01'
fim = '2021-12-31'

# Obtenha os dados de preços das ações
precos_acoes = yf.download(acoes, start=inicio, end=fim)['Adj Close']

# Calcular os retornos diários das ações
retornos_diarios = precos_acoes.pct_change()

# Alocação igual de investimento para cada ativo
numero_ativos = len(acoes)
alocacao = 1.0 / numero_ativos

# Calcular o retorno diário da carteira ingênua
retornos_portfolio = retornos_diarios.mean(axis=1) * alocacao

# Calcular o retorno anual médio da carteira ingênua
retorno_anual_medio = retornos_portfolio.mean() * 252  # Supondo 252 dias úteis em um ano

print(f"Retorno anual médio da carteira ingênua: {retorno_anual_medio:.2%}")

#Este código aloca um investimento igual em todas as ações da lista acoes e calcula o retorno médio 
# da carteira ingênua com base nos dados fornecidos. Vamos ajustar a lista acoes e as datas
# de início e fim conforme necessário.
