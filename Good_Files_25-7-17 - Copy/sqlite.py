import sqlite3
import array
from csv_reader import CSVReader, csv_reader


class SQLite:

    def __init__(self):
        self.column_name = ' '
        self.values = csv_reader.data
        self.connection = sqlite3.connect("entry.db")
        self.cursor = sqlite3.Connection.cursor(self.connection)
        self.function_name = " "

    @staticmethod
    def stat_open_db(db_location):
        try:
            connection = sqlite3.connect(db_location)
        except sqlite3.Error as error:
            print(error)
        except Exception as connection_error:
            print(connection_error)
        else:
            print("Opened database successfully")
            return connection
        finally:
            print("Finishing")

    def open_db(self):
        try:
            connection = sqlite3.connect(db_location)
        except sqlite3.Error as error:
            print(error)
        except Exception as connection_error:
            print(connection_error)
        else:
            print("Opened database successfully")
            return connection
        finally:
            print("Finishing")

    def close_db(self):
        print("closing db...")
        self.connection.close()

    def do_stuff(self, function_name):
        self.open_db()
        eval('self.' + function_name)
        self.commit()
        self.close_db()

    def purge_entry_table(self):
        print("purge..")
        self.cursor.execute("""DROP TABLE if exists entry;""")
        self.connection.commit()

    def sql_create_entry(self):
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

    def set_rows(self):
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

    def get_all_columns(self):
        print("getting all columns..")
        query_result = self.cursor.execute("""SELECT * from entry;""")
        results = query_result.fetchall()
        for result in results:
            print(result)  # prints each array item (these array items are also arrays)
        print(" ")
        return results  # returns a 2D array

    def get_column(self):
        print("getting column..")
        query_result = self.cursor.execute(
            """SELECT """ + input("Please enter the column >>> ") + """ from entry;""")
        print("fetchall....")
        results = query_result.fetchall()
        print("looping")
        for result in results:
            print(result)  # returns single lines with each value on each line
        print("returning")
        print("finished")
        return results  # returns an array of values

    def get_column_values(self):
        print("getting column..")
        query_result = self.cursor.execute(
            """SELECT """ + input("Please enter the column >>> ") + """ from entry;""")
        print("fetchall....")
        results = query_result.fetchall()
        print("looping")
        for result in results:
            print(result)  # returns single lines with each value on each line
        print("returning")
        print("finished")
        return results  # returns an array of values

    def get_row_by_value(self):
        print("getting row by value..")
        query_result = self.cursor.execute(
            """SELECT * FROM entry WHERE """ + input("Please enter the column >>> ") +
            """=""" + """ ' """ + input("Please enter the value >>> ").upper() + """ '; """)
        results = query_result.fetchall()
        for result in results:
            print(result)
        return results


new_db1 = SQLite()
new_db1.stat_open_db("entry.db")  # static function
# new_db1.open_db()  # non-static function
new_db1.purge_entry_table()
new_db1.sql_create_entry()
new_db1.set_rows()
