import helper
import unigram
import bigram
import trigram

def laplace(k, n, gram, fileName):
    result = {}
    count_unigram = unigram.Count_unigram(fileName, unigram.Create_empty_unigram(fileName))
    v = len(count_unigram)+2 #Attention mettre à 1
    print (v)
    if(n==1):
        count_uni = unigram.Count_unigram(fileName,unigram.Create_empty_unigram(fileName))
        for key in gram:
            if(key == '¤'):
                gram[key]= (k)/(helper.char_in_file(fileName)+k*v)
            else:
                gram[key]= (count_uni[key]+k)/(helper.char_in_file(fileName)+k*v)
    
    if(n == 2):
        result = bigram.create_empty_bigram_dictionary(unigram.Create_empty_unigram(fileName))
        count_bigram = bigram.Fill_bigram_dictionary(
            fileName, bigram.create_empty_bigram_dictionary(unigram.Create_empty_unigram(fileName)))
        # return count_bigram
        for table in gram:
            for key in gram[table]:
                if((table =='¤')):
                     gram[table][key] = (k) / (v*k)
                elif((table !='¤')&(key == '¤') ):
                    gram[table][key] = (0 + k) / (count_unigram[table] + v*k)
                
                else:
                    # print("table:",table," key:",key)
                    
                    gram[table][key] = (count_bigram[table][key] + k) / (count_unigram[table] + v*k)

    if(n == 3):
        result = trigram.Create_2d_Trigram(trigram.Count_trigram(fileName, trigram.Create_empty_trigram_count(fileName)),fileName)
        count_trigram = trigram.Count_trigram(fileName, trigram.Create_empty_trigram_count(fileName))
        count_bigram = bigram.countBigram(fileName)
        print(gram)
        for table in gram:
            for key in gram[table]: 
                if (table=="¤¤"): #"¤¤¤" "¤¤A"
                    gram[table][key] = (k) / (v*k)

                elif(gram[table][key]==0):
                    gram[table][key] = (0+ k) / (count_bigram[table] + v*k)
                else: 
                    print(gram[table][key])                       
                    gram[table][key] = (count_trigram[table+key] + k) / (count_bigram[table] + v*k)
    return gram


def lissage(n,fileName):
    print("\n")
    print("n: ",n)
    print("##########################################################################################")
    if (n==3):
        d = 1/n
        trigram_prob = trigram.proba_trigram(fileName)
        bigram_prob = bigram.proba_bigram(fileName)
        unigram_prob = unigram.proba_unigram(fileName)
        for table in trigram_prob:
            for key in trigram_prob[table]:
                trigram_prob[table][key] = d*trigram_prob[table][key]+d*bigram_prob[table[1]][key]+d*unigram_prob[key]
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
        unigram_prob = unigram.proba_unigram(fileName)
        bigram_prob = bigram.proba_bigram(fileName)
        for table in bigram_prob:
            for key in bigram_prob[table]:
                bigram_prob[table][key] = d*bigram[table][key]+d*unigram_prob[key]     
        return bigram  