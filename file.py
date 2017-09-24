import re


def findFile(country):
    file = open("./factbook/index.html", "r", encoding="utf8")
    paysPattern = re.compile(country)

    for line in file:
        test = paysPattern.search(line)
        if(test):
            goodLine = line
            break
    file.close()

    filePattern = re.compile("(geos\/)(..\.html)")

    m = re.search(filePattern, goodLine)

    ''' rechereche pays sur la ligne 
  extract de la ligne
  optention du code pays
  ouverture du bon fichier html '''

    file.close()
    return m.group(2)
