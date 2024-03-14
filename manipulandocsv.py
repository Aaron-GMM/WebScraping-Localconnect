import pandas as pd
import os


def lendo_arquivo():
    arquivos_csv = [
        "localconnectusers.csv",
        "user.csv",
        "planilha.csv"
    ]
    diretorio = "../../pythonProjec/webscrapinglc/arquivos"
    arquivos_existentes = [os.path.join(diretorio, arquivo) for arquivo in arquivos_csv if
                           os.path.exists(os.path.join(diretorio, arquivo))]
    if arquivos_existentes:
        print("Arquivos encontrados:", arquivos_existentes)
        dfs = []
        for arquivo in arquivos_existentes:
            dfs.append(pd.read_csv(arquivo))
        return dfs
    else:
        print("Nenhum arquivo encontrado.")
        return None

def listando_primeira_coluna(lista_dataframes):
    primeiras_colunas = []
    for df in lista_dataframes:
        primeira_coluna = df.iloc[:, 0]
        primeiras_colunas.append(primeira_coluna)
    return primeiras_colunas

if __name__ == '__main__':
    data_frames = lendo_arquivo()
    if data_frames:
        primeiras_colunas = listando_primeira_coluna(data_frames)
        for pc in primeiras_colunas:
            print(pc)
    else:
        print("Não há dados para mostrar.")

