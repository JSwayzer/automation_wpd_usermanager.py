import re


def pro(string, pattern):
    result = re.search(pattern, string)
    if result is not None:
        return result.group()


# ESPECIALIDADES: select distinct(cod_esp) from faesppro
# select cod_esp, descricao from faespcad order by descricao
# COD_ESP	DESCRICAO
def especialidade(esp):
    if pro(esp, "ACUPUNTURA") == "ACUPUNTURA":
        return "001"
    elif pro(esp, "ALERGIA E IMUNOLOGIA") == "ALERGIA E IMUNOLOGIA" \
            or pro(esp, "ALERGIA") == "ALERGIA" \
            or pro(esp, "IMUNOLOGIA") == "IMUNOLOGIA":
        return "0030"
    elif pro(esp, "ANATOMIA PATOLOGICA") == "ANATOMIA PATOLOGICA":
        return "0063"
    elif pro(esp, "ANESTE") == "ANESTE":
        if pro(esp, "ANESTESIOLOGIA") == "ANESTESIOLOGIA" \
                or pro(esp, "ANESTESISTA") == "ANESTESISTA":
            return "002"
        elif pro(esp, "ANESTESISTA UROLOGIA") == "ANESTESISTA UROLOGIA":
            return "0093"
    elif pro(esp, "ANGIOLOGISTA") == "ANGIOLOGISTA" \
            or pro(esp, "ANGIO") == "ANGIO":
        return "0031"
    elif pro(esp, "BUCO MAXILO") == "BUCO MAXILO":
        return "0059"
    elif pro(esp, "CANCEROLOGIA") == "CANCEROLOGIA"\
            or pro(esp, "CANCER") == "CANCER":
        # elif pro(esp, "CANCEROLOGIA/CIRURGICA") == "CANCEROLOGIA/CIRURGICA":
        if pro(esp, "CANCEROLOGIA CIRURGICA") == "CANCEROLOGIA CIRURGICA":
            return "0032"
        # elif pro(esp, "CANCEROLOGIA/CLINICA") == "CANCEROLOGIA/CLINICA":
        elif pro(esp, "CANCEROLOGIA CLINICA") == "CANCEROLOGIA CLINICA":
            return "004"
        # elif pro(esp, "CANCEROLOGIA/PEDIATRICA") == "CANCEROLOGIA/PEDIATRICA":
        elif pro(esp, "CANCEROLOGIA PEDIATRICA") == "CANCEROLOGIA PEDIATRICA":
            return "0033"
        else:
            return "003"
    elif pro(esp, "CARDIOLOGIA") == "CARDIOLOGIA":
        return "005"
    elif pro(esp, "CIRURGIA") == "CIRURGIA":
        if pro(esp, "CIRURGIA CARDIOVASCULAR") == "CIRURGIA CARDIOVASCULAR":
            return "0034"
        elif pro(esp, "CIRURGIA DA MAO") == "CIRURGIA DA MAO":
            return "006"
        elif pro(esp, "CIRURGIA DE CABECA E PESCOCO") == "CIRURGIA DE CABECA E PESCOCO":
            return "0035"
        elif pro(esp, "CIRURGIA DO APARELHO DIGESTIVO") == "CIRURGIA DO APARELHO DIGESTIVO":
            return "007"
        elif pro(esp, "CIRURGIA GERAL") == "CIRURGIA GERAL":
            return "0036"
        elif pro(esp, "CIRURGIA GINECOLOGIA") == "CIRURGIA GINECOLOGIA":
            return "0073"
        elif pro(esp, "CIRURGIA OFTALMOLOGIA") == "CIRURGIA OFTALMOLOGIA":
            return "0072"
        elif pro(esp, "CIRURGIA ORTOPEDIA") == "CIRURGIA ORTOPEDIA":
            return "0070"
        elif pro(esp, "CIRURGIA OTORRINO") == "CIRURGIA OTORRINO":
            return "0071"
        elif pro(esp, "CIRURGIA PEDIATRICA") == "CIRURGIA PEDIATRICA":
            return "008"
        elif pro(esp, "CIRURGIA PLASTICA") == "CIRURGIA PLASTICA":
            return "0037"
        elif pro(esp, "CIRURGIA TORACICA") == "CIRURGIA TORACICA":
            return "009"
        elif pro(esp, "CIRURGIA UROLOGIA") == "CIRURGIA UROLOGIA":
            return "0074"
        elif pro(esp, "CIRURGIA VASCULAR") == "CIRURGIA VASCULAR":
            return "0038"
        else:
            return "0036"
    elif pro(esp, "CITOLOGIA") == "CITOLOGIA":
        return "0060"
    elif pro(esp, "CLINICA MEDICA") == "CLINICA MEDICA":
        return "0010"
    elif pro(esp, "COLOPROCTOLOGIA") == "COLOPROCTOLOGIA":
        return "0039"
    elif pro(esp, "CUIDADOS PALIATIVOS") == "CUIDADOS PALIATIVOS":
        return "0091"
    elif pro(esp, "DERMATOLOGIA") == "DERMATOLOGIA" \
            or pro(esp, "DERMA") == "DERMA":
        return "0011"
    elif pro(esp, "DIAGNOSTICO POR IMAGEM") == "DIAGNOSTICO POR IMAGEM":
        return "0012"
    elif pro(esp, "DIAGNOSTICO POR IMAGEM") == "DIAGNOSTICO POR IMAGEM":
        return "0040"
    elif pro(esp, "ENDOCRINOLOGIA E METABOLOGIA") == "ENDOCRINOLOGIA E METABOLOGIA" \
            or pro(esp, "ENDOCRINOLOGIA") == "ENDOCRINOLOGIA" \
            or pro(esp, "METABOLOGIA") == "METABOLOGIA":
        return "0041"
    elif pro(esp, "ENDOSCOPIA") == "ENDOSCOPIA":
        return "0013"
    elif pro(esp, "ENFERMAGEM") == "ENFERMAGEM":
        if pro(esp, "ENFERMAGEM ALEITAMENTO MATERNO") == "ENFERMAGEM ALEITAMENTO MATERNO":
            return "0082"
        elif pro(esp, "ENFERMAGEM ESTOMATERAPEUTA") == "ENFERMAGEM ESTOMATERAPEUTA":
            return "0076"
        elif pro(esp, "ENFERMAGEM OBSTETRICA") == "ENFERMAGEM OBSTETRICA":
            return "0075"
        else:
            return "0083"
    elif pro(esp, "EXAME") == "EXAME":
        return "0084"
    elif pro(esp, "FISIOTERAPIA") == "FISIOTERAPIA":
        if pro(esp, "FISIOTERAPIA MOTORA") == "FISIOTERAPIA MOTORA":
            return "0078"
        elif pro(esp, "FISIOTERAPIA RESPIRATORIA") == "FISIOTERAPIA RESPIRATORIA":
            return "0077"
        else:
            return "0088"
    elif pro(esp, "FONOAUDIOLOGIA") == "FONOAUDIOLOGIA":
        return "0079"
    elif pro(esp, "GASTROENTEROLOGIA") == "GASTROENTEROLOGIA":
        return "0042"
    elif pro(esp, "GENETICA MEDICA") == "GENETICA MEDICA":
        return "0014"
    elif pro(esp, "GERIATRIA") == "GERIATRIA":
        return "0043"
    elif pro(esp, "GINECOLOGIA E OBSTETRICIA") == "GINECOLOGIA E OBSTETRICIA"\
            or pro(esp, "GINECOLOGIA") == "GINECOLOGIA" \
            or pro(esp, "OBSTETRICIA") == "OBSTETRICIA"\
            or pro(esp, "GINECO") == "GINECO" \
            or pro(esp, "OBSTETR") == "OBSTETR":
        return "0015"
    elif pro(esp, "HANSENOLOGIA") == "HANSENOLOGIA":
        return "0062"
    elif pro(esp, "HEMATOLOGIA E HEMOTERAPIA") == "HEMATOLOGIA E HEMOTERAPIA":
        return "0044"
    elif pro(esp, "HOMEOPATIA") == "HOMEOPATIA":
        return "0016"
    elif pro(esp, "INFECTOLOGIA") == "INFECTOLOGIA" \
            or pro(esp, "INFECTO") == "INFECTO":
        return "0045"
    elif pro(esp, "LABORATORIO") == "LABORATORIO":
        return "0086"
    elif pro(esp, "MASTOLOGIA") == "MASTOLOGIA":
        return "0017"
    # elif pro(esp, "MEDICINA DE FAMILIA/COMUNIDADE") == "MEDICINA DE FAMILIA/COMUNIDADE":
    elif pro(esp, "MEDICINA DE FAMILIA") == "MEDICINA DE FAMILIA":
        return "0046"
    elif pro(esp, "MEDICINA DO TRABALHO") == "MEDICINA DO TRABALHO":
        return "0018"
    elif pro(esp, "MEDICINA DO TRAFEGO") == "MEDICINA DO TRAFEGO":
        return "0047"
    elif pro(esp, "MEDICINA ESPORTIVA") == "MEDICINA ESPORTIVA":
        return "0019"
    elif pro(esp, "MEDICINA FISICA E REABILITACAO") == "MEDICINA FISICA E REABILITACAO":
        return "0048"
    elif pro(esp, "MEDICINA INTENSIVA") == "MEDICINA INTENSIVA":
        return "0020"
    elif pro(esp, "MEDICINA LEGAL") == "MEDICINA LEGAL":
        return "0049"
    elif pro(esp, "MEDICINA NUCLEAR") == "MEDICINA NUCLEAR":
        return "0021"
    elif pro(esp, "MEDICINA PREVENTIVA E SOCIAL") == "MEDICINA PREVENTIVA E SOCIAL":
        return "0050"
    elif pro(esp, "MEDICINA SANITARIA") == "MEDICINA SANITARIA":
        return "0068"
    elif pro(esp, "MELHOR EM CASA") == "MELHOR EM CASA":
        return "PROH"
    elif pro(esp, "MELHOR EM CASA") == "MELHOR EM CASA":
        return "PROHD"
    elif pro(esp, "NEFROLOGIA") == "NEFROLOGIA" \
            or pro(esp, "NEFRO") == "NEFRO":
        return "0022"
    elif pro(esp, "NEONATOLOGIA") == "NEONATOLOGIA" \
            or pro(esp, "NEONAT") == "NEONAT":
        return "0085"
    elif pro(esp, "NEUROCIRURGIA") == "NEUROCIRURGIA":
        return "0051"
    elif pro(esp, "NEUROLOGIA") == "NEUROLOGIA" \
            or pro(esp, "NEURO") == "NEURO":
        if pro(esp, "NEUROLOGIA PEDIATRICA") == "NEUROLOGIA PEDIATRICA":
            return "0069"
        elif pro(esp, "NEUROLOGISTA PEDIATRA") == "NEUROLOGISTA PEDIATRA":
            return "0067"
        else:
            return "0023"
    elif pro(esp, "NUTRIÇÃO") == "NUTRIÇÃO":
        return "0081"
    elif pro(esp, "NUTROLOGIA") == "NUTROLOGIA":
        return "0052"
    elif pro(esp, "OFTALMOLOGIA") == "OFTALMOLOGIA":
        return "0024"
    elif pro(esp, "ONCOLOGIA CLINICA") == "ONCOLOGIA CLINICA":
        return "0064"
    elif pro(esp, "ORTOPEDIA E TRAUMATOLOGIA") == "ORTOPEDIA E TRAUMATOLOGIA" \
            or pro(esp, "ORTOPED") == "ORTOPED" \
            or pro(esp, "TRAUMATOLOGI") == "TRAUMATOLOGI":
        return "0053"
    elif pro(esp, "OTORRINOLARINGOLOGIA") == "OTORRINOLARINGOLOGIA":
        return "0025"
    elif pro(esp, "PATOLOGIA") == "PATOLOGIA":
        return "0054"
    # elif pro(esp, "PATOLOGIA CLINICA/MEDICINAL") == "PATOLOGIA CLINICA/MEDICINAL":
    elif pro(esp, "PATOLOGIA CLINICA") == "PATOLOGIA CLINICA/MEDICINAL":
        return "0026"
    elif pro(esp, "PEDIATRIA") == "PEDIATRIA":
        return "0055"
    elif pro(esp, "PNEUMOLOGIA") == "PNEUMOLOGIA"\
            or pro(esp, "PNEUMO") == "PNEUMO"\
            or pro(esp, "PNEU") == "PNEU":
        return "0027"
    elif pro(esp, "PRE OPERATORIO") == "PRE OPERATORIO"\
            or pro(esp, "OPERATORIO") == "OPERATORIO":
        return "0090"
    elif pro(esp, "PROCTOLOGIA") == "PROCTOLOGIA":
        return "0089"
    elif pro(esp, "PRONTO SOCORRO") == "PRONTO SOCORRO":
        return "0087"
    elif pro(esp, "PSICOLOGIA") == "PSICOLOGIA":
        return "0080"
    elif pro(esp, "PSIQUIATRIA") == "PSIQUIATRIA":
        return "0056"
    elif pro(esp, "RADIOLOGIA E DIAGNOSTICO") == "RADIOLOGIA E DIAGNOSTICO" \
            or pro(esp, "RADIOLOGIA") == "RADIOLOGIA"\
            or pro(esp, "RADIOL") == "RADIOL":
        return "0028"
    elif pro(esp, "RADIOTERAPIA") == "RADIOTERAPIA":
        return "0057"
    elif pro(esp, "REUMATOLOGIA") == "REUMATOLOGIA":
        return "0029"
    elif pro(esp, "SERVICO SOCIAL") == "SERVICO SOCIAL":
        return "0092"
    elif pro(esp, "SEXOLOGIA") == "SEXOLOGIA":
        return "0061"
    elif pro(esp, "TERAPIA INTENSIVA") == "TERAPIA INTENSIVA" \
            or pro(esp, "UTI") == "UTI":
        return "0065"
    elif pro(esp, "TISIOLOGIA") == "TISIOLOGIA":
        return "0066"
    elif pro(esp, "UROLOGIA") == "UROLOGIA":
        return "0058"
