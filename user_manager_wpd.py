from functions.function_profissao import *
from functions.function_categoria_profissional import *
from functions.function_grupo_medico import *
from functions.function_tipo_conselho import *
from functions.function_especialidade import *
from functions.function_atribuicao_grupos import *
from functions.function_replace_specialcharacters import *


def pro(string, pattern):
    result = re.search(pattern, string)
    if result is not None:
        return result.group()


# while True:
#    try:
op = -1
while op != 0:
    print("Script para gerenciar usuários do WPD"
          "\n1 - SQL Script para Checar se usuário já existe e se está inativo"
          "\n2 - SQL Script para Inativar usuário"
          "\n3 - SQL Script para Reativar usuário"
          "\n4 - SQL Script para Criar usuário FATHOS"
          "\n5 - SQL Script para Criar usuário MEDIVEW"
          "\n6 - SQL Script para Checar se usuário já existe e se está inativo - só com nome"
          "\n0 - Sair do programa")
    op = int(input("Escolha sua opção: "))
    if op == 1:
        # NOME
        with open("usuarios.txt", "r") as readFile:  # ler arquivo fonte dos dados
            with open("checar_usuario.txt", "w") as createFile:  # criar o arquivo que armazenará as novas informações já tratadas
                createFile.write("select t1.ind_usuario_ativo as ativo_medview,\n"
                                 "       t1.sn_usu_bloqueado as bloqueado_medview,\n"
                                 "       t2.inativo as inativo_fathos,\n"
                                 "       t1.matricula,\n"
                                 "       t1.apelido as login,\n"
                                 "       t1.nome as nome_medview,\n"
                                 "       t2.nome_pro as nome_fathos,\n"
                                 "       t1.cod_pro,\n"
                                 "       t2.crm,\n"
                                 "       t1.cpf as cpf_medview,\n"
                                 "       t2.cpf as cpf_fathos,\n"
                                 "       t1.dh_nascimento as dt_medview,\n"
                                 "       t2.data_nascimento as dt_fathos\n"
                                 "  from fausucad t1\n"
                                 " inner join faprocad t2 on t2.cod_pro = t1.cod_pro\n"
                                 " where t1.nome      in (")

                # escrever nome:
                for x in readFile:  # loop para ler linha por linha para manipulação
                    x = x.upper()
                    linha = x.split('	')
                    nome = strip_accents(linha[1])
                    createFile.write("'" + nome + "',")
                createFile.write("'" + nome + "')\n")

        # CPF
        with open("usuarios.txt", "r") as readFile:
            with open("checar_usuario.txt", "a") as createFile:
                createFile.write("    or t1.cpf       in (")
                for y in readFile:
                    linha = y.split('	')
                    createFile.write("'" + linha[7] + "',")
                createFile.write("'" + linha[7] + "')\n")

        # CRM
        with open("usuarios.txt", "r") as readFile:
            with open("checar_usuario.txt", "a") as createFile:
                createFile.write("    or t2.crm       in (")
                for z in readFile:
                    linha = z.split('	')
                    createFile.write("'" + linha[4] + "',")
                createFile.write("'" + linha[4] + "')\n")

        # apelido
        with open("usuarios.txt", "r") as readFile:
            with open("checar_usuario.txt", "a") as createFile:
                createFile.write("    or t1.apelido   in (")
                for apelido in readFile:
                    apelido = apelido.upper()
                    linha = apelido.split('	')
                    createFile.write("'" + linha[12] + "',")
                createFile.write("'" + linha[12] + "')\n")

        # matricula
        with open("usuarios.txt", "r") as readFile:
            with open("checar_usuario.txt", "a") as createFile:
                createFile.write("    or t1.matricula in (")
                for matricula in readFile:
                    linha = matricula.split('	')
                    createFile.write("'" + linha[0] + "',")
                createFile.write("'" + linha[0] + "')\n")

        # cod_pro
        with open("usuarios.txt", "r") as readFile:
            with open("checar_usuario.txt", "a") as createFile:
                createFile.write("    or t2.cod_pro   in (")
                for cod_pro in readFile:
                    linha = cod_pro.split('	')
                    createFile.write("'" + linha[10] + "',")
                createFile.write("'" + linha[10] + "');\n")
        print("\nConcluído com sucesso!\n\n")
    elif op == 2:
        with open("usuarios.txt", "r", encoding="utf8") as readFile:
            with open("inativar_usuario.txt", "w", encoding="utf8") as createFile:
                for x in readFile:
                    x = x.upper()
                    nome = strip_accents(x)
                    createFile.write("update faprocad x set x.inativo = 'S' where x.nome_pro = '" + nome + "';\n")
                    createFile.write("update fausucad x set x.ind_usuario_ativo = 'N', sn_usu_bloqueado = 'S' "
                                     "where x.nome = '" + nome + "';\n")
        print("\nConcluído com sucesso!\n\n")
    elif op == 3:
        with open("usuarios.txt", "r", encoding="utf8") as readFile:
            with open("reativar_usuario.txt", "w", encoding="utf8") as createFile:
                for x in readFile:
                    x = x.upper()
                    nome = strip_accents(x)
                    createFile.write("update faprocad x set x.inativo = 'N' where x.nome_pro = '" + nome + "';\n")
                    createFile.write("update fausucad x set x.ind_usuario_ativo = 'S', sn_usu_bloqueado = 'N' "
                                     "where x.nome = '" + nome + "';\n")
        print("\nConcluído com sucesso!\n\n")
    elif op == 4:
        with open("usuarios.txt", "r") as readFile:
            with open("insert_fathos.txt", "w") as createFile:
                # Essas variáveis podem ser vazias, caso não seja médico ou outras profissões que tenha
                indPermIntern = "N"
                indPermAssLaudo = "N"
                codGrupoMedico = ""
                for x in readFile:
                    x = x.upper()
                    linha = x.split('	')
                    # Chamar função para definir a Profissão
                    codProfissao = profissao(linha[3])
                    print("Profissão: ", codProfissao)
                    # Chamar função para definir a Categoria profissional
                    codCategoria = categoria(linha[3])
                    print("Categoria: ", codCategoria)
                    # Chamar função para definir o Tipo de Conselho Regional
                    codConselho = tipoconselho(linha[3])
                    print("Conselho: ", codConselho)
                    if codProfissao == "MEDC":
                        # Chamar função para definir o Grupo Medico
                        codGrupoMedico = grupomedico(linha[14])  # print("Grupo Medico", codGrupoMedico)
                        indPermIntern = "S"
                        indPermAssLaudo = "s"

                    createFile.write("INSERT INTO FAPROCAD (cpf,crm,uf_crm,cod_ant,cod_pro_corp,cod_profissao,"
                                     "fone_celular,bip_pager,email,nome_reduzido,cod_cnes,NU_CNS,SN_EXIBE_RES_CIRURGIA,"
                                     "cod_categ,SN_NAO_TEM_INFORMOU_EMAIL,cep_res,end,bairro_res,cidade_res,estado_res,"
                                     "NUMERO_RES,COMPLEMENTO_RES,fone_res,cep_tra,end_tra,bairro_tra,cidade_tra,"
                                     "estado_tra,NUMERO_TRAB,COMPLEMENTO_TRAB,fone_tra,TP_EST_CIVIL,DS_ORGAO_EMIS_ID,"
                                     "NO_PAI,DS_FORMAC_PROF,NU_ID,DS_NACIONALIDADE,NO_MAE,TP_ESCOLARIDADE,SG_UF_NASC,"
                                     "FK_LOCALI_NASC,TP_RACA_COR,TP_SIT_CONJUGAL,SG_UF_ID,NU_OUTROS_DOCUMENT,DS_CARGO,"
                                     "SN_INCAPAZ_BIOM,banco,conta,agencia,funcionario,staff,docente,sn_cooperado,"
                                     "perc_impos,recibo,ind_perm_intern,ind_perm_ass_laudo,sn_lib_laudo_prov,"
                                     "ind_perm_comanda,cta_provisao_mega,cta_adianta_mega,cod_movto_mega,"
                                     "repasse_grupo_mega,classe_finan_mega,cod_pro,nome_pro,data_nascimento,"
                                     "inativo,tratamento,grupo,perc_hosp,tipo_pac_autoriz,cod_tp_conselho,"
                                     "cod_tipo_lograd_re,cod_tipo_lograd_tr,DS_HORARIOS,FK_CEP_RES,FK_CEP_TRA ) VALUES "
                                     "('" + linha[7] + "','" + linha[4] + "','" + linha[11] + "','" + linha[10] + "','',"
                                     "'" + codProfissao + "','','','','','','','N','" + codCategoria + "','S',"
                                     "'04948970','ESTRADA DO M BOI MIRIM 4815','JARDIM ANGELA (ZONA SUL)','SAO PAULO','SP','5203',"
                                     "NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'1158322500',NULL,'','','','','','',"
                                     "NULL,NULL,NULL,NULL,NULL,NULL,'','','N','','','','S','N','N','N',0,'N',"
                                     "'" + indPermIntern + "','" + indPermAssLaudo + "','N','S','','','','N','','" + linha[10] + "',"
                                     "'" + linha[1] + "',To_Date('" + linha[6] + "', 'DD/MM/YYYY'),'N',NULL,'" + codGrupoMedico + "',"
                                     "NULL,'IAUE','" + codConselho + "',NULL,NULL,NULL,885459,NULL);\n")
                    if codProfissao == "MEDC":
                        # Chamar função para definir o Especialidade Médica
                        espMedica = especialidade(linha[14])  # print(espMedica)
                        espinsert = ("INSERT INTO FAESPPRO (COD_PRO, COD_ESP, SN_PRINCIPAL) VALUES "
                                     "('" + linha[10] + "','" + espMedica + "','S');\n")  # print(espinsert)
                        createFile.write(espinsert)
        print("\nConcluído com sucesso!\n\n")
    elif op == 5:
        with open("usuarios.txt", "r", encoding="utf8") as readFile:
            with open("insert_medview.txt", "w", encoding="utf8") as createFile:
                # loop para ler linha por linha para manipulação
                for x in readFile:
                    x = x.upper()
                    linha = x.split('	')
                    createFile.write(
                        "INSERT INTO FAUSUCAD (MATRICULA, APELIDO, NOME, IND_USUARIO_ATIVO, SN_USU_BLOQUEADO, "
                        "SN_LIBERAR_ACESSO, DH_VALIDADE, DT_HR_ULTIMA_SENHA, COD_BAR_USU, COD_PRO, SETOR, "
                        "FK_COD_SET, CPF, DH_NASCIMENTO, EMAIL, SN_ESTRANGEIRO, NU_DOC_ESTRANG, FK_PAIS) VALUES "
                        "('" + linha[0] + "', '" + linha[12] + "', '" + linha[1] + "', 'S', 'N', 'N', "
                        "To_Date('" + linha[13] + "', 'DD/MM/YYYY'), NULL, NULL, '" + linha[10] + "', NULL, '', "
                        "'" + linha[7] + "', To_Date('" + linha[6] + "', 'DD/MM/YYYY'), NULL, 'N', NULL, NULL);\n")
                    atribui = atribuicaogrupo(linha[17])
                    a = atribui.split(' ')
                    for i in range(0, len(a), 2):
                        createFile.write("insert into faususis (sistema, cod_grupo, matricula) values "
                                         "('" + a[i] + "','" + a[i + 1] + "','" + linha[0] + "');\n")
        print("\nConcluído com sucesso!\n\n")
    elif op == 6:
        with open("usuarios.txt", "r", encoding="utf8") as readFile:  # ler arquivo fonte dos dados
            with open("checar_usuario.txt", "w", encoding="utf8") as createFile:  # criar o arquivo que armazenará as novas informações já tratadas
                createFile.write("select t1.ind_usuario_ativo as ativo_medview,\n"
                                 "       t1.sn_usu_bloqueado as bloqueado_medview,\n"
                                 "       t2.inativo as inativo_fathos,\n"
                                 "       t1.matricula,\n"
                                 "       t1.apelido as login,\n"
                                 "       t1.nome as nome_medview,\n"
                                 "       t2.nome_pro as nome_fathos,\n"
                                 "       t1.cod_pro,\n"
                                 "       t2.crm,\n"
                                 "       t1.cpf as cpf_medview,\n"
                                 "       t2.cpf as cpf_fathos,\n"
                                 "       t1.dh_nascimento as dt_medview,\n"
                                 "       t2.data_nascimento as dt_fathos\n"
                                 "  from fausucad t1\n"
                                 " inner join faprocad t2 on t2.cod_pro = t1.cod_pro\n"
                                 " where t1.nome in (")

                # escrever nome:
                for x in readFile:  # loop para ler linha por linha para manipulação
                    x = x.upper()
                    nome = strip_accents(x)
                    createFile.write("'"+nome+"',")
                    # exit()
                createFile.write("'"+nome+"')")
        print("\nConcluído com sucesso!\n\n")
#    except ValueError:
#        print("\nOops! Não foi informado um valor válido, tente novamente...\n\n")
#    break
