fileName = "./detect_langue/corpus_entrainement/english-training.txt"


#{"a" = 0," ":0 }
def Create_empty_unigram(fileName):
    file = open(
        fileName, "r", encoding="utf8")
    dictionairy = {}
    for line in file:
        for char in line:
            dictionairy[char] = 0
    return dictionairy

# return lengh of file


def Get_lengh_of_file(fileName):
    total_charater = 0
    file = open(
        fileName, "r", encoding="utf8")
    for line in file:
        for char in line:
            total_charater += 1
    return total_charater

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

#{"a" = {"a":0, " ":0, ...}," ":{"a":0, " ":0, ...} }


def create_empty_bigram_dictionary(emptyDictionary):
    result = {}
    for char in emptyDictionary:
        result[char] = emptyDictionary.copy()
    return result

#{"a" = {"a":9, " ":5, ...}," ":{"a":3, " ":4, ...} }


# create occurence of bigram
def Fill_bigram_dictionary(fileName, emptyBigramDictionary):
    file = open(
        fileName, "r", encoding="utf8")
    for line in file:
        for i in range(0, len(line) - 1):
            emptyBigramDictionary[line[i]][line[i + 1]] += 1
    return emptyBigramDictionary

#{"a" = {"a":0.1, " ":0.2, ...}," ":{"a":0.002, " ":0.000, ...} }


def Transform_in_proba_bigram(filledBigramDictionary):
    unigram = Count_unigram(fileName, Create_empty_unigram(fileName))
    for tuple in filledBigramDictionary:
        first_char = tuple
        for char in filledBigramDictionary[tuple]:
            try:
                filledBigramDictionary[first_char][char] = filledBigramDictionary[first_char][char] / \
                    unigram[first_char]
            except ZeroDivisionError:
                filledBigramDictionary[first_char][char] = 0
    return filledBigramDictionary

# calcule la somme de tous les elements du dictionaire


def Calc_sum_line(simpleDico):
    sum = 0
    for key in simpleDico:
        sum = sum + simpleDico[key]
    return sum

#{"abc":0,", e":0, ...}


def Create_empty_trigram_count(fileName):
    file = open(
        fileName, "r", encoding="utf8")
    dictionairy = {}
    for line in file:
        for i in range(0, len(line) - 2):
            dictionairy[line[i] + line[i + 1] + line[i + 2]] = 0
    return dictionairy

#{"ab":{"A":0.43," ":0.001}," e":{"A":0.002," ":0.0032}}


def Create_2d_Trigram(trigramCount, fileName):
    file = open(
        fileName, "r", encoding="utf8")
    empty_int = Create_empty_unigram(fileName)
    count_bigram = countBigram(fileName)
    result = {}

    for key in trigramCount:
        result[key[0] + key[1]] = empty_int

    for key in result:
        for char in key:
            try:
                result[key][char] = trigramCount[key + char] / \
                    count_bigram[key]
            except KeyError:
                pass
    return result

#{"abc":5,", e":6, ...}


def Count_trigram(fileName, emptyTrigram):
    file = open(
        fileName, "r", encoding="utf8")
    for line in file:
        for i in range(0, len(line) - 2):
            emptyTrigram[line[i] + line[i + 1] + line[i + 2]] += 1
    return emptyTrigram


#{"A  ":2, "C,": 3}
def countBigram(fileName):
    file = open(
        fileName, "r", encoding="utf8")
    emptyBigram = {}
    for line in file:
        for i in range(0, len(line) - 2):
            emptyBigram[line[i] + line[i + 1]] = 0
    file = open(
        fileName, "r", encoding="utf8")
    for line in file:
        for i in range(0, len(line) - 2):
            emptyBigram[line[i] + line[i + 1]] += 1
    return emptyBigram


def laplace(n, fileName):

    result = {}
    count_unigram = Count_unigram(fileName, Create_empty_unigram(fileName))
    v = len(count_unigram)
    if(n == 2):
        result = create_empty_bigram_dictionary(Create_empty_unigram(fileName))
        conditional_count = Fill_bigram_dictionary(
            fileName, create_empty_bigram_dictionary(Create_empty_unigram(fileName)))
        for table in conditional_count:
            for key in table:
                result[table][key] = (conditional_count[table][key] + 1) / (count_unigram[table] + v)
                
                # result[table][key] = (conditional_count[table][key] + 1) / (count_unigram[table] + v)
    
    
    if(n == 3):
        result = Create_2d_Trigram(Count_trigram(fileName, Create_empty_trigram_count(fileName)),fileName)
        count_trigram = Count_trigram(fileName, Create_empty_trigram_count(fileName))
        count_bigram = countBigram(fileName)
        for table in result:
            for key in table:
                result[table][key] = (count_trigram[table + key] + 1) / (count_bigram[table] + v)

    return result

   # retourne V, soit le nombre de charactere du corpus


def count_token(fileName):
    test = Count_unigram(fileName, Create_empty_unigram(fileName))
    return len(test)


print(laplace(2, fileName))

# print(Transform_in_proba_bigram(Fill_bigram_dictionary(fileName, create_empty_bigram_dictionary(
#     Create_empty_unigram(fileName)))))
