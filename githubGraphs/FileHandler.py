import csv


class FileHandler(object):
    def __init__(self, file):
        self.file = file

    def get_file(self):
        with open(self.file) as csv_file:
            reader = csv.reader(csv_file)
            value1 = []
            value2 = []
            value3 = []
            for row in reader:
                row1 = row[0]
                row2 = row[1]
                row3 = row[2]

                value1.append(row1)
                value2.append(row2)
                value3.append(row3)

            return [value1, value2, value3]

    def write_file(self):
        open_file = open(self.file, "w")
        writing = input("Write file content: ")
        open_file.write(writing)
        print(writing)
        open_file.close()

