import csv
import json
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
import argparse

# file extesion
mypath = 'C:\\Desktop\\'
fileName = mypath + 'students.csv'
class ParserInterface:
    def convert(self):
        pass

class ParserJSON(ParserInterface):
    def __init__(self):
        pass
    def convert(self):
        global mypath
        dic = Read_CSV_Make_Dict()
        # convert into JSON
        jsonString = json.dumps(dic)
        jsonFile = open("IN_JSON.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

class ParserXML(ParserInterface):
    def __init__(self):
        pass
    def convert(self):
        global mypath
        dic = Read_CSV_Make_Dict()
        # Variable name of Dictionary is Labels
        xml = dicttoxml(dic)

        # Obtain decode string by decode()
        # function
        xml_decode = xml.decode()

        xmlfile = open("IN_XML.xml", "w")
        xmlfile.write(xml_decode)
        xmlfile.close()


def Read_CSV_Make_Dict():
    global mypath, fileName

    # read csv file into a List
    with open('students.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        tmp_Labels = list(csv_reader)

    ## make dict
    Labels = tmp_Labels[0]
    other = []
    for i in range(0, len(tmp_Labels[0])):
        other.append(list())
    aDict = dict(zip(Labels, other))

    for i in tmp_Labels[1:]:
        for k, j in enumerate(i):  # Lines
            aDict[Labels[k]].append(j)
    return aDict



def Covert_to_JSON():
    global mypath
    dic = Read_CSV_Make_Dict()
    # convert into JSON
    jsonString = json.dumps(dic)
    jsonFile = open("IN_JSON.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

def Covert_to_XML():
    global mypath
    dic = Read_CSV_Make_Dict()
    # Variable name of Dictionary is Labels
    xml = dicttoxml(dic)

    # Obtain decode string by decode()
    # function
    xml_decode = xml.decode()

    xmlfile = open(mypath + "IN_XML.xml", "w")
    xmlfile.write(xml_decode)
    xmlfile.close()



def choosen(name):
    if name == 'JSON':
        JSON_File = ParserJSON()
        JSON_File.convert()


    elif name == 'XML':
        XML_File = ParserXML()
        XML_File.convert()

    print(f'Hello, see files you requsted before in the same directory')

def main():
    n = input("Enter the format (JSON or XML)")
    choosen(n)


main()
