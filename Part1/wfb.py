import file
import info
import csv


def get_wfb_info(pays, attribut):
    fileName = file.findFile(pays)
    if(attribut == "NATIONAL_ANTHEM"):
        return info.findAnthem(fileName)

    if(attribut == "LITERACY"):
        return info.findLiterracy(fileName)

    if(attribut == "EXPORTS"):
        return info.findExport(fileName)

    if(attribut == "GDP_REAL_GROWTH_RATE"):
        return info.findGdpGrowth(fileName)

    if(attribut == "GDP_PER_CAPITA"):
        return info.findGdpPerCapita(fileName)

    if(attribut == "NATURAL_HAZARDS"):
        return info.findHazard(fileName)

    if(attribut == "EXECUTIVE_BRANCH"):
        return info.findExecutive(fileName)

    if(attribut == "DIPLOMATIC_REPRESENTATION_FROM_US"):
        return info.findDiplomacy(fileName)


def get_info_csv():
    result = []
    table = []
    i = 0
    k = 0
    with open('wfb_test.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            result.append(row)
    return result


def test_work(correct_table):
    i = 0
    correct = 0
    bad = 0
    attribut = ""
    for answer in correct_table:
        pays = answer[0]

        if(attribut != answer[1]):
            attribut = answer[1]

        correction = answer[2]
        own_result = get_wfb_info(pays, attribut)
        if (correction == own_result):
            correct += 1
        else:
            bad += 1
    precision = (correct)/(correct+bad)*100
    return "Taux de précision avec le CSV de test: "+str(precision)+"%"

print(test_work(get_info_csv()))
# print(get_wfb_info("United Kingdom","DIPLOMATIC_REPRESENTATION_FROM_US"))
