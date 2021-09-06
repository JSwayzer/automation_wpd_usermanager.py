import re


def pro(string, pattern):
    result = re.search(pattern, string)
    if result is not None:
        return result.group()


# Setor: select cod_set, descricao from fasetcad where descricao not like '%BLOQUEADO%' order by cod_set
def setor(stor):
    # Medicos: #################
    if pro(stor, "ALMOXARIFADO") == "ALMOXARIFADO":
        return "0001"
    ############################

    # Enfermagem: ##############
    elif pro(stor, "FARMACIA") == "FARMACIA":
        if pro(stor, "FARMACIA 3") == "FARMACIA 3":
            return "0301"

        elif pro(stor, "FARMACIA ANEXA 1") == "FARMACIA ANEXA 1":
            return "0324"

        elif pro(stor, "FARMACIA ANEXA TERREO") == "FARMACIA ANEXA TERREO":
            return "0323"

        elif pro(stor, "FARMACIA CENTRAL") == "FARMACIA CENTRAL":
            return "0014"

        elif pro(stor, "FARMACIA CENTRO CIRURGICO") == "FARMACIA CENTRO CIRURGICO":
            return "0027"

        elif pro(stor, "FARMACIA DOSE UNITARIA") == "FARMACIA DOSE UNITARIA":
            return "0319"

        elif pro(stor, "FARMACIA MEDICACAO ADULTO") == "FARMACIA MEDICACAO ADULTO":
            return "0309"

        elif pro(stor, "FARMACIA PRONTO SOCORRO") == "FARMACIA PRONTO SOCORRO":
            return "0309"

        else:
            return "0014"
    ############################

    elif pro(stor, "ADMINISTRATIVO") == "ADMINISTRATIVO":
        return "MDV MEDA REC ADM POS APOIO URG APOIO"

