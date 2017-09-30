import re


def findAnthem(fileName):
    memory = []
    i = 0

    pattern_all_file = re.compile("playAnthem")
    country_file = open("./factbook/geos/" + fileName, "r", encoding="utf8")

    for line in country_file:
        memory.insert(i, line)
        i = i + 1
        test = pattern_all_file.search(line)
        if test:
            break
    good_line = memory[-6]

    # print(good_line)
    pattern_good_line = re.compile("(;\">)(.*)(<\/span>)")
    result = pattern_good_line.search(good_line)
    country_file.close()
    return result.group(2)


def findLiterracy(fileName):
    memory = []
    i = 0
    j = 0
    condition_met = False

    pattern_all_file = re.compile("age 15 and over can read and write")
    country_file = open("./factbook/geos/" + fileName, "r", encoding="utf8")

    for line in country_file:
        if (condition_met):
            memory.insert(i, line)
            j = j + 1
            if(j == 7):
                break
        else:
            memory.insert(i, line)
            i = i + 1
            test = pattern_all_file.search(line)
            if test:
                condition_met = True
    good_line = memory[-7]
    pattern_good_line = re.compile("(;\">)(.*)(<\/span)")
    result = pattern_good_line.search(good_line)
    return result.group(2)
