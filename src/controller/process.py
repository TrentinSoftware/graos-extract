from src.controller import lar_agro
from src.controller import agrolink
from src.controller import grao_direto


def process():
    return_lar_agro = lar_agro.process()
    if return_lar_agro:
        print("OCORREU TUDO CERTO PARA EXTRAIR E TRANSFORMAR OS DADOS DA LAR AGRO")
    else:
        print("OCORREU UM ERRO PARA EXTRAIR E TRANSFORMAR OS DADOS DA LAR AGRO")

    return_agrolink = agrolink.process()
    if return_agrolink:
        print("OCORREU TUDO CERTO PARA EXTRAIR E TRANSFORMAR OS DADOS DA AGROLINK")
    else:
        print("OCORREU UM ERRO PARA EXTRAIR E TRANSFORMAR OS DADOS DA AGROLINK")

    return_grao_direto = grao_direto.process()
    if return_grao_direto:
        print("OCORREU TUDO CERTO PARA EXTRAIR E TRANSFORMAR OS DADOS DA GRÃO DIRETO")
    else:
        print("OCORREU UM ERRO PARA EXTRAIR E TRANSFORMAR OS DADOS DA GRÃO DIRETO")
