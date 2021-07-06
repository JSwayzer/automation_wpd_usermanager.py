import re


def acento(string, pattern):
    result = re.search(pattern, string)
    if result is not None:
        return result.group()


readFile = open("../desligamentos.txt", "r")
contador = 0
for x in readFile:
    contador += 1
    x = x.upper()
    if acento(x, "Á") == "Á":
        print(1)
