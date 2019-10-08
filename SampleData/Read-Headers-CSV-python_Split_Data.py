#Reads one line in a large csv file
#Gives total count of lines csv
# __author__ = 'john6807'
import csv,os, pandas

#Input the filepath to your csv file: i.e. "C:\\MyFolder\\MyCSV.csv"
#filename = "C:\\MyFolder\\MyCSV.csv"
#filename = os.path.join(os.path.dirname(__file__)+"\SampleData\TestCSV.csv")
response = input("Please Enter Location of Input CSV (""Example: C:\Test\TestCSV.csv)"": ")

#Depending on your data source, you may need to change the encoding(i.e. ('utf-8','utf-16')
#infile = open(response, 'r', encoding=("iso-8859-15"))
infile = open(response, 'r')

# Read the headers of the csv file
# def file_headers(infile):
#     global fieldnames
#     reader = csv.DictReader(infile)
#     fieldnames = reader.fieldnames
#     print (fieldnames)
#
# file_headers(infile)
#
# firstdata = csv.DictReader(infile).fieldnames

#Size of chunks
chunksize = input("Please Enter Size of Chunk (""Bytes"": ")

for i, size in enumerate(pandas.read_csv(infile,low_memory=False, warn_bad_lines=False, error_bad_lines=False, chunksize=100000)):
    size.to_csv('chunk{}.csv'.format(i))

#Read the length of the file
#def file_length(infile):
#    for i, length in enumerate(infile):
#        pass
#    print (str(i + 2) + " Total lines and headers")
#file_length(infile)

# Do you want to create a sample csv?
#yesno = input("Would you like a sample output CSV (Y/N)?: ")
#while True:
#    yesChoice = set(['yes', 'y', 'Y', 'YES'])
#   noChoice = set(['no', 'n', 'N', 'NO'])
#    if yesno in yesChoice:

        # create a csv with sample data of the headers and row
 #       newcsv = input("Please Enter an Output Location and filename for Sample CSV: ")
#        with open (newcsv, 'w') as file:
#            writer = csv.writer(file,lineterminator="\n")
 #           writer.writerow(fieldnames)
#            writer.writerow(firstdata)
#            break

 #   if yesno in noChoice:
 #       break

os.system("Pause")
exit()
