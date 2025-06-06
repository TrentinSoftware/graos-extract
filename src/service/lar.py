import time
from builtins import str
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from src.web_utils import get_driver_edge_private


class WebCaptureGraos:
    def __init__(self):
        self.url_system = "https://www.lar.ind.br/lar-agro/agricola/"
        self.driver = None

    def capture_value_graos(self):
        self.start_browser()
        df_graos = self.select_option_by_text()
        return df_graos

    def kill_edge_instances(self):
        os.system("taskkill /f /im msedge.exe")

    def close_driver(self):
        self.driver.close()

    def start_browser(self):
        self.driver = get_driver_edge_private()
        self.driver.get(self.url_system)
        self.driver.maximize_window()
        return self.driver

    def extract_table_to_dataframe(self):
        div_element = self.driver.find_element(By.XPATH, "//div[@class='laragro-cotacoes__table']")
        table = div_element.find_element(By.TAG_NAME, "table")
        headers = [header.text.strip() for header in table.find_elements(By.XPATH, ".//thead/tr/td")]

        rows = table.find_elements(By.XPATH, ".//tbody/tr")
        data = []

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            data.append([col.text.strip() for col in cols])

        df = pd.DataFrame(data, columns=headers)
        return df

    def select_option_by_text(self):
        select_id = "cotacao"
        bool_has_list_option = False
        try:
            select_element = Select(self.driver.find_element(By.ID, select_id))

            options_list = [option.text for option in select_element.options]

            print("Opções disponíveis no <select>:")
            print(options_list)
            bool_has_list_option = True
        except Exception as exceptt:
            print(f"Erro ao selecionar a opção: {str(exceptt)}")

        if bool_has_list_option:
            df_graos = pd.DataFrame(columns=['Unidade', 'Produto', 'Data', 'Cotação', 'Fechamento'])
            for option_text in options_list:
                try:
                    select_element = Select(self.driver.find_element(By.ID, select_id))

                    select_element.select_by_visible_text(option_text)
                    print(f"Opção '{option_text}' selecionada com sucesso!")

                    xpath_sbmt_enviar = "//button[@type='submit' and text()='Enviar']"
                    loaded_operacoes_medianeira = False

                    try:
                        WebDriverWait(self.driver, 10).until(
                            ec.presence_of_element_located((By.XPATH, xpath_sbmt_enviar)))
                        loaded_operacoes_medianeira = True
                    except Exception as exceptt:
                        print(f"Erro ao localizar o botão 'Enviar': {exceptt}")

                    if loaded_operacoes_medianeira:
                        sbmt_enviar = self.driver.find_element(By.XPATH, xpath_sbmt_enviar)
                        retry_count = 0

                        while retry_count <= 3:
                            try:
                                time.sleep(1)
                                sbmt_enviar.click()
                                df_graos_atual = self.extract_table_to_dataframe()
                                df_graos = pd.concat([df_graos, df_graos_atual], ignore_index=True)
                                retry_count = 100
                            except Exception as exceptt:
                                print(f"Erro ao clicar no botão 'Enviar': {exceptt}")
                                retry_count += 1
                except Exception as exceptt:
                    print(f"Erro na iteração com a opção '{option_text}': {exceptt}")

            return df_graos