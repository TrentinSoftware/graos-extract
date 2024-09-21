from web_automation import *
from treatments_data import *
import os


def main_fn():
    web_automation = WebCaptureGraos()
    df_graos = web_automation.capture_value_graos()
    df_graos = treat_graos_data(df_graos_raw=df_graos)
    str_data_geracao_rel = get_data_rel(df_graos=df_graos)

    path_folder = "C:/Temp/Relatorio-Graos"
    if not os.path.exists("C:\\Temp"):
        os.makedirs("C:\\Temp")

    if not os.path.exists(path_folder):
        os.makedirs(path_folder)

    csv_path = os.path.join(path_folder, "relatorio_graos_"+str_data_geracao_rel+".csv")
    df_graos.to_csv(csv_path, sep=';', index=False)
    print(f"Arquivo CSV salvo em: {csv_path}")


if __name__ == "__main__":
    main_fn()