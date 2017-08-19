import sqlite3
from CSVReader import CSVReader


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
        #self.values2 = csv_reader.data
        self.connection = sqlite3.connect("entry.db")
        self.cursor = sqlite3.Connection.cursor(self.connection)
        self.empid_value = 0

    def purge_entry_table(self):
        print("purge..")
        self.cursor.execute("""DROP TABLE entry;""")
        #SQLite.execute("""DROP TABLE entry;""")

    def get_all_columns(self):
        print("getting all columns..")
        self.cursor.execute("""SELECT * from entry;""")
        #SQLite.execute("""SELECT * from entry;""")

    def get_column(self, column_name):
        print("getting column..")
        self.cursor.execute("""SELECT""" + column_name + """from entry;""")
        #SQLite.execute("""SELECT""" + column_name + """from entry;""")

    def set_row(self, values):
       print("setting row..")
       self.cursor.execute(
           """INSERT INTO entry (empid, gender, age, sales, bmi, salary, dob) """ + """VALUES (""" + self.values[0][0] + ', ' +
           self.values[0][1] + ', ' + self.values[0][2] + ', ' + self.values[0][3] + ', ' +
           self.values[0][4] + ', ' + self.values[0][5] + ', ' + self.values[0][6] + ', ' """
                   );"""
       )



    def get_row_by_value(self, empid_value):
        print("getting row by value..")
        self.cursor.execute(
            """SELECT ROW in entry WHERE empid=' """ +
            empid_value + """ ';"""
        )

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
print("print new_db1.values")
#print(new_db1.values2)
new_db1.set_row(new_db1.values2)