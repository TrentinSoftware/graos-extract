import requests
import pandas as pd

def request_region_grain(unidade: str, date: str):
    unidade = unidade.replace(" ","%20")
    date = date.replace("/", "-")
    url = "http://127.0.0.1:8000/" + unidade + "/" + date
    headers = {
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        df = pd.DataFrame(data)

        print(df)
    else:
        print(f"Erro: {response.status_code}")

    return df

df = request_region_grain(unidade="OPERACIONAL MEDIANEIRA - PR",date="11/09/2024")
pass
