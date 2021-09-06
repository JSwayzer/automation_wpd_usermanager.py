import re


def pro(string, pattern):
    result = re.search(pattern, string)
    if result is not None:
        return result.group()


# Categoria: select * from mvcatcad
# select cod_categ,descricao,nome_conselho_regi,sigla_conselho_reg from mvcatcad order by descricao
# COD_CATEG,DESCRICAO,NOME_CONSELHO_REGI,SIGLA_CONSELHO_REG
def categoria(cat):
    # Medicos: #################
    if pro(cat, "MEDICO") == "MEDICO":
        if pro(cat, "MEDICO INTERNO") == "MEDICO INTERNO":
            return "MEDR"

        elif pro(cat, "MEDICO PEDIATRA") == "MEDICO PEDIATRA":
            return "MEDP"

        elif pro(cat, "MEDICO PS") == "MEDICO PS":
            return "MED1"

        else:
            return "MED"
    ############################

    # Enfermagem: ##############
    elif pro(cat, "ENF") == "ENF":
        if pro(cat, "TECNICO DE ENFERMAGEM") == "TECNICO DE ENFERMAGEM" or \
                pro(cat, "AUXILIAR DE ENFERMAGEM") == "AUXILIAR DE ENFERMAGEM":
            return "TENF"

        elif pro(cat, "ENFERMEIRO OBSTETRA") == "ENFERMEIRO OBSTETRA":
            return "ENO"

        else:
            return "ENF"
    ############################

    elif pro(cat, "ADMINISTRATIVO") == "ADMINISTRATIVO" \
            or pro(cat, "AUXILIAR DE FARMACIA") == "AUXILIAR DE FARMACIA" \
            or pro(cat, "LACTARISTA") == "LACTARISTA" \
            or pro(cat, "APRENDIZ") == "APRENDIZ" \
            or pro(cat, "ESTAGIARIO") == "ESTAGIARIO" \
            or pro(cat, "SEGURANCA") == "SEGURANCA" \
            or pro(cat, "LIDER DE HIGIEN") == "LIDER DE HIGIEN" \
            or pro(cat, "LIDER DE ATEND") == "LIDER DE ATEND" \
            or pro(cat, "TECNICO DE RADIOLOGIA") == "TECNICO DE RADIOLOGIA" \
            or pro(cat, "TECNICO DE RAIO") == "TECNICO DE RAIO":
        return "ADM"

    elif pro(cat, "ASSISTENTE SOCIAL") == "ASSISTENTE SOCIAL":
        return "ASS"

    elif pro(cat, "AUXILIAR DE FARMACIA") == "AUXILIAR DE FARMACIA":
        return "AUXF"

    elif pro(cat, "FARMACEUTICO") == "FARMACEUTICO":
        return "CRF"

    elif pro(cat, "FISIOTERAPEUTA") == "FISIOTERAPEUTA" \
            or pro(cat, "FISIO") == "FISIO":
        return "FIS"

    elif pro(cat, "FONOAUDIO") == "FONOAUDIO":
        return "FON"

    elif pro(cat, "INFORMATICA") == "INFORMATICA"\
            or pro(cat, "ANALISTA DE SUPORTE") == "ANALISTA DE SUPORTE" \
            or pro(cat, "ANALISTA DE SISTEMAS") == "ANALISTA DE SISTEMAS" \
            or pro(cat, "ANALISTA DE INFRA") == "ANALISTA DE INFRA":
        return "INF"

    elif pro(cat, "LABORATORIO") == "LABORATORIO":
        return "LAB"

    elif pro(cat, "NUTRICIONISTA") == "NUTRICIONISTA":
        return "NUT"

    elif pro(cat, "PSICOLOGO") == "PSICOLOGO":
        return "PSI"

    elif pro(cat, "SCIH") == "SCIH":
        return "SCIH"

    elif pro(cat, "TERAPEUTA OCUPACIONAL") == "TERAPEUTA OCUPACIONAL":
        return "TEO"
