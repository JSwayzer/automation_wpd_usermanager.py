import re
import unicodedata
import unidecode
'''
x = 'Âlàn Roger Gomes Barbosa'
t = re.sub(r'a', 'b', 'banana')
y = re.sub(r'à', 'A', x)

print(t)
print(y)


def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError:  # unicode is a default on python 3
        pass

    text = unicodedata.normalize('NFD', text) \
        .encode('ascii', 'ignore') \
        .decode("utf-8")

    return str(text)


s = strip_accents('àéêöýhelloggggg')

print(s)

somestring = "àéêöhellokkkkk"

# convert plain text to utf-8
u = unicode(somestring, "utf-8")
# convert utf-8 to normal text
print(unidecode.unidecode(u))


accented_string = u'Málaga'
# accented_string is of type 'unicode'
# import unidecode
unaccented_string = unidecode.unidecode(accented_string)
# unaccented_string contains 'Malaga'and is of type 'str'
print(accented_string)

'''

with open("usuarios.txt", "r", encoding="utf8") as readFile:  # ler arquivo fonte dos dados
    with open("checar_usuario.txt", "w", encoding="utf8") as createFile:  # criar o arquivo que armazenará as novas informações já tratadas
        createFile.write(" where t1.nome in (")
        print("where t1.nome in (")

        # escrever nome:
        for x in readFile:  # loop para ler linha por linha para manipulação
            nome = x.upper()
            # nome = strip_accents(x)
            createFile.write("'"+nome+"',")
            print("'"+nome+"',", end=" ")
            # exit()
        createFile.write("'"+nome+"')")
