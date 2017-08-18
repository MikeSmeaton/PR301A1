import sqlite3
import csv
import array

# import sys
# sys.path.append("..")
# from CSVReader.py import *


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

# Calling methods, should go in controller..?##
csv_reader = CSVReader()
csv_reader.set_delimiter()
csv_reader.set_file_location()
csv_reader.read()
##############################################

print("[0]")
print(csv_reader.data[0])
print("[0][0]")
print(csv_reader.data[0][0])
print("[0] [1]")
print(csv_reader.data[0][1])
print("[0] [2]")
print(csv_reader.data[0][2])
print("[0] [3]")
print(csv_reader.data[0][3])


class SQLite:

    try:
        connection = sqlite3.connect("entry.db")
    except Exception as e:
        print(e)
    else:
        print("Opened database successfully")
    finally:
        print("Finishing connecting to database")

    def __init__(self):
        self.column_name = ' '
        self.values = []
        self.values2 = csv_reader.data
        self.connection = sqlite3.connect("db1.db")
        self.cursor = sqlite3.connection.cursor()
        self.empid_vlaue = 0

    def purge_entry_table(self):
        self.cursor.execute("""DROP TABLE entry;""")
        SQLite.execute("""DROP TABLE entry;""")

    def get_all_columns(self):
        self.cursor.execute("""SELECT * from entry;""")
        SQLite.execute("""SELECT empid from entry;""")

    def get_column(self, column_name):
        self.cursor.execute("""SELECT""" + column_name + """from entry;""")
        SQLite.execute("""SELECT""" + column_name + """from entry;""")

    def set_row(self, values):
        self.cursor.execute(
            """INSERT INTO entry (empid, gender, age, sales,
            bmi, salary, dob) """ + """VALUES (""" + values[0][0] + ', ' +
            values[0][1] + ', ' + values[0][2] + ', ' + values[0][3] + ',  ' +
            values[0][4] + ', ' + values[0][5] + ', ' + values[0][6] + """
                    );"""
        )

    def get_row_by_value(self, empid_value):
        self.cursor.execute(
            """SELECT ROW in entry WHERE empid=' """ +
            empid_value + """ ';"""
        )

        # THIS SECTION MAY BE WRONG, IT'S PURPOSE IS TO INSERT BY TAKING
        # THE ARRAY VALUES FROM THE CSV_READER CLASS AND INSERTING THEM INTO THE TABLE

    def sql_create_entry(self):
        self.cursor.execute(
            """
            CREATE TABLE entry (
            empid VARCHAR(3) PRIMARY KEY,
            gender CHAR(2),
            age INT(2),
            sales INT(3),
            bmi STRING(15),
            salary INT(3),
            dob DATE);
            """
        )
