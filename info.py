import re


def findAnthem(fileName):
    memory = []
    i = 0

    pattern_all_file = re.compile("<span class=\"category_data\" style=\"font-weight:normal; vertical-align:bottom;\">\"")
    country_file = open("./factbook/geos/" + fileName, "r", encoding="utf8")

    for line in country_file:
        i = i + 1
        test = pattern_all_file.search(line)
        if test:
            good_line = line
            break

    # print(good_line)
    pattern_good_line = re.compile("(;\">)(.*)(<\/span>)")
    result = pattern_good_line.search(good_line)
    raw_result = result.group(2)
    pattern_non_english = re.compile("(\".*\")( )(\()(.*)(\))")
    pattern_english = re.compile("(\")(.*)(\")")
    result_non_english = pattern_non_english.search(raw_result)
    result_english = pattern_english.search(raw_result)
    country_file.close()
    if(result_non_english):
        return result_non_english.group(4)
    if(result_english):
        return result_english.group(2)
    return raw_result


def findLiterracy(fileName):
    memory = []
    i = 0
    j = 0
    condition_met = False

    pattern_all_file = re.compile("age 15 and over")
    country_file = open("./factbook/geos/" + fileName, "r", encoding="utf8")

    for line in country_file:
        if (condition_met):
            memory.insert(i, line)
            j = j + 1
            if(j == 12):
                break
        else:
            memory.insert(i, line)
            i = i + 1
            test = pattern_all_file.search(line)
            if test:
                condition_met = True
    good_line = memory[-12]
    pattern_good_line = re.compile("(;\">)(.*)( <\/span)")
    result = pattern_good_line.search(good_line)
    country_file.close()
    return result.group(2)


def findExport(fileName):
    memory = []
    i = 0
    j = 0
    condition_met = False
    cond_virgule = False

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
    raw_result = pattern_good_line.search(
        good_line).group(2)  # 566 billion (est 2013)
    pattern_money = re.compile("(\$)(\d*.*)( .*ion)")
    clean_result = pattern_money.search(raw_result)

    sum = clean_result.group(2)
    float_sum = float(sum)
    money_adj = clean_result.group(3)

    million = 1000000
    billion = 1000000000
    trillion = 1000000000000

    money_adj = pattern_money.search(clean_result.group(0)).group(3)
    if(money_adj == " million"):
        result = float_sum * million
    if(money_adj == " billion"):
        result = float_sum * billion
    if(money_adj == " trillion"):
        result = float_sum * trillion

    country_file.close()
    return "$" + str(int(result))


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
    raw_result = result.group(2)
    pattern_percent = re.compile("(.*%)")
    end_result = pattern_percent.search(raw_result)
    return end_result.group(1)


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
    pattern_raw_result = re.compile("(\">)(.*)(<\/div)")
    pattern_result = re.compile("(\$)(\d*,\d*)")
    raw_result = pattern_raw_result.search(good_line).group(2)
    result = pattern_result.search(raw_result).group(2)
    country_file.close()

    list_of_output = ["$"]
    for letter in result:
        if(letter != ","):
            list_of_output.append(letter)

    result_clean = "".join(list_of_output)
    return result_clean


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
    hazard_pattern2 = re.compile(".[Hh]urricane.")
    hazard_pattern3 = re.compile(".[Cc]yclone.")
    hazard_pattern4 = re.compile(".[Tt]yphoon.")

    result = False

    while starting_number < size_memory:
        test1 = hazard_pattern1.search(memory[starting_number])
        test2 = hazard_pattern2.search(memory[starting_number])
        test3 = hazard_pattern3.search(memory[starting_number])
        test4 = hazard_pattern4.search(memory[starting_number])

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
    country_file.close()
    if (result):
        return "YES"
    else:
        return "NO"


def findExecutive(fileName):

    memory = []
    i = 0
    Title = ""
    condition_met = False

    pattern_all_file = re.compile("[chief|head] of state:")
    pattern_span = re.compile("(;\">)(.*)(</span>)")
    country_file = open("./factbook/geos/" + fileName, "r", encoding="utf8")

    for line in country_file:
        if (condition_met):
            memory.insert(i, line)
            test_span = pattern_span.search(line)
            if(test_span):
                raw_result = test_span.group(2)
                # print(test_span.group(2))
                break
        else:
            memory.insert(i, line)
            i = i + 1
            test = pattern_all_file.search(line)
            if test:
                condition_met = True

    Title1_pattern = re.compile("Queen ")
    Title2_pattern = re.compile("King ")
    Title3_pattern = re.compile("Prince ")
    Title4_pattern = re.compile("President ")

    Title1 = Title1_pattern.search(raw_result)
    Title2 = Title2_pattern.search(raw_result)
    Title3 = Title3_pattern.search(raw_result)
    Title4 = Title4_pattern.search(raw_result)

    k = 2
    while True:

        if(Title1):
            Title = "Queen"
            break
        if(Title2):
            Title = "King"
            break
        if(Title3):
            Title = "Prince"
            break
        if(Title4):
            Title = "President"
            break
        k += 1
        if (k == 10000):
            Title = "Unknown"
            break

    pattern_name = re.compile("(" + Title + " )(.*)( \(since)")
    name_head_of_state = pattern_name.search(raw_result)
    if (name_head_of_state == None):
        return "Unknown"

    country_file.close()

    return(name_head_of_state.group(2) + ", " + Title)


def findDiplomacy(fileName):
    memory = []
    i = 0
    j = 0
    condition_met = False

    pattern_all_file = re.compile("mailing address:")
    country_file = open("./factbook/geos/" + fileName,
                        "r", encoding="utf8")

    for line in country_file:
        if (condition_met):
            memory.insert(i, line)
            j = j + 1
            if(j == 2):
                break
        else:
            memory.insert(i, line)
            i = i + 1
            test = pattern_all_file.search(line)
            if test:
                condition_met = True
    
    good_line = memory[-2]
    pattern_good_line = re.compile("(\">)(.*)(<\/span)")
    result = pattern_good_line.search(good_line)
    country_file.close()
    raw_result = result.group(2)
    print(raw_result)
    # pattern_percent = re.compile("(.*%)")
    # end_result = pattern_percent.search(raw_result)
    #return end_result.group(1)
