# importação de funções específica do módulo calc.py
from functions.function_profissao import *
from functions.function_categoria_profissional import *
from functions.function_grupo_medico import *
from functions.function_tipo_conselho import *
from functions.function_especialidade import *
from functions.function_atribuicao_grupos import *


# outra forma seria importa tudo de um única vez:
# from calc import *


def pro(string, pattern):
    result = re.search(pattern, string)
    if result is not None:
        return result.group()


# while True:
#    try:
op = -1
while op != 0:
    print("Script para criar profissionais no Fathos"
          "\n1 - SQL Script para Checar se usuário já existe e se está inativo no FATHOS"
          "\n2 - SQL Script para Checar se usuário já existe e se está inativo no MEDVIEW"
          "\n3 - SQL Script para Inativar usuário FATHOS"
          "\n4 - SQL Script para Inativar usuário MEDIVEW"
          "\n5 - SQL Script para Criar usuário FATHOS"
          "\n6 - SQL Script para Criar usuário MEDIVEW"
          "\n0 - Sair do programa")
    op = int(input("Escolha sua opção: "))
    if op == 1:
        # ler arquivo fonte dos dados
        # NOME
        readFile = open("../usuarios.txt", "r")
        # criar o arquivo que armazenará as novas informações já tratadas
        createFile = open("checar_fathos.txt", "w")
        createFile.write("select x.inativo,\n\t x.nome_pro,\n\t x.cod_pro,\n\t x.cpf,\n\t x.data_nascimento "
                         "\nfrom faprocad x \nwhere ( x.nome_pro in (")
        # loop para ler linha por linha para manipulação
        # escrever nome:
        for x in readFile:
            x = x.upper()
            # separar linhas por vírgula (','), transformando em variável do tipo list
            linha = x.split('	')
            # escrever no arquivo as informações manipuladas
            # CHAPA,NOME,ADMISSAO,CARGO,REGISTRO,SECAO,DTNASCIMENTO,CPF,CARTIDENTIDADE,GESTOR,COD HCIS, UFCRM
            # após separado por vírgula, os textos podem ser lidos pelo índice: 0,1,2,3,4,5,6,7,8,9,10,11
            # escreverNome = (", '"+linha[1]+"'\n")
            # print(escreverNome)
            createFile.write("'"+linha[1]+"',\n\t")

        createFile.write("'"+linha[1]+"'\n\t")
        createFile.write(")")
        createFile.close()
        readFile.close()

        # CPF
        readFile = open("../usuarios.txt", "r")

        # criar o arquivo que armazenará as novas informações já tratadas
        createFile = open("checar_fathos.txt", "a")
        createFile.write("\n or x.cpf in (")
        for y in readFile:
            linha = y.split('	')
            createFile.write("'"+linha[7]+"',\n\t")

        createFile.write("'"+linha[7]+"'\n\t")
        createFile.write(")")
        createFile.close()
        readFile.close()

        # CRM
        readFile = open("../usuarios.txt", "r")

        # criar o arquivo que armazenará as novas informações já tratadas
        createFile = open("checar_fathos.txt", "a")
        createFile.write("\n or x.crm in (")
        for z in readFile:
            linha = z.split('	')
            createFile.write("'"+linha[4]+"',\n\t")
        createFile.write("'"+linha[4]+"'\n\t")
        createFile.write("))")
        createFile.close()
        readFile.close()

        # data_nascimento
        readFile = open("../usuarios.txt", "r")

        # criar o arquivo que armazenará as novas informações já tratadas
        createFile = open("checar_fathos.txt", "a")
        createFile.write("\n and x.data_nascimento in (")
        for w in readFile:
            linha = w.split('	')
            createFile.write("To_Date('"+linha[6]+"', 'DD/MM/YYYY'),\n\t")
        createFile.write("To_Date('"+linha[6]+"', 'DD/MM/YYYY')\n\t")
        createFile.write(");")
        createFile.close()
        readFile.close()
    elif op == 2:
        # CHAPA,NOME,DTNASCIMENTO,CPF,COD HCIS,LOGIN
        # após separado por vírgula, os textos podem ser lidos pelo índice: 0,1,6,7,10,12
        readFile = open("../usuarios.txt", "r")
        createFile = open("checar_medview.txt", "w")
        createFile.write(
            'select x.ind_usuario_ativo,\n\t sn_usu_bloqueado,\n\t x.matricula,\n\t x.apelido,\n\t x.nome, '
            '\n\tx.cod_pro,\n\t x.cpf,\n\t x.dh_nascimento\n from fausucad x\n where ( x.nome in (')
        # NOME
        for nome in readFile:
            nome = nome.upper()
            linha = nome.split('	')
            createFile.write("'"+linha[1]+"',\n\t")
        createFile.write("'"+linha[1]+"'\n\t")
        createFile.write(")")
        createFile.close()
        readFile.close()

        # apelido
        readFile = open("../usuarios.txt", "r")
        createFile = open("checar_medview.txt", "a")
        createFile.write("\n or x.apelido in (")
        for apelido in readFile:
            apelido = apelido.upper()
            linha = apelido.split('	')
            createFile.write("'"+linha[12]+"',\n\t")
        createFile.write("'"+linha[12]+"'\n\t")
        createFile.write(")")
        createFile.close()
        readFile.close()

        # matricula
        readFile = open("../usuarios.txt", "r")
        createFile = open("checar_medview.txt", "a")
        createFile.write("\n or x.matricula in (")
        for matricula in readFile:
            linha = matricula.split('	')
            createFile.write("'"+linha[0]+"',\n\t")
        createFile.write("'"+linha[0]+"'\n\t")
        createFile.write(")")
        createFile.close()
        readFile.close()

        # CPF
        readFile = open("../usuarios.txt", "r")
        createFile = open("checar_medview.txt", "a")
        createFile.write("\n or x.cpf in (")
        for cpf in readFile:
            linha = cpf.split('	')
            createFile.write("'"+linha[7]+"',\n\t")
            print(linha[7])
        createFile.write("'"+linha[7]+"'\n\t")
        createFile.write(")")
        createFile.close()
        readFile.close()

        # cod_pro
        readFile = open("../usuarios.txt", "r")

        # criar o arquivo que armazenará as novas informações já tratadas
        createFile = open("checar_medview.txt", "a")
        createFile.write("\n or x.cod_pro in (")

        for cod_pro in readFile:
            linha = cod_pro.split('	')
            createFile.write("'"+linha[10]+"',\n\t")
        createFile.write("'"+linha[10]+"'\n\t")
        createFile.write("))")
        createFile.close()
        readFile.close()

        # data_nascimento
        readFile = open("../usuarios.txt", "r")

        # criar o arquivo que armazenará as novas informações já tratadas
        createFile = open("checar_medview.txt", "a")
        createFile.write("\n and x.dh_nascimento in (")
        for dh_nascimento in readFile:
            linha = dh_nascimento.split('	')
            createFile.write("To_Date('"+linha[6]+"', 'DD/MM/YYYY'),\n\t")
        createFile.write("To_Date('"+linha[6]+"', 'DD/MM/YYYY')\n\t")
        createFile.write(");")
        createFile.close()
        readFile.close()
    elif op == 3:
        readFile = open("../desligamentos.txt", "r")
        createFile = open("inativar_fathos.txt", "w")
        for x in readFile:
            x = x.upper()
            # linha = x.split('	')
            # CHAPA,NOME,ADMISSAO,CARGO,REGISTRO,SECAO,DTNASCIMENTO,CPF,
            # CARTIDENTIDADE,GESTOR,COD HCIS,UFCRM,LOGIN,DH_VALIDADE
            # após separado por vírgula, os textos podem ser lidos pelo índice: 0,1,2,3,4,5,6,7,8,9,10,11,12,13
            '''createFile.write("update faprocad x set x.inativo = 'S' "
                             "where x.nome_pro = '"+linha[1]+"' and x.cpf = '"+linha[7]+"';\n")'''
            createFile.write("update faprocad x set x.inativo = 'S' where x.nome_pro = '"+x+"';\n")
        createFile.close()
        readFile.close()
    elif op == 4:
        readFile = open("../desligamentos.txt", "r")
        createFile = open("inativar_medview.txt", "w")
        for x in readFile:
            x = x.upper()
            # linha = x.split('	')
            # createFile.write("update fausucad x set x.ind_usuario_ativo = 'N' and sn_usu_bloqueado = 'S' "
            # "where x.matricula = '"+linha[0]+"' or x.apelido = '"+linha[12]+"' or x.cod_pro = '"+linha[10]+"' "
            # "(x.nome = '"+linha[1]+"' and x.cpf = '"+linha[7]+"' and x.dh_nascimento = '"+linha[6]+"';\n")
            '''createFile.write("update fausucad x set x.ind_usuario_ativo = 'N' and sn_usu_bloqueado = 'S' "
                             "where x.nome = '"+linha[1]+"' and x.cpf = '"+linha[7]+"' and"
                             " x.dh_nascimento = '"+linha[6]+"';\n")'''
            createFile.write("update fausucad x set x.ind_usuario_ativo = 'N', sn_usu_bloqueado = 'S' "
                             "where x.nome = '"+x+"';\n")
        createFile.close()
        readFile.close()
    elif op == 5:
        """pattern = 'llo'
        string = '-----2344-Hello--World!'
        result = re.search(pattern, string)
        print(result.group())
        if result is not None:
            print('WOW')
        print(result)"""

        # ler arquivo fonte dos dados
        readFile = open("../usuarios.txt", "r")
        # criar o arquivo que armazenará as novas informações já tratadas
        createFile = open("../insert_fathos.txt", "w")
        # Essas variáveis podem ser vazias, caso não seja médico ou outras profissões que tenha
        # regsitro em Conselho regional
        indPermIntern = "N"
        indPermAssLaudo = "N"
        codGrupoMedico = ""
        contador = 0
        # loop para ler linha por linha para manipulação
        for x in readFile:
            x = x.upper()
            # separar linhas por vírgula (','), transformando em variável do tipo list
            linha = x.split('	')
            # CHAPA,NOME,ADMISSAO,CARGO,REGISTRO,SECAO,DTNASCIMENTO,CPF,
            # CARTIDENTIDADE,GESTOR,CÓDIGO HCIS,UFCRM,LOGIN,DH_VALIDADE,
            # GPMEDICO,CLT/PJ/RPA,ESPECIALIDADE
            # após separado por vírgula, os textos podem ser lidos pelo índice: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
            # print("DRT"+linha[0]+"\n"+linha[1]+"\n"+linha[7]+"\n"+linha[6]+"\n"+linha[3]+"\n"+linha[4])
            # Chamar função para definir a Profissão
            codProfissao = profissao(linha[3])
            print("Profissão: ")
            print(codProfissao)
            # Chamar função para definir a Categoria profissional
            codCategoria = categoria(linha[3])
            print("Categoria: ")
            print(codCategoria)
            # Chamar função para definir o Tipo de Conselho Regional
            codConselho = tipoconselho(linha[3])
            print("Conselho: ")
            print(codConselho)
            if codProfissao == "MEDC":
                # Chamar função para definir o Grupo Medico
                codGrupoMedico = grupomedico(linha[14])
                print("Grupo Medico")
                print(codGrupoMedico)
                indPermIntern = "S"
                indPermAssLaudo = "s"
            contador += 1

            createFile.write("INSERT INTO FAPROCAD (cpf,crm,uf_crm,cod_ant,cod_pro_corp,cod_profissao,"
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
                             "('"+linha[7]+"','"+linha[4]+"','"+linha[11]+"','"+linha[10]+"','',"
                             "'"+codProfissao+"','','','','','','','N','"+codCategoria+"','S',"
                             "'04948970','ESTRADA DO M BOI MIRIM 4815','JARDIM ANGELA (ZONA SUL)','SAO PAULO','SP','5203',"
                             "NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'1158322500',NULL,'','','','','','',"
                             "NULL,NULL,NULL,NULL,NULL,NULL,'','','N','','','','S','N','N','N',0,'N',"
                             "'"+indPermIntern+"','"+indPermAssLaudo+"','N','S','','','','N','','"+linha[10]+"',"
                             "'"+linha[1]+"',To_Date('"+linha[6]+"', 'DD/MM/YYYY'),'N',NULL,'"+codGrupoMedico+"',"
                             "NULL,'IAUE','"+codConselho+"',NULL,NULL,NULL,885459,NULL);\n")
            if codProfissao == "MEDC":
                # Chamar função para definir o Especialidade Médica
                espMedica = especialidade(linha[14])
                print(espMedica)
                espinsert = ("INSERT INTO FAESPPRO (COD_PRO, COD_ESP, SN_PRINCIPAL) VALUES "
                             "('"+linha[10]+"','"+espMedica+"','S');\n")
                print(espinsert)
                createFile.write(espinsert)
        print(contador)
        createFile.close()
        readFile.close()
    elif op == 6:
        # ler arquivo fonte dos dados
        readFile = open("../usuarios.txt", "r")
        # criar o arquivo que armazenará as novas informações já tratadas
        createFile = open("../insert_medview.txt", "w")
        contador = 0
        # loop para ler linha por linha para manipulação
        for x in readFile:
            x = x.upper()
            # separar linhas por vírgula (','), transformando em variável do tipo list
            linha = x.split('	')
            contador += 1
            # CHAPA,NOME,ADMISSAO,CARGO,REGISTRO,SECAO,DTNASCIMENTO,
            # CPF,CARTIDENTIDADE,GESTOR,COD HCIS, UFCRM,LOGIN,DH_VALIDADE
            # após separado por vírgula, os textos podem ser lidos pelo índice: 0,1,2,3,4,5,6,7,8,9,10,11,12,13
            createFile.write("INSERT INTO FAUSUCAD (MATRICULA, APELIDO, NOME, IND_USUARIO_ATIVO, SN_USU_BLOQUEADO, "
                             "SN_LIBERAR_ACESSO, DH_VALIDADE, DT_HR_ULTIMA_SENHA, COD_BAR_USU, COD_PRO, SETOR, "
                             "FK_COD_SET, CPF, DH_NASCIMENTO, EMAIL, SN_ESTRANGEIRO, NU_DOC_ESTRANG, FK_PAIS) VALUES "
                             "('"+linha[0]+"', '"+linha[12]+"', '"+linha[1]+"', 'S', 'N', 'N', "
                             "To_Date('"+linha[13]+"', 'DD/MM/YYYY'), NULL, NULL, '"+linha[10]+"', NULL, '', "
                             "'"+linha[7]+"', To_Date('"+linha[6]+"', 'DD/MM/YYYY'), NULL, 'N', NULL, NULL);\n")

            atribui = atribuicaogrupo(linha[17])
            print(atribui)
            a = atribui.split(' ')
            print(len(a))
            if len(a) == 2:
                createFile.write("insert into faususis (sistema, cod_grupo, matricula) values "
                                 "('"+a[0]+"','"+a[1]+"','"+linha[0]+"');\n")
            elif len(a) == 4:
                createFile.write("insert into faususis (sistema, cod_grupo, matricula) values "
                                 "('"+a[0]+"','"+a[1]+"','"+linha[0]+"');\n")
                createFile.write("insert into faususis (sistema, cod_grupo, matricula) values "
                                 "('"+a[2]+"','"+a[3]+"','"+linha[0]+"');\n")
            elif len(a) == 6:
                createFile.write("insert into faususis (sistema, cod_grupo, matricula) values "
                                 "('"+a[0]+"','"+a[1]+"','"+linha[0]+"');\n")
                createFile.write("insert into faususis (sistema, cod_grupo, matricula) values "
                                 "('"+a[2]+"','"+a[3]+"','"+linha[0]+"');\n")
                createFile.write("insert into faususis (sistema, cod_grupo, matricula) values "
                                 "('"+a[4]+"','"+a[5]+"','"+linha[0]+"');\n")
            elif len(a) == 18:
                for atrx in range(0, 17, 2):
                    createFile.write("insert into faususis (sistema, cod_grupo, matricula) values "
                                     "('"+a[atrx]+"','"+a[atrx+1]+"','"+linha[0]+"');\n")
        print(contador)
        createFile.close()
        readFile.close()
#    except ValueError:
#        print("\nOops! Não foi informado um valor válido, tente novamente...\n\n")
#    break
