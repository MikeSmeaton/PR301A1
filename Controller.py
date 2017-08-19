from ChartOutputController import ChartController
from CSVReader import CSVReader

class Controller(object):
    def __init__(self):
        self.inputCSVArray = ""
        pass

    def graph_pi_gender(self, male_female_array):
        test_pie = ChartController("Genders of Sales People")
        test_pie.get_pie_chart(["Male", "Female"], male_female_array)

    def read_from_csv(self):
        csv = CSVReader()
        self.inputCSVArray = csv.read()

    def read_from_csv_changes(self):
        csv = CSVReader()
        csv.set_delimiter()
        csv.set_file_location()
        self.inputCSVArray = csv.read();
        pass

    def output_array(self):
        print(self.inputCSVArray)

# used for testing purposes. Main method will be in the CLI console view.
if __name__ == "__main__":
    c = Controller()
    # c.graph_pi_gender([200, 400])

    c.read_from_csv()
    c.output_array()