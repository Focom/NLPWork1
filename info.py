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
    country_file.close()
    return result.group(2)


def findExport(fileName):
    memory = []
    i = 0
    j = 0
    condition_met = False

    pattern_all_file = re.compile("<a href=\"../fields/2078.html")
    country_file = open("./factbook/geos/" + fileName, "r", encoding="utf8")

    for line in country_file:
        if (condition_met):
            memory.insert(i, line)
            j = j + 1
            if(j == 9):
                break
        else:
            memory.insert(i, line)
            i = i + 1
            test = pattern_all_file.search(line)
            if test:
                condition_met = True
    good_line = memory[-9]
    pattern_good_line = re.compile("(\">)(.*)(<\/div)")
    result = pattern_good_line.search(good_line)
    country_file.close()
    return result.group(2)


def findGdpGrowth(fileName):
    memory = []
    i = 0
    j = 0
    condition_met = False

    pattern_all_file = re.compile("GDP - real growth rate:")
    country_file = open("./factbook/geos/" + fileName, "r", encoding="utf8")

    for line in country_file:
        if (condition_met):
            memory.insert(i, line)
            j = j + 1
            if(j == 17):
                break
        else:
            memory.insert(i, line)
            i = i + 1
            test = pattern_all_file.search(line)
            if test:
                condition_met = True
    good_line = memory[-17]
    pattern_good_line = re.compile("(\">)(.*)(<\/div)")
    result = pattern_good_line.search(good_line)
    country_file.close()
    return result.group(2)


def findGdpPerCapita(fileName):
    memory = []
    i = 0
    j = 0
    condition_met = False

    pattern_all_file = re.compile(
        "Notes and Definitions: GDP - per capita \(PPP\)")
    country_file = open("./factbook/geos/" + fileName, "r", encoding="utf8")

    for line in country_file:
        if (condition_met):
            memory.insert(i, line)
            j = j + 1
            if(j == 17):
                break
        else:
            memory.insert(i, line)
            i = i + 1
            test = pattern_all_file.search(line)
            if test:
                condition_met = True
    good_line = memory[-17]
    pattern_good_line = re.compile("(\">)(.*)(<\/div)")
    result = pattern_good_line.search(good_line)
    country_file.close()
    return result.group(2)


def findHazard(fileName):
    memory = []
    i = 0
    j = 0
    condition_met = False

    pattern_all_file = re.compile("hazards")
    country_file = open("./factbook/geos/" + fileName, "r", encoding="utf8")

    for line in country_file:
        if (condition_met):
            memory.insert(i, line)
            j = j + 1
            if(j == 150):
                break
        else:
            memory.insert(i, line)
            i = i + 1
            test = pattern_all_file.search(line)
            if test:
                condition_met = True

    size_memory = len(memory)
    starting_number = size_memory - 150
    hazard_pattern1 = re.compile(".[wW]ind.")
    hazard_pattern2 = re.compile(".[Hh]urricanes.")
    hazard_pattern3 = re.compile(".[Cc]yclone.")
    hazard_pattern4 = re.compile(".[Tt]yphoons.")
    hazard_pattern5 = re.compile(".[Aa]ir.")

    result = False

    while starting_number < size_memory:
        test1 = hazard_pattern1.search(memory[starting_number])
        test2 = hazard_pattern2.search(memory[starting_number])
        test3 = hazard_pattern3.search(memory[starting_number])
        test4 = hazard_pattern4.search(memory[starting_number])
        test5 = hazard_pattern5.search(memory[starting_number])

        starting_number = starting_number + 1
        if(test1):
            result = True
            break
        if(test2):
            result = True
            break
        if(test3):
            result = True
            break
        if(test4):
            result = True
            break
        if(test5):
            result = True
            break
    country_file.close()    
    return result
