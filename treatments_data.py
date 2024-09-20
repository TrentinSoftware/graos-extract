import pandas as pd


def treat_graos_data(df_graos_raw):
    df_graos_treated = pd.DataFrame(columns=['Unidade', 'Data', 'Cotação Soja', 'Cotação Milho', 'Cotação Trigo'])

    graos_dict = {}

    for index, row in df_graos_raw.iterrows():
        unidade_atual = str(row['Unidade'])
        produto_atual = str(row['Produto'])
        data_atual = str(row['Data'])
        cotacao_atual = str(row['Fechamento'])

        if unidade_atual not in graos_dict:
            graos_dict[unidade_atual] = {
                'Unidade': unidade_atual,
                'Data': data_atual,
                'Cotação Soja': None,
                'Cotação Milho': None,
                'Cotação Trigo': None
            }

        if produto_atual == 'Soja':
            graos_dict[unidade_atual]['Cotação Soja'] = cotacao_atual
        elif produto_atual == 'Milho':
            graos_dict[unidade_atual]['Cotação Milho'] = cotacao_atual
        elif produto_atual == 'Trigo':
            graos_dict[unidade_atual]['Cotação Trigo'] = cotacao_atual

    df_graos_treated = pd.DataFrame(graos_dict.values())
    return df_graos_treated

def get_data_rel(df_graos):
    for index, row in df_graos.iterrows():
        str_data_rel = str(row['Data']).replace("/", "-")
        str_data_rel = str_data_rel.replace("\\", "-")
        return str_data_rel
        break