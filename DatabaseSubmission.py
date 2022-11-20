# Database Submission Assignment for The Tech Academy


# Creating database with 2 columns, the ID auto-increment
# and file name column

import sqlite3

conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute ("CREATE TABLE IF NOT EXISTS tbl_data ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )")
    conn.commit()
    
# tuple of file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# Pulling file names in tuple that end in '.txt' by a loop
conn = sqlite3.connect('test.db')
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO tbl_data (col_file) VALUES (?)', (x,))
            # utilizing the format of a single tuple (x,) 
            print(x)
    
conn.close()




