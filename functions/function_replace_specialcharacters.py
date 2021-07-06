# import re
import unicodedata
import unidecode

def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError:  # unicode is a default on python 3
        pass

    text = unicodedata.normalize('NFD', text) \
        .encode('ascii', 'ignore') \
        .decode("utf-8")

    return str(text)


# s = strip_accents('àéêöýhelloggggg')
#
# print(s)

'''def pro(string, pattern):
    result = re.search(pattern, string)
    if result is not None:
        return result.group()


def speca(spc):
    re.sub(r'á', 'A', spc)
    re.sub(r'à', 'A', spc)

    if pro(spc, "á") == "á" \
            or pro(spc, "à") == "à" \
            or pro(spc, "ã") == "ã" \
            or pro(spc, "â") == "â" \
            or pro(spc, "ä") == "ä":
        return "A"

    elif pro(spc, "é") == "é" \
            or pro(spc, "è") == "è" \
            or pro(spc, "ë") == "ë" \
            or pro(spc, "ê") == "ê":
        return "E"

    elif pro(spc, "í") == "í" \
            or pro(spc, "ì") == "ì" \
            or pro(spc, "î") == "î" \
            or pro(spc, "ï") == "ï":
        return "I"

    elif pro(spc, "ó") == "ó" \
            or pro(spc, "ò") == "ò" \
            or pro(spc, "õ") == "õ" \
            or pro(spc, "ô") == "ô" \
            or pro(spc, "ö") == "ö":
        return "O"

    elif pro(spc, "ú") == "ú" \
            or pro(spc, "ù") == "ù" \
            or pro(spc, "û") == "û" \
            or pro(spc, "ü") == "ü":
        return "U"

    elif pro(spc, "ç") == "ç":
        return "Ç"

    elif pro(spc, "ý") == "ý`" \
            or pro(spc, "ÿ") == "ÿ":
        return "Y"

    elif pro(spc, "’") == "’":
        return ""
'''
