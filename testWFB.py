import csv
import Main

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
  for answer in correct_table:
    pays = answer[0]
    attribut = answer[1]
    correction = answer[2]
    own_result=Main.get_wfb_info(pays,attribut)
    if (correction==str(own_result)):
      print('OK')
    else:
      print('bad')
