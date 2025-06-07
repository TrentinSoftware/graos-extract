import csv
from selenium.webdriver.common.by import By
from src.web_utils import get_driver_edge_private


def process():
    driver = get_driver_edge_private()

    try:
        driver.get("https://www.agrolink.com.br/cotacoes/graos/")
        rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr:not(.tr-border)")
        data = []

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            product = cols[0].text.split('\n')[0].strip()
            location = cols[1].text if len(cols) > 4 else cols[0].find_element(By.TAG_NAME, "span").text

            #price_div = cols[2].find_element(By.TAG_NAME, "div")
            #price_style = price_div.get_attribute("style")
            price = "Preço não extraível diretamente"
            update_date = cols[3].text if len(cols) > 4 else cols[2].text

            data.append({
                "Produto": product,
                "Localização": location,
                "Preço": price,
                "Data de Atualização": update_date
            })

        write_csv_in = 'agrolink.csv'
        with open(write_csv_in, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Produto', 'Localização', 'Preço', 'Data de Atualização']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data)

        print(f"Dados extraídos e salvos em {write_csv_in}")
        return write_csv_in

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None
    finally:
        driver.quit()
