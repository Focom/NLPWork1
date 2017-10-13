def char_in_file(fileName):
    file = open(
        fileName, "r", encoding="utf8")
    result=0
    for line in file:
        for char in line:
            result +=1
    return result

  # return lengh of file
def Get_lengh_of_file(fileName):
    total_charater = 0
    file = open(
        fileName, "r", encoding="utf8")
    for line in file:
        for char in line:
            total_charater += 1
    return total_charater

  # calcule la somme de tous les elements du dictionaire
def Calc_sum_line(simpleDico):
    sum = 0
    for key in simpleDico:
        sum = sum + simpleDico[key]
    return sum

  # retourne V, soit le nombre de charactere du corpus
def count_token(fileName):
    test = Count_unigram(fileName, Create_empty_unigram(fileName))
    return len(test)

def save_dic_to_file(dic,namOfFile):
    text_file = open(namOfFile+".txt", "w", encoding="utf8")
    text_file.write(str(dic))
    text_file.close()