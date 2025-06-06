from selenium import webdriver
from selenium.webdriver.edge.options import Options


def get_driver_edge_private():
    edge_options = Options()
    edge_options.add_argument("--inprivate")  # Abre o navegador no modo InPrivate (anônimo)
    return webdriver.Edge(options=edge_options)