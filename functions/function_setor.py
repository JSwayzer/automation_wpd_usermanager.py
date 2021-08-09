import re


def pro(string, pattern):
    result = re.search(pattern, string)
    if result is not None:
        return result.group()


# Categoria: select * from mvcatcad
# select cod_categ,descricao,nome_conselho_regi,sigla_conselho_reg from mvcatcad order by descricao
# COD_CATEG,DESCRICAO,NOME_CONSELHO_REGI,SIGLA_CONSELHO_REG
def setor(set):
    # Medicos: #################
    if pro(set, "ALMOXARIFADO") == "ALMOXARIFADO":
        return "0001"
    ############################

    # Enfermagem: ##############
    elif pro(set, "FARMACIA") == "FARMACIA":
        if pro(set, "FARMACIA 3") == "FARMACIA 3":
            return "0301"

        elif pro(set, "FARMACIA ANEXA 1") == "FARMACIA ANEXA 1":
            return "0324"

        elif pro(set, "FARMACIA ANEXA TERREO") == "FARMACIA ANEXA TERREO":
            return "0323"

        elif pro(set, "FARMACIA CENTRAL") == "FARMACIA CENTRAL":
            return "0014"

        elif pro(set, "FARMACIA CENTRO CIRURGICO") == "FARMACIA CENTRO CIRURGICO":
            return "0027"

        elif pro(set, "FARMACIA DOSE UNITARIA") == "FARMACIA DOSE UNITARIA":
            return "0319"

        elif pro(set, "FARMACIA MEDICACAO ADULTO") == "FARMACIA MEDICACAO ADULTO":
            return "0309"

        elif pro(set, "FARMACIA PRONTO SOCORRO") == "FARMACIA PRONTO SOCORRO":
            return "0309"

        else:
            return "0014"
    ############################

    elif pro(set, "ADMINISTRATIVO") == "ADMINISTRATIVO":
        return "MDV MEDA REC ADM POS APOIO URG APOIO"
