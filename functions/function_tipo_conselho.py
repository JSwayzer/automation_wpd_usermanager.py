import re


def pro(string, pattern):
    result = re.search(pattern, string)
    if result is not None:
        return result.group()


'''COD_TP_CONSELHO	DESCRICAO	DESCRICAO_ABV	COD_CONSPROF_TISS
001	CONSELHO REG DE MEDICINA	CRM	CRM
002	CONSELHO REG DE ENFERMAGEM	COREN	COREN
003	CONSELHO REG DE NUTRICAO	CRN	CRN
004	CONSELHO REG DE ODONTOLOGIA	CRO	CRO
005	CONSELHO REG FISIO/TERA OCUP.	CREFITO	CREFITO
006	CONSELHO REG DE FARMACIA	CRF	CRF
007	CONSELHO REG DE FONOAUDIOLOGIA	CRFA	OUT
008	CONSELHO REG DE PSICOLOGIA	CRP	CRP
012	INFORMATICA	INF	OUT
013	CONSELHO REG DE BIOMEDICINA	CRBM	OUT
014	CONSELHO REG. SERV. SOCIAL SP	CRESS	CRAS
015	CONSELHO REGIONAL DE BIOLOGIA	CRBIO	CRAS
016	INTERNO	INTERNO	
'''


# Categoria: select * from mvcatcad
# select cod_categ,descricao,nome_conselho_regi,sigla_conselho_reg from mvcatcad order by descricao
# COD_CATEG,DESCRICAO,NOME_CONSELHO_REGI,SIGLA_CONSELHO_REG
def tipoconselho(tcon):
    # Medicos: #################
    if pro(tcon, "MEDICO") == "MEDICO":
        if pro(tcon, "MEDICO INTERNO") == "MEDICO INTERNO":
            return "016"

        elif pro(tcon, "MEDICO PEDIATRA") == "MEDICO PEDIATRA":
            return "001"

        elif pro(tcon, "MEDICO PS") == "MEDICO PS":
            return "001"

        else:
            return "001"
    ############################

    # Enfermagem: ##############
    elif pro(tcon, "ENFER") == "ENFER":
        if pro(tcon, "TECNICO DE ENFERMAGEM") == "TECNICO DE ENFERMAGEM":
            return "002"

        elif pro(tcon, "ENFERMEIRO OBSTETRA") == "ENFERMEIRO OBSTETRA":
            return "002"

        else:
            return "002"
    ############################

    elif pro(tcon, "ADMINISTRATIVO") == "ADMINISTRATIVO" \
            or pro(tcon, "INFORMATICA") == "INFORMATICA" \
            or pro(tcon, "ATEND") == "ATEND" \
            or pro(tcon, "ANALISTA DE SUPORTE") == "ANALISTA DE SUPORTE" \
            or pro(tcon, "ANALISTA DE SISTEMAS") == "ANALISTA DE SISTEMAS" \
            or pro(tcon, "AUXILIAR DE FARMACIA") == "AUXILIAR DE FARMACIA" \
            or pro(tcon, "LACTARISTA") == "LACTARISTA" \
            or pro(tcon, "APRENDIZ") == "APRENDIZ" \
            or pro(tcon, "ESTAGIARIO") == "ESTAGIARIO" \
            or pro(tcon, "SEGURANCA") == "SEGURANCA" \
            or pro(tcon, "RAIO") == "RAIO" \
            or pro(tcon, "RADIO") == "RADIO":
        return "012"

    elif pro(tcon, "ASSISTENTE SOCIAL") == "ASSISTENTE SOCIAL":
        return "014"

    elif pro(tcon, "FARMACEUTICO") == "FARMACEUTICO":
        return "006"

    elif pro(tcon, "FISIOTERAPEUTA") == "FISIOTERAPEUTA" \
            or pro(tcon, "TERAPEUTA OCUPACIONAL") == "TERAPEUTA OCUPACIONAL" \
            or pro(tcon, "FISIO") == "FISIO":
        return "005"

    elif pro(tcon, "FONOAUDIOLOGA") == "FONOAUDIOLOGA":
        return "007"

    elif pro(tcon, "LABORATORIO") == "LABORATORIO":
        return "013"

    elif pro(tcon, "NUTRICIONISTA") == "NUTRICIONISTA":
        return "003"

    elif pro(tcon, "PSICOLOGO") == "PSICOLOGO":
        return "008"

    elif pro(tcon, "SCIH") == "SCIH":
        return "002"

    elif pro(tcon, "BIOLOGISTA") == "BIOLOGISTA":
        return "015"

    else:
        return "''"
