import pandas as pd
import os
import matplotlib.pyplot as plt

diretorio_historico = "historico/relatorios"
caminho_grafico = "dados/grafico_tendencia.png"

def gerar_grafico_tendencia():
    print("Gerando gráfico de tendência...")

    arquivos = [f for f in os.listdir(diretorio_historico) if f.endswith('.csv')]
    dfs = []

    for arquivo in arquivos:
        caminho_completo = os.path.join(diretorio_historico, arquivo)
        df = pd.read_csv(caminho_completo)
        timestamp_str = arquivo.split('_')[0] + '_' + arquivo.split('_')[1]
        df['timestamp'] = pd.to_datetime(timestamp_str, format='%Y-%m-%d_%H%M')
        dfs.append(df)

    df_historico = pd.concat(dfs, ignore_index=True)
    df_pivot = df_historico.pivot(index='timestamp', columns='nome', values='total_vendas').sort_index()

    plt.figure(figsize=(12, 6))
    for coluna in df_pivot.columns:
        plt.plot(df_pivot.index, df_pivot[coluna], label=coluna, marker='o')

    plt.title('Tendência de Vendas ao Longo do Tempo')
    plt.xlabel('Data e Hora')
    plt.ylabel('Total de Vendas')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(caminho_grafico)
    plt.close()

    print(f"Gráfico salvo em: {caminho_grafico}")

if __name__ == "__main__":
    gerar_grafico_tendencia()
