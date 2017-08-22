import csv


class FileHandler(object):
    def __init__(self, file):
        self.file = file

    def get_file(self):
        with open(self.file) as csv_file:
            """
            >>> file = FileHandler('written_file.csv')
            >>> file.get_file()
            [['Oxygen', 'Hydrogen', 'Carbon_Dioxide'], ['4500', '2500', '1053'], ['words name', 'Number Names', 'None']]
            """
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

    def write_file(self, input_content):
        open_file = open(self.file, "w")
        open_file.write(input_content)
        open_file.close()
        return input_content

