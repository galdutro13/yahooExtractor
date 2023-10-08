import yfinance as yf
from datetime import datetime, timedelta
#Importamos a biblioteca yfinance, que permite acessar dados financeiros usando a API do Yahoo Finanças.
#Versão inicial terão melhorias no futuro de acordo com a nossa necessidade

def extrair_rendimento_acao(acao, anos):
    try:
        # Cria um objeto para a ação desejada
        acao_obj = yf.Ticker(acao)

        # Calcula a data de início como a data atual menos 'anos' anos
        data_inicio = datetime.now() - timedelta(days=365 * anos)

        # Obtém o histórico de preços no período especificado
        historico = acao_obj.history(period=f"{anos}y")

        if historico.empty:
            return "Nenhum dado disponível para o período especificado."

        # Calcula o rendimento
        rendimento = (historico['Close'].iloc[-1] - historico['Open'].iloc[0]) / historico['Open'].iloc[0] * 100

        return rendimento

    except yf.TickerError as te:
        return f"Erro ao buscar informações da ação {acao}: {te}"
    except Exception as e:
        return f"Erro desconhecido: {str(e)}"

if __name__ == "__main__":
    acao = input("Digite o símbolo da ação (por exemplo, AAPL para a Apple): ")
    anos = int(input("Digite o número de anos para análise: "))

    rendimento = extrair_rendimento_acao(acao, anos)

    if isinstance(rendimento, float):
        print(f"Rendimento da ação {acao} nos últimos {anos} anos: {rendimento:.2f}%")
    else:
        print(f"Erro ao obter o rendimento da ação {acao}: {rendimento}")
