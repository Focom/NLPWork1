import detectLang
import graph

# ====================================================================================================
# La detection est rapide car toute les perplexites sont stockées dans les fichiers binaires pp_EN etc
# Pour regénerer les fichiers :
# Executer detectLang.create_all_pp_and_save_to_disc()
# Les resultats des perplexités pour tous les fichiers seront serialisés dans les fichiers binaires.
# ces fichiers sont necessaire à la fontions detectLang.detect_language()
# Pour serialisé les dictionaires j'utilise la bibliotheque intégrer à python => pickle
# ====================================================================================================

test_file_number = 19

# detect_language(Numéro du fichier dans le repertoire de test, N du modele nGram)
# Print le code de la langue reconnue et la perplexité du modèle choisis.
detectLang.detect_language(test_file_number,1)
detectLang.detect_language(test_file_number,2)
detectLang.detect_language(test_file_number,3)

# ====================================================================================================
# Nécessite matplotlib
# Installé matplotlib avec => pip install matplotlib
# ====================================================================================================

# graphFile(Numéro du fichier dans le repertoire de test)
graph.graphFile(test_file_number)

