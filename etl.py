import pandas as pd
import os
import glob


def extrair_dados_e_consolidar(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, '*.json'))   
    df_lista = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_lista, ignore_index=True)
    return df_total 

def calcular_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df_total_vendas = df.copy()
    df_total_vendas["Total"] = df["Quantidade"] * df["Venda"]
    return df_total_vendas

def carregar_dados(df: pd.DataFrame, caminho: str, tipo_arq: list[str]) -> None:
    
    for tipo in tipo_arq:
        if tipo == "csv":
            df.to_csv(caminho + "." + tipo, index=False)
        elif tipo == "json":
            df.to_json(caminho + "." + tipo, orient="records")   
        elif tipo == "parquet":
            df.to_parquet(caminho + "." + tipo, index=False)

        print(f"Arquivo: `{caminho + "." + tipo}` salvo com sucesso!")      

    return None

def calcular_kpi_total_vendas_consolidado(pasta: str, formato_saida: list[str]) -> None:
    dta_frame = extrair_dados_e_consolidar(pasta)
    dta_frame_calculado = calcular_kpi_total_vendas(dta_frame)
    carregar_dados(dta_frame_calculado, os.path.join(pasta, "total_vendas"), formato_saida) 
    
    return None

    

