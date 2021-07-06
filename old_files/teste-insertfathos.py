from function_create_fathos import *
from functions.function_categoria_profissional import *
from functions.function_grupo_medico import *
from functions.function_tipo_conselho import *
import re


def pro(string, pattern):
    result = re.search(pattern, string)
    if result is not None:
        return result.group()


"""pattern = 'llo'
string = '-----2344-Hello--World!'
result = re.search(pattern, string)
print(result.group())
if result is not None:
    print('WOW')
print(result)"""

readFile = open("../usuarios.txt", "r")
createFile = open("../insert_fathos.txt", "w")
indPermIntern = "N"
indPermAssLaudo = "N"
codGrupoMedico = ""
contador = 0
for x in readFile:
    x = x.upper()
    linha = x.split(',')
    codProfissao = profissao(linha[3])
    print(codProfissao)
    codCategoria = categoria(linha[3])
    print(codCategoria)
    codConselho = tipoconselho(linha[3])
    print(codConselho)
    if codProfissao == "MEDC":
        codGrupoMedico = grupomedico(linha[14])
        print(codGrupoMedico)
        # espMedica = especialidade(linha[14])
        # print(espMedica)
        indPermIntern = "S"
        indPermAssLaudo = "s"
    contador += 1
    print(contador)
    createFile.write("INSERT INTO FAPROCAD (cpf,crm,uf_crm,cod_ant,cod_pro_corp,cod_profissao,"
                     "fone_celular,bip_pager,email,nome_reduzido,cod_cnes,NU_CNS,SN_EXIBE_RES_CIRURGIA,"
                     "cod_categ,SN_NAO_TEM_INFORMOU_EMAIL,cep_res,end,bairro_res,cidade_res,estado_res,"
                     "NUMERO_RES,COMPLEMENTO_RES,fone_res,cep_tra,end_tra,bairro_tra,cidade_tra,estado_tra,"
                     "NUMERO_TRA,COMPLEMENTO_TRAB,fone_tra,TP_EST_CIVIL,DS_ORGAO_EMIS_ID,NO_PAI,"
                     "DS_FORMAC_PROF,NU_ID,DS_NACIONALIDADE,NO_MAE,TP_ESCOLARIDADE,SG_UF_NASC,FK_LOCALI_NASC,"
                     "TP_RACA_COR,TP_SIT_CONJUGAL,SG_UF_ID,NU_OUTROS_DOCUMENT,DS_CARGO,SN_INCAPAZ_BIOM,banco,"
                     "conta,agencia,funcionario,staff,docente,sn_cooperado,perc_impos,recibo,ind_perm_intern,"
                     "ind_perm_ass_laudo,sn_lib_laudo_prov,ind_perm_comanda,cta_provisao_mega,cta_adianta_mega,"
                     "cod_movto_mega,repasse_grupo_mega,classe_finan_mega,cod_pro,nome_pro,data_nascimento,"
                     "inativo,tratamento,grupo,perc_hosp,tipo_pac_autoriz,cod_tp_conselho,cod_tipo_lograd_re,"
                     "cod_tipo_lograd_tr,DS_HORARIOS,FK_CEP_RES,FK_CEP_TRA ) VALUES "
                     "('"+linha[7]+"','"+linha[4]+"','"+linha[11]+"','"+linha[10]+"','',"
                     "'"+codProfissao+"','','','','','','','N','"+codCategoria+"','S',"
                     "'04948970','ESTRADA DO M BOI MIRIM 4815','JARDIM ANGELA (ZONA SUL)','SAO PAULO','SP','5203',"
                     "NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'1158322500',NULL,'','','','','','',"
                     "NULL,NULL,NULL,NULL,NULL,NULL,'','','N','','','','S','N','N','N',0,'N',"
                     "'"+indPermIntern+"','"+indPermAssLaudo+"','N','S','','','','N','','"+linha[10]+"',"
                     "'"+linha[1]+"',To_Date('"+linha[6]+"', 'DD/MM/YYYY'),'N',NULL,"+codGrupoMedico+","
                     "NULL,'IAUE',"+codConselho+",NULL,NULL,NULL,885459,NULL);\n")

"""print("INSERT INTO FAPROCAD ( cpf,crm,uf_crm,cod_ant,cod_pro_corp,cod_profissao,"
      "fone_celular,bip_pager,email,nome_reduzido,cod_cnes,NU_CNS,SN_EXIBE_RES_CIRURGIA,"
      "cod_categ,SN_NAO_TEM_INFORMOU_EMAIL,cep_res,end,bairro_res,cidade_res,estado_res,"
      "NUMERO_RES,COMPLEMENTO_RES,fone_res,cep_tra,end_tra,bairro_tra,cidade_tra,estado_tra,"
      "NUMERO_TRAB,COMPLEMENTO_TRAB,fone_tra,TP_EST_CIVIL,DS_ORGAO_EMIS_ID,NO_PAI,"
      "DS_FORMAC_PROF,NU_ID,DS_NACIONALIDADE,NO_MAE,TP_ESCOLARIDADE,SG_UF_NASC,FK_LOCALI_NASC,"
      "TP_RACA_COR,TP_SIT_CONJUGAL,SG_UF_ID,NU_OUTROS_DOCUMENT,DS_CARGO,SN_INCAPAZ_BIOM,banco,"
      "conta,agencia,funcionario,staff,docente,sn_cooperado,perc_impos,recibo,ind_perm_intern,"
      "ind_perm_ass_laudo,sn_lib_laudo_prov,ind_perm_comanda,cta_provisao_mega,cta_adianta_mega,"
      "cod_movto_mega,repasse_grupo_mega,classe_finan_mega,cod_pro,nome_pro,data_nascimento,"
      "inativo,tratamento,grupo,perc_hosp,tipo_pac_autoriz,cod_tp_conselho,cod_tipo_lograd_re,"
      "cod_tipo_lograd_tr,DS_HORARIOS,FK_CEP_RES,FK_CEP_TRA ) VALUES "
     "('"+linha[7]+"','"+numRegistro+"','"+ufCRM+"','"+linha[10]+"','"
     "','"+codProfissao+"','','','','','','','N','"+codCategoria+"','S',"
     "'04948970','ESTRADA DO M BOI MIRIM 4815','JARDIM ANGELA (ZONA SUL)','SAO PAULO','SP','5203',"
     "NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'1158322500',NULL,'','','','','','',"
     "NULL,NULL,NULL,NULL,NULL,NULL,'','','N','','','','S','N','N','N',0,"
     "'N',"+linha[10]+"','"+linha[1]+"',To_Date('"+linha[6]+"', 'DD/MM/YYYY'),"
     "'N',NULL,'"+gpMedico+"',NULL,'IAUE','"+codConselho+"',NULL,NULL,NULL,885459,NULL);")"""

# partial match in list
# h
# h
# Verificar profissao - se médico, enfermeiro, auxiliar administrativo
# verificar categoria - se profissao = médico: médico ou médico interno ou medico pediatra ou medico PS
#                       se profissao = enfermeiro: enfermagem ou enfermeiro obstetra ou scih
#                       se profissao = administrativo: administrativo
# verificar grupo médico - se profissão = médico: definir o grupo médico!

