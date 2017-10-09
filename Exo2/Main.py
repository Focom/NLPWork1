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

def proba_unigram(fileName):
    return transform_Occurence_in_probabilist(fileName,Count_unigram(fileName,Create_empty_unigram(fileName)))

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

def proba_bigram(fileName):
    return Transform_in_proba_bigram(Fill_bigram_dictionary(fileName, create_empty_bigram_dictionary(Create_empty_unigram(fileName))))

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
            if ((key=="A ") & (char=="c" )):
                print(trigramCount[key + char] / count_bigram[key])
                break
            try:
                result[key][char] = trigramCount[key + char] / count_bigram[key]
            except KeyError:
                pass
    return result

def proba_trigram(fileName):
    return Create_2d_Trigram(Count_trigram(fileName,Create_empty_trigram_count(fileName)),fileName)

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


def laplace(k, n, fileName):

    result = {}
    count_unigram = Count_unigram(fileName, Create_empty_unigram(fileName))
    v = len(count_unigram)
    if(n == 2):
        result = create_empty_bigram_dictionary(Create_empty_unigram(fileName))
        conditional_count = Fill_bigram_dictionary(
            fileName, create_empty_bigram_dictionary(Create_empty_unigram(fileName)))
        # return conditional_count
        for table in conditional_count:
            for key in conditional_count[table]:
                # print("table:",table," key:",key)
                result[table][key] = (conditional_count[table][key] + k) / (count_unigram[table] + v*k)

    if(n == 3):
        result = Create_2d_Trigram(Count_trigram(fileName, Create_empty_trigram_count(fileName)),fileName)
        count_trigram = Count_trigram(fileName, Create_empty_trigram_count(fileName))
        count_bigram = countBigram(fileName)
        for table in result:
            for key in result[table]:
                try:
                    result[table][key] = (count_trigram[table+key] + k) / (count_bigram[table] + v*k)
                except KeyError:
                    result[table][key] =  1 / (count_bigram[table] + v)
    return result

# retourne V, soit le nombre de charactere du corpus
def count_token(fileName):
    test = Count_unigram(fileName, Create_empty_unigram(fileName))
    return len(test)

def lissage(n,fileName):
    print("\n")
    print("n: ",n)
    print("##########################################################################################")
    if (n==3):
        d = 1/n
        trigram = proba_trigram(fileName)
        bigram = proba_bigram(fileName)
        unigram = proba_unigram(fileName)
        for table in trigram:
            for key in trigram[table]:
                trigram[table][key] = d*trigram[table][key]+d*bigram[table[1]][key]+d*unigram[key]
                # if ((table=="A ") & (key=="c" )):
                #     print("les clés: ",table,key)
                #     print("uni: ",unigram[key])
                #     print("bigram: ",bigram[table[1]][key])
                #     print("Trigram: ",trigram[table][key])
                #     print(d*trigram[table][key]+d*bigram[table[1]][key]+d*unigram[key])
                    # return None
        return trigram
    if (n==2):
        d = 1/n
        unigram = proba_unigram(fileName)
        bigram = proba_bigram(fileName)
        for table in bigram:
            for key in bigram[table]:
                bigram[table][key] = d*bigram[table][key]+d*unigram[key]     
        return bigram  

# print(proba_unigram(fileName))

def perplexite(n,gram,fileName):
    result=[]
    testFile = open(
        fileName, "r", encoding="utf8")
    lineToCalculate={}
    charToAnalyse = ""
    for line in textFile:
        for i in range(0,len(line)):
           
            if (n==1):
                return None
            if (n==2):
                lineToCalculate = gram[line[i]]
                charToAnalyse = line[i]
            # if(n==3):
                # lineToCalculate = gram[[line[i]+Line[i+1]]
                # charToAnalyse = line[i+1]
            # result.append("a")

    return None

def addUnk(n,gram,fileName):
    unk = {}
    """
    ajout de tuple de nom unk
    remplir le tuple unk avec {a:0,....,unk:0}
    ajouter la clé unk:0 a la fin de chaque tuple
    """
    if(n==2):
        unk = Create_empty_unigram(fileName)
        gram["¤"]=unk
        for tuple in gram:
            gram[tuple]["¤"]=0
        return gram
    if(n==3):
        empty_unigram = Create_empty_unigram(fileName)
        empty_unigram["¤"] = 0
        compo = []
        # print(empty_unigram)
        for key in empty_unigram: # On creer les compos
            compo.append("¤"+key)
            compo.append(key+"¤")
        
            for tuple in gram: # Aujoute toutes les compos aux autres lignes
                for combi in compo:
                    gram[tuple][combi]=0

        for combi in compo:
            gram[combi]=empty_unigram
        print (gram)
        return None

def calcPerplexite(dic):
    result = 0
    proba = []
    for key in dic:
        proba.append(dic[key])
    
    # for p in proba:

    return result


print(addUnk(3,proba_trigram(fileName),fileName))


# lissage(3,fileName)
# print(countBigram(fileName)["A "])
# print(Count_trigram(fileName,Create_empty_trigram_count(fileName))["A c"])
# proba_trigram(fileName)
# for table in lissage(3,fileName):
#     print(Calc_sum_line(table))