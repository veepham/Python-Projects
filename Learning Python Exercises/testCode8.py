import sqlite3

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_person ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_person(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
                ('Sara', 'Jones', 'sjones@gmail.com'))
    cur.execute("INSERT INTO tbl_person(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
                ('Sally', 'Shell', 'sshell@gmail.com'))
    cur.execute("INSERT INTO tbl_person(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
                ('Kevin', 'Bacon', 'kbacon@gmail.com'))
    
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname,col_lname,col_email FROM tbl_person WHERE col_fname = 'Sara'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0],item[1],item[2])
    print(msg)
