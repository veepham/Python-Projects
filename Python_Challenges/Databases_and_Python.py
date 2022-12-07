# Databases and Python Challenge
#
# Version: Python 3.11.0
#
# Prompt:   Create a database table in RAM named Roster that includes the fields ‘Name’, ‘Species’ and ‘IQ.’
#           Populate your new table with the following values:
#               Jean-Baptiste Zorg, Human, 122
#               Korben Dallas, Meat Popsicle, 100
#               Ak'not, Mangalore, -5
#           Update the Species of Korben Dallas to be Human.
#           Display the names and IQs of everyone in the table who is classified as Human.
#

import sqlite3

# tuple for data points
rosterList = (("Jean-Baptiste Zorg", "Human", 122),("Korben Dallas", "Meat Popsicle", 100),("Ak'not", "Mangalore", -5))

with sqlite3.connect(':memory:') as connection:
    c = connection.cursor() # establishing cursor
    # creating table
    c.execute ("CREATE TABLE IF NOT EXISTS tbl_roster ( \
                Name TEXT, \
                Species TEXT, \
                IQ INT \
                )")
    c.executemany("INSERT INTO tbl_roster VALUES (?,?,?)", rosterList) # adding values to table using tuple
    # updating species of one of the data sets
    c.execute("UPDATE tbl_roster SET Species = 'Human' WHERE Name = 'Korben Dallas'")
    # defining what parameters to print
    c.execute("SELECT Name,IQ FROM tbl_roster WHERE Species = 'Human'")
    for row in c.fetchall():
        print(row)


