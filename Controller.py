from ChartOutputController import ChartController
from CSVReader import CSVReader
from Validator import Validator
from Entry import Entry
from SQLite import SQLite


class Controller(object):
    def __init__(self):
        self.inputCSVArray = []
        self.db = SQLite()

    # --- Database methods ---
    def init_db(self):
        self.db.set_values(self.inputCSVArray)
        self.db.open_db()
        self.db.purge_entry_table()
        self.db.sql_create_entry()
        self.db.connection.commit()
        self.db.close_db()

    def populate_db(self):
        self.db.open_db()
        self.db.set_rows()
        self.db.connection.commit()
        self.db.close_db()


    # --- Graphs hard coded methods ---
    def graph_pi_gender(self, male_female_array):
        test_pie = ChartController("Genders of Sales People")
        test_pie.get_pie_chart(["Male", "Female"], male_female_array)


    # --- csv reader ---
    def read_from_csv(self):
        csv = CSVReader()
        self.inputCSVArray = csv.read()

    def read_from_csv_filename(self, filename):
        csv = CSVReader()
        csv.file_location = filename
        self.inputCSVArray = csv.read()

    def read_from_csv_filename_delimiter(self, filename, delimiter):
        csv = CSVReader()
        csv.file_location = filename
        csv.var = delimiter
        self.inputCSVArray = csv.read()


    def commit_input(self, input_array):
        validated = self.run_validator(input_array)
        self.run_db()

    # --- validator ---
    def run_validator(self, input_array):
        empid, gender, age, sales, bmi, salary, birthday = ""
        x = 0
        entry_outputs, output_array = []
        while x < len(input_array):
            empid = input_array[x][0]
            gender = input_array[x][1]
            age = input_array[x][2]
            sales = input_array[x][3]
            bmi = input_array[x][4]
            salary = input_array[x][5]
            birthday = input_array[x][6]
            v = Validator(empid, gender, age, sales, bmi, salary, birthday)
            entry_outputs.append(v.validate())
        self.convert_entry_collection_to_array(entry_outputs)
        output_array = self.convert_entry_collection_to_array(entry_outputs)


    # --- converter for entry to array ---
    def convert_entry_collection_to_array(self, entry):
        result = []
        x = 0;
        while x < len(entry):
            result[x][0] = entry.get_empid()
            result[x][1] = entry.get_gender()
            result[x][2] = entry.get_age()
            result[x][3] = entry.get_sales()
            result[x][4] = entry.get_bmi()
            result[x][5] = entry.get_salary()
            result[x][6] = entry.get_birthday()
        return result

    def convert_array_to_entry_collection(self, array):
        #take array and convert to entry list
        pass




# used for testing purposes. Main method will be in the CLI console view.
if __name__ == "__main__":
    con = Controller()
    # c.graph_pi_gender([200, 400])

    # c.read_from_csv()
    # c.output_array()
    test_object_array = []
    a = Entry("A12", "M", "21", "123", "Normal", "666", "01-01-1990")
    b = Entry("B12", "F", "21", "123", "Normal", "666", "01-01-1990")
    c = Entry("C12", "M", "21", "123", "Fat Mofo", "666", "01-01-1990")
    test_object_array.append(a.get_birthday())
    test_object_array.append(b)
    test_object_array.append(c)

    print(test_object_array)

