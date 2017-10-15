
import helper

#{"a" = 0," ":0 }
def Create_empty_unigram(fileName):
    file = open(
        fileName, "r", encoding="utf8")
    dictionairy = {}
    for line in file:
        for char in line:
            dictionairy[char] = 0
    return dictionairy

  #{"a" = 9," ":1000 }
def Count_unigram(fileName, emptyDictionary):
    file = open(
        fileName, "r", encoding="utf8")
    for line in file:
        for char in line:
            emptyDictionary[char] += 1
    return emptyDictionary

  #{"a" = 0.00001," ":0.3 }
def transform_Occurence_in_probabilist(fileName, OccurenceDictionary):
    for char in OccurenceDictionary:
        OccurenceDictionary[char] = OccurenceDictionary[char] / \
            Get_lengh_of_file(fileName)
    return OccurenceDictionary

def Get_lengh_of_file(fileName):
    total_charater = 0
    file = open(
        fileName, "r", encoding="utf8")
    for line in file:
        for char in line:
            total_charater += 1
    return total_charater


def proba_unigram(fileName):
  return transform_Occurence_in_probabilist(fileName,Count_unigram(fileName,Create_empty_unigram(fileName)))

