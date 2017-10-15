import matplotlib.pyplot as plt
import helper

pp_FR = helper.open_serialized_dico("pp_FR")
pp_EN = helper.open_serialized_dico("pp_EN")
pp_SP = helper.open_serialized_dico("pp_SP")
pp_PO = helper.open_serialized_dico("pp_PO")

def graphFile(fileNumber):
  x = [1,2,3]
  FR_PP = [pp_FR[str(fileNumber)][str(1)],pp_FR[str(fileNumber)][str(2)],pp_FR[str(fileNumber)][str(3)]]
  EN_PP = [pp_EN[str(fileNumber)][str(1)],pp_EN[str(fileNumber)][str(2)],pp_EN[str(fileNumber)][str(3)]]
  SP_PP = [pp_SP[str(fileNumber)][str(1)],pp_SP[str(fileNumber)][str(2)],pp_SP[str(fileNumber)][str(3)]]
  PO_PP = [pp_PO[str(fileNumber)][str(1)],pp_PO[str(fileNumber)][str(2)],pp_PO[str(fileNumber)][str(3)]]
  
  plt.plot(x,FR_PP,label='Francais')
  plt.plot(x,EN_PP,label='Anglais')
  plt.plot(x,SP_PP,label="Espagnol")
  plt.plot(x,PO_PP,label="Portuguais")
  plt.title('PP de '+'test'+str(fileNumber)+'.txt'+' en fonction du modèle de langue')
  plt.ylabel('Perplexité')
  plt.xlabel('Modele N gram (1, 2, 3)')
  plt.legend()
  plt.show()

# graphFile(14)

