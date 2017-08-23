import csv
import array


class CSVReader:
    def __init__(self):
        self.var = ','
        self.data = []
        self.file_location = '../csv3.csv'

    def set_delimiter(self):
        self.var = input("Please enter the delimiter character in use >>> ")

    def set_file_location(self):
        self.file_location = input("Please enter the file location >>> ")


    def read(self):
        with open(self.file_location, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter = self.var, quotechar='|')
            for row in csvreader:
                self.data.append(row)
        return self.data

#Calling methods, should go in controller..?##
# csv_reader = CSVReader()
# csv_reader.set_delimiter()
# csv_reader.set_file_location()
# csv_reader.read()
##############################################

# print("[0]")
# print(csv_reader.data[0])
# print("[0][0]")
# print(csv_reader.data[0][0])
# print("[0] [1]")
# print(csv_reader.data[0][1])
# print("[0] [2]")
# print(csv_reader.data[0][2])
# print("[0] [3]")
# print(csv_reader.data[0][3])

###################################################################################
##              OLD CODE MAY NOT BE NECESSARY                                    ##
## path = 'H:\\BCIT_YEAR3_SEMESTER1\\Python\\new1.txt' ## Do I need to use this? ##
##                days_file = open(path,'r') ## and this                         ##
###################################################################################