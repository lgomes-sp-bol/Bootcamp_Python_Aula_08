from etl import extrair_dados
    
if __name__ == "__main__":
    pasta = "Data"
    df_consolidado = extrair_dados(pasta)
    print(df_consolidado)