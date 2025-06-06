import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.web_utils import get_driver_edge_private


def clean_price(price_str):
    """Converte strings de preço como 'R$ 123,75' para 123.75 (float)"""
    try:
        cleaned = price_str.replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.').strip()
        return float(cleaned)
    except:
        return None


def extract_graodireto_offers():

    driver = get_driver_edge_private()

    try:
        driver.get("https://www.graodireto.com.br/")

        wait = WebDriverWait(driver, 15)
        section_locator = (By.CSS_SELECTOR, "section[id^='headlessui-tabs-panel-']")
        wait.until(EC.visibility_of_element_located(section_locator))

        html_content = driver.page_source

        soup = BeautifulSoup(html_content, 'html.parser')

        all_offers = []

        product_map = {
            'Soja': 'soy',
            'Milho': 'corn',
            'Sorgo': 'sorghum'
        }

        for product_name, product_class in product_map.items():
            product_section = soup.find('section', class_='space-y-6')
            if not product_section:
                continue

            offer_cards = product_section.find_all('button', class_=f'hover:border-products-{product_class}')

            for card in offer_cards:
                try:
                    price_div = card.find('div', class_='text-3xl')
                    price_str = price_div.get_text(strip=True) if price_div else 'N/A'

                    price_num = clean_price(price_str)

                    location_p = card.find('p', class_='text-base')
                    location = location_p.get_text(strip=True) if location_p else 'N/A'
                    description_h3 = card.find('h3', class_='text-web-body-2')
                    description = description_h3.get_text(strip=True) if description_h3 else 'N/A'

                    all_offers.append({
                        'Produto': product_name,
                        'Preco_str': price_str,
                        'Preco_num': price_num,
                        'Localidade': location,
                        'Descricao': description,
                        'Data_Coleta': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
                except Exception as e:
                    print(f"Erro ao processar card de {product_name}: {str(e)}")

        return pd.DataFrame(all_offers)

    except Exception as e:
        print(f"Erro durante a extração: {str(e)}")
        return pd.DataFrame()

    finally:
        driver.quit()
