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
        self.file_location = '/csv3.csv'

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
        self.connection = sqlite3.connect("entry.db")
        self.cursor = sqlite3.Connection.cursor(self.connection)
        self.empid_value = 'A12'

    def purge_entry_table(self):
        print("purge..")
        self.cursor.execute("""DROP TABLE entry;""")
        #SQLite.execute("""DROP TABLE entry;""")

    def get_all_columns(self):
        print("getting all columns..")
        self.cursor.execute("""SELECT * from entry;""")
        return self.cursor.fetchall()
        #SQLite.execute("""SELECT * from entry;""")

    def get_this_column(self, column_name):
        print("getting column..")
        self.cursor.execute("""SELECT""" + column_name + """from entry;""")
        return self.cursor.fetchall()
        #SQLite.execute("""SELECT""" + column_name + """from entry;""")

    def get_column(self):
        print("getting column..")
        self.cursor.execute("""SELECT empid FROM entry;""")
        return self.cursor.fetchall()
        #SQLite.execute("""SELECT""" + column_name + """from entry;""")

    def set_row(self, values2):
        print("setting row..")
        self.cursor.execute(
           """INSERT INTO entry (empid, gender, age, sales, bmi, salary, dob) """ +
           """ VALUES (""" +
           """ ' """ + self.values2[0][0] + """ ' """ +  ', ' +
           """ ' """ + self.values2[0][1] + """ ' """ + ', ' +
           """ ' """ + self.values2[0][2] + """ ' """ + ', ' +
           """ ' """ + self.values2[0][3] + """ ' """ + ', ' +
           """ ' """ + self.values2[0][4] + """ ' """ + ', ' +
           """ ' """ + self.values2[0][5] + """ ' """ + ', ' +
           """ ' """ + self.values2[0][6] + """ ' """ +
           """ ); """
        )

    def get_empid_by_value(self, empid_value):
        print("getting row by value..")
        self.cursor.execute(
            """SELECT ROW in entry WHERE empid=' """ +
            """ ' """ + empid_value + """ ' """ + """ ; """
        )
        return self.cursor.fetchall()




        # THIS SECTION MAY BE WRONG, IT'S PURPOSE IS TO INSERT BY TAKING
        # THE ARRAY VALUES FROM THE CSV_READER CLASS AND INSERTING THEM INTO THE TABLE

    def sql_create_entry(self):
        print("creating entry table into db....")
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

new_db1 = SQLite()
new_db1.purge_entry_table()
new_db1.sql_create_entry()
print("printing csv_reader.data")
print(csv_reader.data)
new_db1.set_row(csv_reader.data)
print(new_db1.get_empid_by_value('A12'))



#print("print new_db1.values")
#print(new_db1.values2)

#def set_row(self, values):
#    print("setting row..")
#    self.cursor.execute(
#        """INSERT INTO entry (empid, gender, age, sales,
#        bmi, salary, dob) """ + """VALUES (""" + values[0][0] + ', ' +
#        values[0][1] + ', ' + values[0][2] + ', ' + values[0][3] + ',  ' +
#        values[0][4] + ', ' + values[0][5] + ', ' + values[0][6] + ', '"""
#                );"""
#    )
