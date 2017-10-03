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
    result = re.search(filePattern, goodLine)
    file.close()
    return result.group(2)
