"""
Modulo ETL - Engenharia de Dados (Extracao)
Projeto Integrador: Desenvolvimento Low Code em Ciencia de Dados - SENAC

Responsavel: Janaina Figueiredo da Silva
Funcao: Engenharia de Dados (Extracao)

Este script implementa a etapa de EXTRACAO (Extract) do processo ETL,
realizando a leitura da base de dados original em formato CSV e
disponibilizando os dados para as etapas subsequentes de transformacao e carga.
"""

import os
import pandas as pd


# ---------------------------------------------------------------------------
# Configuracoes de caminhos
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO_BASE_ORIGINAL = os.path.join(BASE_DIR, "data", "base_original.csv")
CAMINHO_BASE_TRATADA = os.path.join(BASE_DIR, "data", "base_tratada.csv")


# ---------------------------------------------------------------------------
# EXTRACT - Extracao dos dados
# ---------------------------------------------------------------------------
def extrair_dados(caminho_arquivo: str = CAMINHO_BASE_ORIGINAL) -> pd.DataFrame:
    """
    Realiza a extracao dos dados a partir do arquivo CSV original.

    Parametros
    ----------
    caminho_arquivo : str
        Caminho completo para o arquivo CSV de origem.

    Retorna
    -------
    pd.DataFrame
        DataFrame contendo os dados brutos extraidos.
    """
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(
            f"Arquivo nao encontrado: {caminho_arquivo}. "
            "Verifique se o dataset esta na pasta data/."
        )

    df = pd.read_csv(caminho_arquivo)
    return df


def exibir_relatorio_extracao(df: pd.DataFrame) -> None:
    """
    Exibe um relatorio resumido dos dados extraidos, incluindo
    dimensoes, tipos de dados, valores nulos e amostra inicial.

    Parametros
    ----------
    df : pd.DataFrame
        DataFrame com os dados extraidos.
    """
    print("=" * 60)
    print("  RELATORIO DE EXTRACAO - Engenharia de Dados")
    print("=" * 60)

    print(f"\nTotal de registros: {len(df)}")
    print(f"Total de colunas:   {len(df.columns)}")

    print("\n--- Colunas e tipos de dados ---")
    for coluna in df.columns:
        tipo = df[coluna].dtype
        nulos = df[coluna].isnull().sum()
        print(f"  {coluna:<25} | Tipo: {str(tipo):<10} | Nulos: {nulos}")

    print(f"\n--- Valores nulos totais: {df.isnull().sum().sum()} ---")

    print("\n--- Estatisticas descritivas (colunas numericas) ---")
    print(df.describe().to_string())

    print("\n--- Valores unicos em colunas categoricas ---")
    for coluna in df.select_dtypes(include=["object", "string"]).columns:
        valores_unicos = df[coluna].nunique()
        print(f"  {coluna}: {valores_unicos} valores unicos", end="")
        if valores_unicos <= 15:
            print(f" -> {sorted(df[coluna].dropna().unique().tolist())}")
        else:
            print()

    print("\n--- Primeiros 5 registros ---")
    print(df.head().to_string())

    print("\n" + "=" * 60)
    print("  Extracao concluida com sucesso!")
    print("=" * 60)


# ---------------------------------------------------------------------------
# Execucao principal
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Iniciando processo de extracao de dados...\n")

    df_extraido = extrair_dados()
    exibir_relatorio_extracao(df_extraido)
