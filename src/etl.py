from extract import extrair_dados, exibir_relatorio_extracao
from transform import transformar_dados
from load import salvar_dados



# PIPELINE ETL

def executar_pipeline():

    print("=" * 60)
    print("INICIANDO PIPELINE ETL")
    print("=" * 60)

    
    # EXTRACT
   
    print("\n[1/3] ETAPA EXTRACT")

    df = extrair_dados()

    exibir_relatorio_extracao(df)

    
    # TRANSFORM
    
    print("\n[2/3] ETAPA TRANSFORM")

    df = transformar_dados(df)

    
    # LOAD
   
    print("\n[3/3] ETAPA LOAD")

    salvar_dados(df)

    print("\n" + "=" * 60)
    print("PIPELINE ETL FINALIZADO COM SUCESSO")
    print("=" * 60)



# EXECUCAO PRINCIPAL

if __name__ == "__main__":

    executar_pipeline()
