import helper
import unigram
import bigram
import trigram
import lissage
import math

# Faire les gram
# Faire ajout ¤
# Faire lissage
# lire fenetre dans fichier
# gerer cas des ¤
# trouver perplexiter sur fenetre
# sarreter au nombre limite de fenetre
def calcPerplexite(n,fileTraining,fileTest):

    if(n==1):
        proba = []
        n = 0
        sum = 0
        result = 0
        closeGram = unigram.proba_unigram(fileTraining)
        openGram = helper.addUnk(1,closeGram,fileTraining)
        smoothedGram = lissage.laplace(1,1,openGram,fileTraining)
        file = open(
        fileTest, "r", encoding="utf8")
        for line in file:
          for i in range(0,len(line)):
            try:
              proba.append(smoothedGram[line[i]])
            except KeyError:
              proba.append(smoothedGram["¤"])
            n +=1
        for p in proba:
          sum+=math.log(p)
        result = (-1/n)*sum
        result = math.exp(result)
    
    if (n==2):
        proba = []
        n = 0
        sum = 0
        result = 0
        closeGram = bigram.proba_bigram(fileTraining)
        openGram = helper.addUnk(2,closeGram,fileTraining)
        smoothedGram = lissage.laplace(1,2,openGram,fileTraining)
        file = open(
        fileTest, "r", encoding="utf8")
        for line in file:
          for i in range(0,len(line)-1):
            try:
              proba.append(smoothedGram[line[i]][line[i+1]])
              n +=1
            except KeyError:
              try:
                proba.append(smoothedGram[line[i]]["¤"])
                n+=1
              except KeyError:
                proba.append(smoothedGram["¤"]["¤"])
                n+=1
        for p in proba:
          sum+=math.log(p)
        result = (-1/n)*sum
        result = math.exp(result)

  
    if(n==3):
      proba = []
      n = 0
      sum = 0
      result = 0
      closeGram = trigram.proba_trigram(fileTraining)
      openGram = helper.addUnk(3,closeGram,fileTraining)
      smoothedGram = lissage.laplace(1,3,openGram,fileTraining)
      helper.save_dic_to_file(smoothedGram,'smoothedgram')
      file = open(
        fileTest, "r", encoding="utf8")
      for line in file:
        for i in range(0,len(line)-2):
          try:
              proba.append(smoothedGram[line[i]+line[i+1]][line[i+2]])
              n +=1
          except KeyError:
            try:
              proba.append(smoothedGram[line[i]+line[i+1]]["¤"])
              n+=1
            except KeyError:
              proba.append(smoothedGram["¤¤"]["¤"])
              n+=1
      for p in proba:
          sum+=math.log(p)
      result = (-1/n)*sum
      result = math.exp(result)
    return result

fileTraining = "./detect_langue/corpus_entrainement/english-training.txt"
fileTest = "./detect_langue/corpus_test/test4.txt"

print(calcPerplexite(3,fileTraining,fileTest))

# test = helper.addUnk(3,trigram.proba_trigram(fileName),fileName)
# helper.save_dic_to_file(test,"test")