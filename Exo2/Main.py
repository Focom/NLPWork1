fileName = "./detect_langue/corpus_entrainement/english-training.txt"

import helper
import unigram
import bigram
import trigram

# Faire les gram
# Faire ajout ¤
# Faire lissage
# lire fenetre dans fichier
# trouver perplexiter sur fenetre
# sarreter au nombre limite de fenetre
def calcPerplexite(n,gram,fileName, laplace):

    # if(n==1):
    #     closeGram = unigram.proba_unigram
    #     openGram = helper.addUnk(1,closeGram,fileName)
    #     if(laplace == true):
    #         pass
    return None


test = helper.addUnk(3,trigram.proba_trigram(fileName),fileName)
helper.save_dic_to_file(test,"test")