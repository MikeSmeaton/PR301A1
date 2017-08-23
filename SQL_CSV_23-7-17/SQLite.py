import sqlite3
import array
from CSVReader import CSVReader, csv_reader

class SQLite:

    def __init__(self):
        self.column_name = ' '
        self.values = csv_reader.data
        self.connection = sqlite3.connect("entry.db")
        self.cursor = sqlite3.Connection.cursor(self.connection)
        self.function_name = " "
        #self.empid_value = input("Please enter the empid >>> ")

    def open_db(self):
        try:
            connection = sqlite3.connect("entry.db")
        except Exception as My_Connection_Error:
            print(ConnectionError)
        else:
            print("Opened database successfully")
        finally:
            print("Finishing connecting to database")

    def close_db(self):
        print("closing db...")
        self.connection.close()

#    def do_stuff(self, function_name):
#        method_name = ("{}{}{}{}".format("self", '.' ,function_name,'()'))
#        self.open_db()
#        print("fuck")
#        method_name
#        print("cunts")
#        #self.commit()
#        self.close_db()

#    def do_stuff2(self, function_name):
#        method_name = print("self." + function_name + '()')
#        result = method_name
#        self.open_db()
#        result
#        #self.commit()
#        self.close_db()

    def purge_entry_table(self):
        print("purge..")
        #self.open_db()
        self.cursor.execute("""DROP TABLE if exists entry;""")
        self.connection.commit()
        #self.close_db()


    def sql_create_entry(self):
        #self.open_db()
        print("creating entry table into db....")
        self.cursor.execute(
            """
            CREATE TABLE if not exists entry (
            empid VARCHAR(4) PRIMARY KEY,
            gender CHAR(2),
            age INT(2),
            sales INT(3),
            bmi STRING(15),
            salary INT(3),
            dob DATE);
            """
        )
        self.connection.commit()
        #self.close_db()

    def set_rows(self, values):
        #self.open_db()
        print("setting row..")
        x = 0
        while x < len(csv_reader.data):
            self.cursor.execute(
            """INSERT INTO entry (empid, gender, age, sales, bmi, salary, dob) """ +
            """ VALUES (""" +
            """ ' """ + self.values[x][0] + """ ' """ + ', ' +
            """ ' """ + self.values[x][1] + """ ' """ + ', ' +
            """ ' """ + self.values[x][2] + """ ' """ + ', ' +
            """ ' """ + self.values[x][3] + """ ' """ + ', ' +
            """ ' """ + self.values[x][4] + """ ' """ + ', ' +
            """ ' """ + self.values[x][5] + """ ' """ + ', ' +
            """ ' """ + self.values[x][6] + """ ' """ + """ ); """
            )
            x += 1
        self.connection.commit()
        #self.close_db()

    def get_all_columns(self):
        #self.open_db()
        print("getting all columns..")
        query_result = self.cursor.execute("""SELECT * from entry;""")
        results = query_result.fetchall()
        for result in results:
            print(result) #prints each array item (these array items are also arrays)
        print(" ")
        return results #returns a 2D array
        #self.close_db()

    def get_column(self):
        #self.open_db()
        print("getting column..")
        query_result = self.cursor.execute(
            """SELECT """ + input("Please enter the column >>> ") + """ from entry;""")
        print("fetchall....")
        results = query_result.fetchall()
        print("looping")
        for result in results:
            print(result) #returns single lines with each value on each line
        print("returning")
        print("finished")
        return results #returns an array of values
        #self.close_db()

    def get_row_by_value(self):
        #self.open_db()
        print("getting row by value..")
        query_result = self.cursor.execute(
            """SELECT * FROM entry WHERE """ + input("Please enter the column >>> ") +
            """=""" + """ ' """ + input("Please enter the value >>> ").upper() + """ '; """)
        results = query_result.fetchall()
        for result in results:
            print(result)
        return results
        #self.close_db()



new_db1 = SQLite()
new_db1.open_db()
new_db1.purge_entry_table()
new_db1.sql_create_entry()


#print("starting methods")
#print(" ")
#print("get_all_columns")
#print(new_db1.get_all_columns())
#print(" ")
#print("get_column")
#print(new_db1.get_column())
#print(" ")
#print("get_row_by_value")
#print(new_db1.get_row_by_value())
new_db1.set_rows(csv_reader.file_location)
print(" ")
print(" initiating method")
print(new_db1.get_all_columns())
#print(new_db1.do_stuff('get_all_colums'))

#print(" ")
#print("printing csv_reader.data")
#print(csv_reader.data)
#print(" ")
#print("NEXT")
#print(" ")
#print("set_row")
#new_db1.set_rows(csv_reader.file_location)
#print(" ")
#print(new_db1.get_row_by_value())
#print(new_db1.get_column())
#print(" ")
#print(new_db1.get_all_columns())
#print(" ")
#new_db1.close_db()