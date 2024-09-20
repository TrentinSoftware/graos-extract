# uvicorn fast_api:app --reload
from fastapi import FastAPI
import api_integration.utils_api as utils


app = FastAPI()


@app.get("/")
def hello_world():
    return "Olá mundo, minha API está no ar"


@app.get("/dates")
def dates_disponiveis():
    message = {"message": "Os parâmetros de data permitidas são: "}
    list_datas = utils.all_date_disp()
    return [message,list_datas]


@app.get("/regions")
def regions_disponiveis():
    message = {"message": "Os parâmetros de regions permitidas são: "}
    list_regions = utils.all_region_disp()
    return [message, list_regions]


@app.get(("/regions/{date}"))
def regions_disponiveis_in_date(date):
    response = utils.region_disp_in_specific_date(date=date)
    return response


@app.get("/all/{date}")
def all_grain_historic(date):
    response = utils.all_grain_historic(date)
    return response


@app.get("/{region}/{date}")
def region_grain_historic(date: str, region: str):
    response = utils.grain_historic_in_region(date=date, region=region)
    return response

