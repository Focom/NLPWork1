import helper
import unigram
import bigram
import trigram
import copy

fileName = "./detect_langue/corpus_entrainement/english-training.txt"


def laplace(k, n, gram, fileName):
    count_unigram = unigram.Count_unigram(fileName, unigram.Create_empty_unigram(fileName))
    v = len(count_unigram)+2 #Attention mettre à 1
    if(n==1):
        count_uni = unigram.Count_unigram(fileName,unigram.Create_empty_unigram(fileName))
        for key in gram:
            if(key == '¤'):
                gram[key]= (k)/(helper.char_in_file(fileName)+k*v)
            else:
                gram[key]= (count_uni[key]+k)/(helper.char_in_file(fileName)+k*v)
    
    if(n == 2):
        count_bigram = bigram.Fill_bigram_dictionary(
            fileName, bigram.create_empty_bigram_dictionary(unigram.Create_empty_unigram(fileName)))
        for table in gram:
            for key in gram[table]:
                if((table =='¤')):
                     gram[table][key] = (k) / (v*k)
                elif((table !='¤')&(key == '¤') ):
                    gram[table][key] = (0 + k) / (count_unigram[table] + v*k)
                
                else:
                   gram[table][key] = (count_bigram[table][key] + k) / (count_unigram[table] + v*k)

    if(n == 3):
        countTrigram = copy.deepcopy(trigram.count_trigram(fileName))
        countBigram = copy.deepcopy(bigram.countBigram(fileName))
        for key in gram:
            for key2 in gram[key]:
                if ((key2=='¤')& (key!='¤¤')):
                     gram[key][key2] = (0+ k) / (countBigram[key] + v*k)
                if((key2!='¤')&(key!='¤¤')):
                    try:
                        gram[key][key2] = (countTrigram[key+key2] + k) / (countBigram[key] + v*k)
                    except KeyError:
                        gram[key][key2] = (0+ k) / (countBigram[key] + v*k)
                if(key=='¤¤'):
                    gram[key][key2] = (0+ k) / (0 + v*k) 

    return gram


def lissage(n,fileName):

    if (n==3):
        d = 1/n
        trigram_prob = helper.addUnk(3,trigram.proba_trigram(fileName),fileName) 
        bigram_prob = helper.addUnk(2,bigram.proba_bigram(fileName),fileName) 
        unigram_prob = helper.addUnk(1,unigram.proba_unigram(fileName),fileName) 
        for table in trigram_prob: # Ajouter gestion de ¤
            for key in trigram_prob[table]:
                trigram_prob[table][key] = d*trigram_prob[table][key]+d*bigram_prob[table[1]][key]+d*unigram_prob[key]
                print(trigram_prob[table][key])
        return trigram_prob
    
    if (n==2):
        d = 1/n
        unigram_prob = helper.addUnk(1,unigram.proba_unigram(fileName),fileName)
        bigram_prob = helper.addUnk(2,bigram.proba_bigram(fileName),fileName) 
        for table in bigram_prob:
            for key in bigram_prob[table]:
                bigram_prob[table][key] = d*bigram[table][key]+d*unigram_prob[key]     
        return bigram_prob  


# test = laplace(1,3,helper.addUnk(3,trigram.proba_trigram(fileName),fileName),fileName)
# test = lissage(3,fileName)
# helper.save_dic_to_file(str(test),'test')
# print(helper.Calc_sum_line(test['A ']))