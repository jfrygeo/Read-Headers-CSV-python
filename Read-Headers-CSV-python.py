#Reads one line in a large csv file
#Gives total count of lines csv
# __author__ = 'john6807'
import csv,os

#Input the filepath to your csv file: i.e. "C:\\MyFolder\\MyCSV.csv"
#filename = "C:\\MyFolder\\MyCSV.csv"
filename = os.path.join(os.path.dirname(__file__)+"\SampleData\TestCSV.csv")

#Depending on your data source, you may need to change the encoding(i.e. ('utf-8','utf-16')
#infile = open(filename, 'r', encoding=("iso-8859-15"))
infile = open(filename, 'r')

# Read the headers of the csv file
def file_headers(infile):
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    print (fieldnames)
file_headers(infile)

#Read the length of the file
def file_length(infile):
    for i, length in enumerate(infile):
        pass
    print (str(i + 2) + " Total lines and headers")
file_length(infile)

exit()
