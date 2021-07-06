import re


def pro(string, pattern):
    result = re.search(pattern, string)
    if result is not None:
        return result.group()


# Grupo: select * from fagprcad
# select cod_grupro,descricao from fagprcad order by descricao
# COD_GRUPRO,DESCRICAO
def grupomedico(gpm):
    if pro(gpm, "AMBULATORIO DE ESPECIALIDADES") == "AMBULATORIO DE ESPECIALIDADES":
        return "017"

    elif pro(gpm, "ANALISES CLINICAS") == "ANALISES CLINICAS":
        return "010"

    elif pro(gpm, "ANALISES CLINICAS") == "ANALISES CLINICAS":
        return "001"

    elif pro(gpm, "ASSISTENCIA MEDICA AMBULATORIA ESPECIALIDADES") == "ASSISTENCIA MEDICA AMBULATORIA ESPECIALIDADES":
        return "019"

    elif pro(gpm, "ASSISTENCIA MEDICA AMBULATORIA") == "ASSISTENCIA MEDICA AMBULATORIA":
        return "018"

    elif pro(gpm, "CARDIOLOGIA") == "CARDIOLOGIA":
        return "012"

    elif pro(gpm, "CIRURGIA") == "CIRURGIA":
        if pro(gpm, "CIRURGIA GERAL") == "CIRURGIA GERAL" or pro(gpm, "MEDICO CIRURGIAO") == "MEDICO CIRURGIAO":
            return "002"

        elif pro(gpm, "CIRURGIA PEDIATRICA") == "CIRURGIA PEDIATRICA":
            return "028"

    elif pro(gpm, "CLINICA MEDICA") == "CLINICA MEDICA" or pro(gpm, "MEDICO CLINICO") == "MEDICO CLINICO":
        return "003"

    elif pro(gpm, "COORD MEDICO DE LABORATORIO") == "COORD MEDICO DE LABORATORIO":
        return "016"

    elif pro(gpm, "DIRETOR") == "DIRETOR":
        return "031"

    elif pro(gpm, "ENDOSCOPIA") == "ENDOSCOPIA":
        return "009"

    elif pro(gpm, "FISIOTERAPEUTA") == "FISIOTERAPEUTA":
        return "FISI"

    elif pro(gpm, "FONOAUDIOLOGO") == "FONOAUDIOLOGO":
        return "FONO"

    elif pro(gpm, "GINECOLOGIA") == "GINECOLOGIA" or pro(gpm, "OBSTRETRICIA") == "OBSTRETRICIA":
        return "004"

    elif pro(gpm, "MEDICINA DO TRABALHO") == "MEDICINA DO TRABALHO":
        return "015"

    elif pro(gpm, "MEDICO RESIDENTE") == "MEDICO RESIDENTE":
        return "030"

    elif pro(gpm, "NEFROLOGIA") == "NEFROLOGIA":
        return "027"

    elif pro(gpm, "NEONATOLOGIA") == "NEONATOLOGIA" \
            or pro(gpm, "NEONATO") == "NEONATO":
        return "011"

    elif pro(gpm, "NEUROLOGIA") == "NEUROLOGIA":
        return "029"

    elif pro(gpm, "NUTROLOGIA") == "NUTROLOGIA":
        return "023"

    elif pro(gpm, "ORTOPEDIA") == "ORTOPEDIA" or pro(gpm, "MEDICO ORTOPEDISTA") == "MEDICO ORTOPEDISTA":
        return "006"

    elif pro(gpm, "OTORRINOLARINGOLOGISTA") == "OTORRINOLARINGOLOGISTA":
        return "OTO"

    elif pro(gpm, "PEDIATRIA") == "PEDIATRIA" or pro(gpm, "MEDICO PEDIATRA") == "MEDICO PEDIATRA":
        return "005"

    elif pro(gpm, "PSIQUIATRIA") == "PSIQUIATRIA":
        return "007"

    elif pro(gpm, "RADIOLOGIA") == "RADIOLOGIA":
        return "008"

    elif pro(gpm, "SUPERVISAO") == "SUPERVISAO":
        return "014"

    elif pro(gpm, "UNID BAS DE SAUDE ADM MON AZUL") == "UNID BAS DE SAUDE ADM MON AZUL":
        return "022"

    elif pro(gpm, "UNID BAS DE SAUDE ADM OS-CEJAM") == "UNID BAS DE SAUDE ADM OS-CEJAM":
        return "021"

    elif pro(gpm, "UNID DE APOIO E RETAG DE SAUDE") == "UNID DE APOIO E RETAG DE SAUDE":
        return "020"

    elif pro(gpm, "UROLOGIA") == "UROLOGIA":
        return "024"

    elif pro(gpm, "TERAPIA INTENSIVA") == "TERAPIA INTENSIVA" \
            or pro(gpm, "UTI") == "UTI":
        return "013"

    elif pro(gpm, "VASCULAR") == "VASCULAR":
        return "026"

    elif pro(gpm, "VASECTOMIA") == "VASECTOMIA":
        return "025"
