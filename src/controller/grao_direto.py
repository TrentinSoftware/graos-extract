from src.service import grao_direto

def process():
    output_file = 'grao_direto.csv'
    try:
        df = grao_direto.extract_graodireto_offers()

        if not df.empty:
            df = df.sort_values(['Produto', 'Preco_num'])

            df.to_csv(output_file, index=False, encoding='utf-8-sig', float_format='%.2f')
            print(f"Dados salvos com sucesso em {output_file}")
        else:
            print("Nenhuma oferta foi encontrada")

        return output_file

    except Exception as e:
        print(f"Erro durante a transformação dos dados: {str(e)}")
        return None
