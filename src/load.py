import os
import pandas as pd



# Configuracao dos caminhos

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

CAMINHO_SAIDA = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "base_tratada.csv"
)



# LOAD - Limpeza e exportacao dos dados

def salvar_dados(df: pd.DataFrame):

    print("=" * 60)
    print("INICIANDO ETAPA LOAD")
    print("=" * 60)

    
    # Remove linhas duplicadas
   
    initial_rows = len(df)

    df.drop_duplicates(inplace=True)

    print(
        f"\nLinhas duplicadas removidas: "
        f"{initial_rows - len(df)}"
    )

    print(
        f"Total de linhas apos remover duplicatas: "
        f"{len(df)}"
    )

    
    # Remove espacos em branco das colunas de texto
   
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()

    print("\nEspacos em branco removidos das colunas.")

   
    # Padronizacao da coluna Name
    
    df['Name'] = df['Name'].str.title()

    print("\nColuna 'Name' padronizada.")

    
    # Conversao da coluna Last_Login
    
    df['Last_Login'] = pd.to_datetime(df['Last_Login'])

    print(
        "\nTipo de dado da coluna "
        "'Last_Login' convertido para datetime."
    )

    
    # Padronizacao dos nomes das colunas
    
    df.rename(columns={
        'User_ID': 'user_id',
        'Name': 'name',
        'Age': 'age',
        'Country': 'country',
        'Subscription_Type': 'subscription_type',
        'Watch_Time_Hours': 'watch_time_hours',
        'Favorite_Genre': 'favorite_genre',
        'Last_Login': 'last_login',
        'Faixa_Etaria': 'faixa_etaria'
    }, inplace=True)

    print("\nColunas renomeadas com sucesso.")

   
    # Criacao da pasta de saida
    
    os.makedirs(
        os.path.dirname(CAMINHO_SAIDA),
        exist_ok=True
    )

    
    # Exportacao da base tratada
    
    df.to_csv(
        CAMINHO_SAIDA,
        index=False
    )

    print("\nBase tratada salva com sucesso!")

    print(f"\nArquivo salvo em:\n{CAMINHO_SAIDA}")

    print("\n" + "=" * 60)
    print("LOAD FINALIZADO COM SUCESSO")
    print("=" * 60)
