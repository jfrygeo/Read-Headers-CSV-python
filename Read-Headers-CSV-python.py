#Reads one line in a large csv file
# __author__ = 'john6807'
import csv, os

#Input the filepath to your csv file: i.e. "C:\\MyFolder\\MyCSV.csv"
filepath = r"C:\\MyFolder\\MyCSV.csv"

with open(filepath, 'r') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    print (fieldnames)

os.system("pause")
