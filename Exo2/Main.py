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
    file = open(
        fileName, "r", encoding="utf8")
    for line in file:
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
        result[char] = emptyDictionary.copy()
    return result


def Fill_bigram_dictionary(fileName, emptyBigramDictionary):
    file = open(
       fileName, "r", encoding="utf8")
    for line in file:
        for i in range(0, len(line) - 1):
            emptyBigramDictionary[line[i]][line[i + 1]] += 1
    return emptyBigramDictionary
# print(create_empty_bigram_dictionary(Create_empty_int_dictionary(fileName)))

def Transform_in_proba_bigram(filledBigramDictionary):
  for tuple in filledBigramDictionary:
    firstChar = tuple
    for char in tuple:
      filledBigramDictionary[firstChar][char]= filledBigramDictionary[firstChar][char]/Calc_sum_line(tuple)
  return filledBigramDictionary

def Calc_sum_line(simpleDico):
  sum = 0
  for key in simpleDico:
    sum += simpleDico[key]
  return sum


print(Transform_in_proba_bigram(Fill_bigram_dictionary(fileName, create_empty_bigram_dictionary(
    Create_empty_int_dictionary(fileName)))))
