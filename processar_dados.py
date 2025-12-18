import pandas as pd

def pipeline_vendas():
    print("--- Iniciando Pipeline de Dados ---")

    # 1. Extração (Extract)
    df = pd.read_csv('dados_vendas.csv')
    print(f"Dados brutos carregados: {len(df)} linhas.")

    # 2. Transformação (Transform) - Limpeza de dados (Data Foundation)
    # Removendo linhas com valores vazios (NaN)
    df_limpo = df.dropna().copy()

    # Convertendo tipos (garantindo que preço e quantidade sejam números)
    df_limpo['preco'] = pd.to_numeric(df_limpo['preco'])
    df_limpo['quantidade'] = pd.to_numeric(df_limpo['quantidade'])

    # Criando métrica de negócio (Impacto no DRE)
    df_limpo['faturamento_total'] = df_limpo['preco'] * df_limpo['quantidade']

    print(f"Limpeza concluída. {len(df_limpo)} linhas válidas restantes.")

    # 3. Carga (Load)
    df_limpo.to_csv('vendas_final.csv', index=False)
    print("Arquivo 'vendas_final.csv' gerado com sucesso!")

if __name__ == "__main__":
    pipeline_vendas()