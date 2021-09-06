import re


def pro(string, pattern):
    result = re.search(pattern, string)
    if result is not None:
        return result.group()


# Categoria: select * from mvcatcad
# select cod_categ,descricao,nome_conselho_regi,sigla_conselho_reg from mvcatcad order by descricao
# COD_CATEG,DESCRICAO,NOME_CONSELHO_REGI,SIGLA_CONSELHO_REG
def atribuicaogrupo(atr):
    # Medicos: #################
    if pro(atr, "MEDICO") == "MEDICO":
        return "MDV MEDM POS VIS"
    ############################

    # Enfermagem: ##############
    elif pro(atr, "ENF") == "ENF":
        if pro(atr, "TECNICO DE ENFERMAGEM") == "TECNICO DE ENFERMAGEM" \
                or pro(atr, "AUXILIAR DE ENFERMAGEM") == "AUXILIAR DE ENFERMAGEM":
            return "MDV MEDAU POS ENF02"

        elif pro(atr, "ENFERMEIRO OBSTETRA") == "ENFERMEIRO OBSTETRA":
            return "MDV ENO POS ENF03"

        else:
            return "MDV MEDEN POS ENF03"
    ############################

    elif pro(atr, "ADMINISTRATIVO") == "ADMINISTRATIVO":
        return "MDV MEDA REC ADM POS APOIO URG APOIO"

    elif pro(atr, "LIDER DE HIGIEN") == "LIDER DE HIGIEN":
        return "EST PED POS PED"

    elif pro(atr, "LACTARISTA") == "LACTARISTA":
        return "MDV MEDA POS LACT"

    elif pro(atr, "RECEPCAO") == "RECEPCAO" \
            or pro(atr, "ATEND") == "ATEND":
        return "DIA AGEND MDV MEDA POS BAS REC AMD URG PS02 VIS PORTA"

    elif pro(atr, "ASSISTENTE SOCIAL") == "ASSISTENTE SOCIAL":
        return "MDV ASS POS APOIO"

    elif pro(atr, "AUXILIAR DE FARMACIA") == "AUXILIAR DE FARMACIA":
        return "EST FAR MDV AUXF POS APOIO"

    elif pro(atr, "FARMACEUTICO") == "FARMACEUTICO":
        return "EST FARL EST LIDF MDV FARMA POS CENSO"

    elif pro(atr, "FISIOTERAPEUTA") == "FISIOTERAPEUTA" \
            or pro(atr, "FISIO") == "FISIO":
        return "MDV MEDFI POS ENF03"

    elif pro(atr, "FONO") == "FONO":
        return "MDV MEFON POS APOIO"

    elif pro(atr, "INFORMATICA") == "INFORMATICA" \
            or pro(atr, "ANALISTA DE SUPORTE") == "ANALISTA DE SUPORTE" \
            or pro(atr, "ANALISTA DE SISTEMAS") == "ANALISTA DE SISTEMAS" \
            or pro(atr, "ANALISTA DE INFRA") == "ANALISTA DE INFRA":
        return "BLO INFO DIA INFO EST INFO FAT INFO MDV MEDI POS INFO REC INFO URG INFO VIS INFO"

    elif pro(atr, "LAB") == "LAB":
        return "MDV LAB POS LAB"

    elif pro(atr, "NUTRICIONISTA") == "NUTRICIONISTA":
        return "EST NUT MDV MEDNU POS APOIO"

    elif pro(atr, "PSIQ") == "PSIC":
        return "MDV MEDM POS APOIO"

    elif pro(atr, "PSIC") == "PSIC":
        return "MDV MEDPS POS PSI"

    elif pro(atr, "TERAPEUTA OCUPACIONAL") == "TERAPEUTA OCUPACIONAL":
        return "MDV METEO POS APOIO"

    elif pro(atr, "APRENDIZ") == "APRENDIZ" \
            or pro(atr, "ESTAGIARIO") == "ESTAGIARIO" \
            or pro(atr, "RAIO") == "RAIO" \
            or pro(atr, "RADIO") == "RADIO":
        return "MDV MEDA POS APOIO"
