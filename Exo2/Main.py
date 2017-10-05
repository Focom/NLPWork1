

# def gram():
    # total_charater = 0
    # file = open(
    #     "./detect_langue/corpus_entrainement/english-training.txt", "r", encoding="utf8")
    # dictionairy = {}
    # for line in file:
    #   for char in line:
    #     dictionairy[char] = 0
    #     total_charater +=1

    # filesecond  = open(
    #     "./detect_langue/corpus_entrainement/english-training.txt", "r", encoding="utf8")
    # for line in filesecond:
    #   for char in line:
    #     dictionairy[char]+=1
    # print ("Comptes des characteres")
    # print(dictionairy)
    # print(total_charater)

    # i = 0

    # for char in dictionairy:
    #   dictionairy[char] = dictionairy[char]/total_charater
    # print("Proba des charactere")
    # print(dictionairy)


# gram()

fileName = "./detect_langue/corpus_entrainement/english-training.txt"

def Create_empty_int_dictionary(fileName):
    file = open(
        fileName, "r", encoding="utf8")
    dictionairy = {}
    for line in file:
        for char in line:
            dictionairy[char] = 0
    return dictionairy


def Get_lengh_of_file(fileName):
    total_charater = 0
    file = open(
        fileName, "r", encoding="utf8")
    for line in file:
        for char in line:
            total_charater += 1
    return total_charater


def Create_occurence_dictionary(fileName, emptyDictionary):
    filesecond = open(
        "./detect_langue/corpus_entrainement/english-training.txt", "r", encoding="utf8")
    for line in filesecond:
        for char in line:
            emptyDictionary[char] += 1
    return emptyDictionary
    # print ("Comptes des characteres")
    # print(dictionairy)
    # print(total_charater)


def transform_Occurence_in_probabilist(fileName, OccurenceDictionary):
    for char in OccurenceDictionary:
        OccurenceDictionary[char] = OccurenceDictionary[char] / \
            Get_lengh_of_file(fileName)
    return OccurenceDictionary
    # print("Proba des charactere")
    # print(dictionairy)

def create_empty_bigram_dictionary(emptyDictionary):
  result = {}
  for char in emptyDictionary:
    result[char]=emptyDictionary.copy()
  return result

def fill_bigram_dictionary(emptyBigramDictionary):
  

# print(create_empty_bigram_dictionary(Create_empty_int_dictionary(fileName)))

