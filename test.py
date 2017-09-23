# p1 * p2 = exp(log(p1)+log(p2))

import re

file = open("./factbook/index.html","r",encoding="utf8")
paysPattern = re.compile("France")

for line in file:
    test = paysPattern.search(line)
    if(test):
        print("trouver")
        goodLine = line
        break
file.close()
print(goodLine)

filePattern = re.compile("(geos\/)(..\.html)")

''' rechereche pays sur la ligne 
extract de la ligne
optention du code pays
ouverture du bon fichier html '''

file.close()