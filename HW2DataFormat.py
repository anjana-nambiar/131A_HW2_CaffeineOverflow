"""
Authors: Caffine Overflow-Anjana Nambiar, Hitayshi Shah, Karan Gandhi, Kalyal Pullela 
CMPE 131-Professor Bond
Homework2: Data Format
"""


import sys
import pandas
from dict2xml import dict2xml
from pathlib import Path
import os
import json
import csv

def createCSVFile(tabFile):
    print("converting file from txt to csv... ")
    read_file = pandas.read_csv (tabFile, delimiter="\t")
    csv_outfile_name = Path(tabFile).stem + ".csv"
    print("Converted file: " +  csv_outfile_name)
    read_file.to_csv (csv_outfile_name, index=None)
    return

def createJSONFile(tabFile):
      print("converting file from txt to json...")
      with open (tabFile, 'r') as file:
        reader = csv.DictReader(file, delimiter="\t")
        data = list(reader)
        json_outfile_name = Path(tabFile).stem + ".json"
        print("Converted file: " + json_outfile_name)
        json_outfile=open(json_outfile_name, 'w')
        json.dump(data,json_outfile,indent=4)
        json_outfile.close()
        return

def createDictionary(fn):
    dt = pandas.read_csv(fn, sep = '\t')
    list_of_dictionarys = [item for item in dt.T.to_dict().values()]
    return list_of_dictionarys

def createXMLFile(tabFile):
    print("converting file from txt to xml...")
    dict = createDictionary(tabFile)
    xml_data = dict2xml(dict)
    xml_outfile = Path(tabFile).stem + ".xml"
    print("Converted file: " + xml_outfile)
    with open(xml_outfile, "w", encoding="utf-8") as f:
        f.write(xml_data)
        f.close()
        return
 
def serializeTabbedTxt(filename, option):
    print("The original file: " + fileName)
    txt = """
    'c' csv file
    'j' json file
    'x' xml file
    """
    print(txt)
    print("Chosen option:" + option)
    
    if option == 'c': 
        createCSVFile(fileName)
    elif option == 'j': 
        createJSONFile(fileName)
    elif option == 'x': 
        createXMLFile(fileName) 





if __name__ == "__main__":
    fileName = str(sys.argv[1])
    option = str(sys.argv[2])
    print("**********************************************")
    serializeTabbedTxt(fileName, option)