import sqlite3

peopleValues = (('Ron','Obvious',42), ('Luigi','Vercotti',43), ('Arthur','Belling',28))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES (?,?,?)",
                  peopleValues)

    c.execute("SELECT FirstName,LastName FROM People WHERE Age > 30")
    for row in c.fetchall():
        print(row)
    c.execute("SELECT FirstName,LastName FROM People WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
