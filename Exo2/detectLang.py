import perplexite
import os, os.path
import copy
import helper
from distutils.util import strtobool
import sys


def create_pp_of_lang(code_lang):
  
  if(code_lang=="EN"):
    file_training = "./detect_langue/corpus_entrainement/english-training.txt"
  if(code_lang == "FR"):
    file_training = "./detect_langue/corpus_entrainement/french-training.txt"
  if(code_lang == "SP"):
    file_training = "./detect_langue/corpus_entrainement/espanol-training.txt"
  if(code_lang == "PO"):
    file_training = "./detect_langue/corpus_entrainement/portuguese-training.txt"

  onlyfiles = next(os.walk("./detect_langue/corpus_test"))[2]
  number_of_file = (len(onlyfiles))
  result ={}
  empty_pp_result = {"1":0,"2":0,"3":0}
  for i in range(1,number_of_file):
    result[str(i)] = copy.deepcopy(empty_pp_result)
  for file in result:
    for n in result[file]:
      result[file][n] = perplexite.calcPerplexite(int(n),file_training,"./detect_langue/corpus_test/test"+file+".txt")
  return result

def create_all_pp_and_save_to_disc():
  response = helper.query_yes_no("Vous allez generez les resultats, cela va prendre beaucoup de temps, êtes vous sur ?","no")
  if(response):
    pp_FR = create_pp_of_lang("FR")
    pp_EN = create_pp_of_lang("EN")
    pp_SP = create_pp_of_lang("SP")
    pp_PO = create_pp_of_lang("PO")

    helper.serialize_dico(pp_FR,"pp_FR")
    helper.serialize_dico(pp_EN,"pp_EN")
    helper.serialize_dico(pp_SP,"pp_SP")
    helper.serialize_dico(pp_PO,"pp_PO")
    print("Toutes les pp sont sauvegardé dans les fichiers bin, ne pas les supprimer :)")

def detect_language(fileNumber,n):
    # response = helper.query_yes_no("Avez vous generer les fichier binaire des modele nGram ?","yes")
    # if (response == False):
    #   create_all_pp_and_save_to_disc()
    # else:
  pp_FR = helper.open_serialized_dico("pp_FR")
  pp_EN = helper.open_serialized_dico("pp_EN")
  pp_SP = helper.open_serialized_dico("pp_SP")
  pp_PO = helper.open_serialized_dico("pp_PO")
  result = {"pp_FR":pp_FR[str(fileNumber)][str(n)],"pp_EN":pp_EN[str(fileNumber)][str(n)],"pp_SP":pp_SP[str(fileNumber)][str(n)],"pp_PO":pp_PO[str(fileNumber)][str(n)]}
  score = 99999999
  for key in result:
    if (result[key]<score):
      score = result[key]
      lang = key[3]+key[4]
  print("la langue:",lang,"le score:",score)
  return lang

detect_language(3,1)
detect_language(3,2)
detect_language(3,3)
