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
            return "RG"

        elif pro(tcon, "MEDICO PEDIATRA") == "MEDICO PEDIATRA":
            return "CRM"

        elif pro(tcon, "MEDICO PS") == "MEDICO PS":
            return "CRM"

        else:
            return "CRM"
    ############################

    # Enfermagem: ##############
    elif pro(tcon, "ENFER") == "ENFER":
        if pro(tcon, "TECNICO DE ENFERMAGEM") == "TECNICO DE ENFERMAGEM":
            return "COREN"

        elif pro(tcon, "ENFERMEIRO OBSTETRA") == "ENFERMEIRO OBSTETRA":
            return "COREN"

        else:
            return "COREN"
    ############################

    elif pro(tcon, "ADMINISTRATIVO") == "ADMINISTRATIVO":
        return ""

    elif pro(tcon, "ASSISTENTE SOCIAL") == "ASSISTENTE SOCIAL":
        return "CRESS"

    elif pro(tcon, "AUXILIAR DE FARMACIA") == "AUXILIAR DE FARMACIA":
        return "AUXF"

    elif pro(tcon, "FARMACEUTICO") == "FARMACEUTICO":
        return "CRF"

    elif pro(tcon, "FISIOTERAPEUTA") == "FISIOTERAPEUTA":
        return "CREFITO"

    elif pro(tcon, "FONOAUDIOLOGA") == "FONOAUDIOLOGA":
        return "CRFA"

    elif pro(tcon, "INFORMATICA") == "INFORMATICA":
        return "INF"

    elif pro(tcon, "LABORATORIO") == "LABORATORIO":
        return "CRBM"

    elif pro(tcon, "NUTRICIONISTA") == "NUTRICIONISTA":
        return "CRN"

    elif pro(tcon, "PSICOLOGO") == "PSICOLOGO":
        return "CRP"

    elif pro(tcon, "SCIH") == "SCIH":
        return ""

    elif pro(tcon, "TERAPEUTA OCUPACIONAL") == "TERAPEUTA OCUPACIONAL":
        return "CREFITO"
