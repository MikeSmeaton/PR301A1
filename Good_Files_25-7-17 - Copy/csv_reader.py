import csv


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
            csvreader = csv.reader(csvfile, delimiter=self.var, quotechar='|')
            for row in csvreader:
                self.data.append(row)
        return self.data


# Calling methods, should go in controller..?##
csv_reader = CSVReader()
# csv_reader.set_delimiter()
# csv_reader.set_file_location()
csv_reader.read()


