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


def transform_Occurence_in_probabilist(fileName, OccurenceDictionary):
    for char in OccurenceDictionary:
        OccurenceDictionary[char] = OccurenceDictionary[char] / \
            Get_lengh_of_file(fileName)
    return OccurenceDictionary


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


def Transform_in_proba_bigram(filledBigramDictionary):
    unigram = Create_occurence_dictionary(fileName,Create_empty_int_dictionary(fileName))
    for tuple in filledBigramDictionary:
        first_char = tuple
        for char in filledBigramDictionary[tuple]:
            try:
                filledBigramDictionary[first_char][char]= filledBigramDictionary[first_char][char]/unigram[first_char]
            except ZeroDivisionError:
                filledBigramDictionary[first_char][char] = 0
    return filledBigramDictionary

def Calc_sum_line(simpleDico):
    sum = 0
    for key in simpleDico:
        sum = sum + simpleDico[key]
    return sum

def Create_empty_trigram(fileName):
    file = open(
       fileName, "r", encoding="utf8")
    dictionairy = {}
    for line in file:
        for i in range(0,len(line)-2):
            dictionairy[line[i]+line[i+1]+line[i+2]] = 0
    return dictionairy

def Count_trigram(fileName,emptyTrigram):
    file = open(
       fileName, "r", encoding="utf8")
    for line in file:
        for i in range(0,len(line)-2):
            emptyTrigram[line[i]+line[i+1]+line[i+2]]+=1
    return emptyTrigram

# def Add_unigram_to_trigram(emptyTrygram):   Sert a rien
#     unigram = Create_empty_int_dictionary(fileName).copy()
#     for key in emptyTrygram:
#         emptyTrygram[key]=unigram
#     return emptyTrygram


print(Count_trigram(fileName,Create_empty_trigram(fileName)))


# print(Transform_in_proba_bigram(Fill_bigram_dictionary(fileName, create_empty_bigram_dictionary(
#     Create_empty_int_dictionary(fileName)))))
