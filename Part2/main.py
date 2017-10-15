import detectLang
import graph

# ====================================================================================================
# La detection est rapide car toute les perplexites sont stockées dans les fichiers binaires pp_EN etc
# Pour regénerer les fichiers :
# Executer detectLang.create_all_pp_and_save_to_disc(), décommenter la ligne suivante
# detectLang.create_all_pp_and_save_to_disc()
# Les resultats des perplexités pour tous les fichiers seront serialisés dans les fichiers binaires.
# ces fichiers sont necessaire à la fontions detectLang.detect_language()
# Pour serialisé les dictionaires j'utilise la bibliotheque intégrer à python => pickle
# ====================================================================================================

test_file_number = 13

# detect_language(Numéro du fichier dans le repertoire de test, N du modele nGram)
# Print le code de la langue reconnue et la perplexité du modèle choisis.
detectLang.detect_language(test_file_number,1)
detectLang.detect_language(test_file_number,2)
detectLang.detect_language(test_file_number,3)

# ====================================================================================================
# Nécessite matplotlib
# Installé matplotlib avec => pip install matplotlib
# ====================================================================================================

# Affiche sur un graphique les perplexité de tous les modeles sur un même fichier
graph.graphFile(test_file_number)

# Pour donner le résultat sur tous les fichier test dans la console
# detectLang.show_all_result()
