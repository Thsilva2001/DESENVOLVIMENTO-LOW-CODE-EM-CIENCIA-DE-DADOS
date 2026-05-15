import pandas as pd



# Funcao para classificacao por faixa etaria

def faixa_etaria(idade):

    if idade < 18:
        return "Menor de idade"

    elif idade < 30:
        return "Jovem"

    elif idade < 60:
        return "Adulto"

    else:
        return "Senior"


# TRANSFORM - Transformacao dos dados

def transformar_dados(df: pd.DataFrame) -> pd.DataFrame:

    print("=" * 60)
    print("INICIANDO TRANSFORMACAO DOS DADOS")
    print("=" * 60)

    # Verificacao de duplicatas

    duplicados = df.duplicated().sum()

    print(f"\nDuplicatas encontradas: {duplicados}")

  
    # Criacao da coluna faixa etaria

    df["Faixa_Etaria"] = df["Age"].apply(faixa_etaria)

    print("\nColuna 'Faixa_Etaria' criada com sucesso.")

    # Tabelas agregadas para analise
   
    df_pais = df["Country"].value_counts().reset_index()
    df_pais.columns = ["Country", "Quantidade"]

    df_faixa = (
        df.groupby("Faixa_Etaria")
        .size()
        .reset_index(name="Quantidade")
    )

    df_genero = (
        df["Favorite_Genre"]
        .value_counts()
        .reset_index()
    )

    df_genero.columns = [
        "Favorite_Genre",
        "Quantidade"
    ]

    
    # Cruzamento de variaveis
    
    df_faixa_genero = (
        df.groupby(
            ["Faixa_Etaria", "Favorite_Genre"]
        )
        .size()
        .reset_index(name="Quantidade")
    )

    df_pais_faixa = (
        df.groupby(
            ["Country", "Faixa_Etaria"]
        )
        .size()
        .reset_index(name="Quantidade")
    )

    
    # Resumo geral
    
    resumo = {
        "total_registros": df.shape[0],
        "total_paises": df["Country"].nunique(),
        "faixa_mais_comum": df["Faixa_Etaria"].mode()[0]
    }

    print("\n--- Resumo Geral ---")

    for chave, valor in resumo.items():
        print(f"{chave}: {valor}")

    print("\n--- Faixas Etarias ---")
    print(df["Faixa_Etaria"].value_counts())

    print("\n" + "=" * 60)
    print("TRANSFORMACAO FINALIZADA COM SUCESSO")
    print("=" * 60)

    return df
