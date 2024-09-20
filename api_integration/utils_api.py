import os
import pandas as pd

# Variáveis GLOBAIS
diretorio_folder = 'C:/Temp/Relatorio-Graos'
unidades_column = 'Unidade'
preco_soja_column = 'Cotação Soja'
preco_milho_column = 'Cotação Milho'
preco_trigo_column = 'Cotação Trigo'
date_column = 'Data'


def list_arquivos_in_folder(diretorio: str):
    files_in_folder = [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]
    return files_in_folder


def transform_df_in_dict(df):
    result = []
    for index, row in df.iterrows():
        record = {
            "unidade": str(row[unidades_column]),
            "data": str(row[date_column]),
            "cotacao_soja": str(row[preco_soja_column]).strip(),
            "cotacao_milho": str(row[preco_milho_column]).strip(),
            "cotacao_trigo": str(row[preco_trigo_column]).strip()
        }
        result.append(record)
    return result


def all_date_disp():
    arquivos = list_arquivos_in_folder(diretorio=diretorio_folder)
    arquivos = [file_name.replace('relatorio_graos_', '') for file_name in arquivos]
    datas_disp = [file_name.replace('.csv', '') for file_name in arquivos]
    return datas_disp


def all_region_disp():
    arquivos = list_arquivos_in_folder(diretorio=diretorio_folder)
    arquivos = [os.path.join(diretorio_folder, file_name) for file_name in arquivos]

    list_unidades = []
    for file in arquivos:
        df = pd.read_csv(file, sep=";")
        list_unidades.extend(df[unidades_column].tolist())

    list_unidades = list(set(list_unidades))

    response = {"regions": list_unidades}
    return response


def region_disp_in_specific_date(date):
    print(f"Filtrando a data {date}, que deve sempre ser no padrão dd-MM-yyyy")
    list_datas = all_date_disp()
    has_data: bool = date in list_datas

    if has_data:
        csv_file_path = diretorio_folder + f'/relatorio_graos_{date}.csv'
        df = pd.read_csv(csv_file_path, sep=";")
        list_unidades = df[unidades_column].tolist()
        list_unidades = list(set(list_unidades))
        response = {"regions": list_unidades}
    else:
        response = {"message": "A data que você passou não existe", "status_code": 400}

    return response


def all_grain_historic(date: str):
    print(f"Filtrando a data {date}, que deve sempre ser no padrão dd-MM-yyyy")
    list_datas = all_date_disp()
    has_data: bool = date in list_datas

    if has_data:
        csv_file_path = diretorio_folder + f'/relatorio_graos_{date}.csv'
        df = pd.read_csv(csv_file_path, sep=";")
        response = transform_df_in_dict(df=df)
    else:
        response = {"message": "A data que você passou não existe", "status_code": 400}

    return response

def grain_historic_in_region(date: str, region: str):
    print(f"Filtrando a data {date}, que deve sempre ser no padrão dd-MM-yyyy")
    list_datas = all_date_disp()
    has_data: bool = date in list_datas

    if has_data:
        csv_file_path = diretorio_folder + f'/relatorio_graos_{date}.csv'
        df = pd.read_csv(csv_file_path, sep=";")
        df = df[df[unidades_column] == region]
        response = transform_df_in_dict(df=df)
    else:
        response = {"message": "A data que você passou não existe", "status_code": 400}

    return response

