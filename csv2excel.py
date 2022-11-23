import os
import pandas as pd

def csv2excel(file):
    csvreader = pd.read_csv(file, encoding='utf-8')
    pd.to_excel(csvreader)
    
csvFile = input("Please input a csv file path: ")

csv2excel(csvFile)
