import unigram

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
def Transform_in_proba_bigram(filledBigramDictionary,fileName):
    unigram_count = unigram.Count_unigram(fileName, unigram.Create_empty_unigram(fileName))
    for tuple in filledBigramDictionary:
        first_char = tuple
        for char in filledBigramDictionary[tuple]:
            try:
                filledBigramDictionary[first_char][char] = filledBigramDictionary[first_char][char] / \
                    unigram_count[first_char]
            except ZeroDivisionError:
                filledBigramDictionary[first_char][char] = 0
    return filledBigramDictionary

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



def proba_bigram(fileName):
  return Transform_in_proba_bigram(Fill_bigram_dictionary(fileName, create_empty_bigram_dictionary(unigram.Create_empty_unigram(fileName))),fileName)
