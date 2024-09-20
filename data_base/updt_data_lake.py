import psycopg2
import pandas as pd
from sqlalchemy import create_engine


def dataframe_to_sql_inserts(df, table_name):
    insert_statements = []
    for index, row in df.iterrows():
        unidade: str = str(row['Unidade'])
        data_updt: str = str(row['Data'])
        preco_soja: str = str(row['Cotação Soja'])
        preco_milho: str = str('Cotação Milho')
        preco_trigo: str = str('Cotação Trigo')
        insert_statement = f"INSERT INTO {table_name} (unidade, data, cotacao_soja, cotacao_milho, cotacao_trigo) " \
                           f"VALUES ('{unidade}', '{data_updt}', {preco_soja}, {preco_milho}, {preco_trigo});"
        insert_statements.append(insert_statement)
    return "\n".join(insert_statements)


def get_data(path):
    return pd.read_csv(path, sep=",")


csv_file_path = 'C:/Temp/Relatorio-Graos/relatorio_graos_04-09-2024.csv'
sql_file_path = 'C:/Users/LAB-F3-PC13/Documents/bckp-grain-table.sql'
df = get_data(path=csv_file_path)

novos_inserts = dataframe_to_sql_inserts(df, 'cotacoes_graos')

with open(sql_file_path, 'r', encoding='utf-8') as file:
    sql_content = file.read()

sql_content += "\n" + novos_inserts

with open(sql_file_path, 'w', encoding='utf-8') as file:
    file.write(sql_content)

print("Dados do DataFrame inseridos no arquivo SQL com sucesso!")





