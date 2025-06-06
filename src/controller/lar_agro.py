from src.service.lar import *
from src.model.treatments_data import *
import os


def process():
    try:
        web_automation = WebCaptureGraos()
        df_graos = web_automation.capture_value_graos()
        df_graos = treat_graos_data(df_graos_raw=df_graos)
        csv_path = 'lar_agro.csv'

        df_graos.to_csv(csv_path, sep=';', index=False)
        print(f"Arquivo CSV salvo em: {csv_path}")
        return csv_path
    except Exception as exc:
        print(f"Ocorreu um erro ao tentar buscar dados da Lar Agro: \n{exc}")
        return None