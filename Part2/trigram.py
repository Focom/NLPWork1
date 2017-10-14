import bigram
import unigram
import copy
import helper

fileName = "./detect_langue/corpus_entrainement/english-training.txt"

def count_empty_trigram(fileName):
  file = open(
        fileName, "r", encoding="utf8")
  dictionairy = {}
  for line in file:
      for i in range(0, len(line) - 2):
          dictionairy[line[i] + line[i + 1] + line[i + 2]] = 0
  return dictionairy

def count_trigram(fileName):
  emptyTrigram = count_empty_trigram(fileName)
  file = open(
      fileName, "r", encoding="utf8")
  for line in file:
      for i in range(0, len(line) - 2):
          emptyTrigram[line[i] + line[i + 1] + line[i + 2]] += 1
  return emptyTrigram

def create_empty_2d_trigram(fileName):
  countTrigram = count_trigram(fileName)
  empty_count_unigram = unigram.Create_empty_unigram(fileName)
  result = {}
  for key in countTrigram:
    result[key[0]+key[1]] = copy.deepcopy(empty_count_unigram)
  return result

def create_2d_trigram_count(fileName):
  empty2dTrigram = create_empty_2d_trigram(fileName)
  count3gram = copy.deepcopy(count_trigram(fileName))
  
  for key in empty2dTrigram:
    for key2 in empty2dTrigram[key]:
      try:
        empty2dTrigram[key][key2] = count3gram[key+key2]
      except KeyError:
        pass
  return empty2dTrigram

def create_proba_trigram(fileName):
  trigramCount2d = create_2d_trigram_count(fileName)
  bigramCount = copy.deepcopy(bigram.countBigram(fileName))
  trigramCount = copy.deepcopy(count_trigram(fileName))

  for key in trigramCount2d:
    for key2 in trigramCount2d[key]:
      try:
        trigramCount2d[key][key2] = trigramCount[key+key2]/bigramCount[key]
      except KeyError:
        pass
  return trigramCount2d


def proba_trigram(fileName):
  return create_proba_trigram(fileName)

# test = create_proba_trigram(fileName)
# helper.save_dic_to_file(test,"test")

