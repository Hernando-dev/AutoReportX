import pandas as pd
import sqlite3
import time
import os

# Configurações
caminho_csv = "dados/dados_brutos.csv"
caminho_saida = "dados/dados_atualizados.csv"
caminho_historico = "historico/relatorios"

def atualizar_dados():
    print("Iniciando atualização dos dados...")

    if not os.path.exists(caminho_historico):
        os.makedirs(caminho_historico)

    if not os.path.exists(caminho_csv):
        df = pd.DataFrame({
            'id': [1, 2, 3],
            'nome': ['João', 'Maria', 'Pedro'],
            'venda': [100, 250, 150]
        })
        df.to_csv(caminho_csv, index=False)

    df = pd.read_csv(caminho_csv)
    df['data_atualizacao'] = time.strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect(':memory:')
    df.to_sql('vendas', conn, index=False)
    query_sql = """
        SELECT nome, SUM(venda) AS total_vendas
        FROM vendas
        GROUP BY nome
        ORDER BY total_vendas DESC
    """
    df_resultado = pd.read_sql_query(query_sql, conn)

    df_resultado.to_csv(caminho_saida, index=False)

    timestamp = time.strftime('%Y-%m-%d_%H%M')
    caminho_historico_arquivo = os.path.join(caminho_historico, f"{timestamp}_dados.csv")
    df_resultado.to_csv(caminho_historico_arquivo, index=False)

    print(f"Dados salvos em {caminho_saida}")
    print(f"Cópia salva no histórico: {caminho_historico_arquivo}")

if __name__ == "__main__":
    atualizar_dados()
