import sqlite3

connection = sqlite3.connect('database.sqlite3')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE DRIVERS(
                    NAME TEXT,
                    PHONE_NO TEXT,
                    ADDRESS TEXT,
                    ORGANISATION TEXT,
                    BLOOD_GRP TEXT,
                    LICENCE_MONTH_VALIDITY TEXT,
                    LICENCE_YEAR_VALIDITY  INTEGER
               )""")

connection.commit()
connection.close()