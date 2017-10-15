import unigram
import pickle
import sys

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
    test = unigram.Count_unigram(fileName, unigram.Create_empty_unigram(fileName))
    return len(test)

def save_dic_to_file(dic,namOfFile):
    text_file = open(namOfFile+".txt", "w", encoding="utf8")
    text_file.write(str(dic))
    text_file.close()

# Ajoute le token ¤ au modele ngram vide
def addUnk(n,gram,fileName):
    """
    ajout de tuple de nom unk
    remplir le tuple unk avec {a:0,....,unk:0}
    ajouter la clé unk:0 a la fin de chaque tuple
    """
    if(n==1):
        gram["¤"]=0
        return gram

    if(n==2):
        empty_uni = unigram.Create_empty_unigram(fileName)
        gram["¤"]=empty_uni
        for tuple in gram:
            gram[tuple]["¤"]=0
        return gram
    if(n==3):
        empty_unigram = unigram.Create_empty_unigram(fileName)
        empty_unigram["¤"] = 0
        compo = []
        for tuple in gram:
            gram[tuple]["¤"]=0

        gram["¤¤"]=0
        gram["¤¤"]=empty_unigram

        return gram

def serialize_dico(dico,NameFile):
    file1 = open(NameFile+".bin","wb")
    pickle.dump(dico,file1)
    file1.close()

def open_serialized_dico(NameFile):
    file2 = open(NameFile+".bin","rb")
    return pickle.load(file2)

def query_yes_no(question, default="yes"): # Copy pasted from Stack Overflow
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")