fileName = "./detect_langue/corpus_entrainement/english-training.txt"

import helper
import unigram
import bigram
import trigram


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
        empty_uni = Create_empty_unigram(fileName)
        gram["¤"]=empty_uni
        for tuple in gram:
            gram[tuple]["¤"]=0
        return gram
    if(n==3):
        empty_unigram = Create_empty_unigram(fileName)
        empty_unigram["¤"] = 0
        compo = []
        for tuple in gram:
            gram[tuple]["¤"]=0

        gram["¤¤"]=0
        gram["¤¤"]=empty_unigram

        return gram


# Faire les gram
# Faire ajout ¤
# Faire lissage
# lire fenetre dans fichier
# trouver perplexiter sur fenetre
# sarreter au nombre limite de fenetre
def calcPerplexite(n,gram,fileName, laplace):

    if(n==1):
        closeGram = proba_unigram
        openGram = addUnk(1,closeGram,fileName)
        if(laplace == true):
            pass
    return None


trigram = trigram.proba_trigram(fileName)
# sum=0
# for tuple in trigram:
#     print(helper.Calc_sum_line(trigram[tuple]))


text_file = open("Output.txt", "w", encoding="utf8")
text_file.write(str(trigram))
text_file.close()


# gram = addUnk(3, proba_trigram(fileName),fileName)
# goodgram = laplace(1,3,gram,fileName)

# text_file = open("Output.txt", "w",encoding="utf8")
# text_file.write(str(goodgram))
# text_file.close()
