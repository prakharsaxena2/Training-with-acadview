import MySQLdb

# Importing MySQLdb module
db = MySQLdb.connect("localhost", "root", "2050", "dbase")
# Connecting Database
cursor = db.cursor()
# Creating cursor

'''Q1'''
# Creating Table BOOKS
sql1 = """CREATE TABLE BOOKS
BOOK_ID INT NOT NULL,
TITLE_ID INT,
LOCATION CHAR(15),
GENRE CHAR(15)
"""

# Creating Table TITLES
sql2 = """CREATE TABLE TITLES
TITLE_ID INT NOT NULL,
TITLE CHAR(30),
ISBN INT,
PUBLISHER_ID INT,
PUBLICATION_YEAR INT
"""

# Creating Table PUBLISHERS
sql3 = """CREATE TABLE PUBLISHERS
PUBLISHER_ID INT NOT NULL,
NAME CHAR(30),
STREET_ADDRESS CHAR(30),
SUITE_NUMBER INT,
ZIP_CODE_ID INT
"""

# Creating Table ZIP CODES
sql4 = """CREATE TABLE ZIP_CODES
ZIP_CODE_ID INT NOT NULL,
CITY CHAR(20),
STATE(20),
ZIP_CODE INT
"""

# Creating Table AUTHORS TITLES
sql5 = """CREATE TABLE AUTHORS_TITLES
AUTHOR_TITLE_ID INT NOT NULL,
AUTHOR_ID INT,
TITLE_ID INT
"""

# Creating Table AUTHORS
sql6 = """CREATE TABLE AUTHORS
AUTHOR_ID INT NOT NULL,
FIRST_NAME CHAR(10),
MIDDLE_NAME CHAR(10),
LAST_NAME CHAR(10)
"""

# Executing statements
cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
cursor.execute(sql5)
cursor.execute(sql6)

'''Q2'''
# Inserting into BOOKS
insert1 = """INSERT INTO BOOKS(BOOK_ID,TITLE_ID,LOCATION,GENRE )
        VALUES(199, 83, "Turning Points","Autobiography")"""
try:
    cursor.execute(insert1)
    db.commit()
except:
    db.rollback()

# Inserting into TITLES
insert2 = """INSERT INTO TITLES( TITLE_ID,TITLE,ISBN,PUBLISHER_ID,PUBLICATION_YEAR )
        VALUES(83,"Turning Points",9789350293478,347,2012)"""
try:
    cursor.execute(insert2)
    db.commit()
except:
    db.rollback()

# Inserting into PUBLISHERS
insert3 = """INSERT INTO PUBLISHERS(PUBLISHER_ID,NAME,STREET_ADDRESS,STATE_NUMBER,ZIP_CODE_ID )
        VALUES(347,"Harper Collins","Sector 57",4,68)"""
try:
    cursor.execute(insert3)
    db.commit()
except:
    db.rollback()

# Inserting into ZIP CODES
insert4 = """INSERT INTO ZIP_CODES(ZIP_CODE_ID,CITY,STATE,ZIP_CODE)
        VALUES(68,"Noida","UP",201301)"""
try:
    cursor.execute(insert4)
    db.commit()
except:
    db.rollback()

# Inserting into AUTHORS TITLES
insert5 = """INSERT INTO AUTHORS_TITLES(AUTHOR_TITLE_ID,AUTHOR_ID,TITLE_ID )
        VALUES(100,101,285)"""
try:
    cursor.execute(insert5)
    db.commit()
except:
    db.rollback()

# Inserting into AUTHORS
insert6 = """INSERT INTO AUTHORS(AUTHOR_ID, FIRST_NAME, MIDDLE_NAME,LAST_NAME )
        VALUES(109,""APJ,"Abdul","Kalam")"""
try:
    cursor.execute(insert6)
    db.commit()
except:
    db.rollback()

'''Q3'''
# Updating values into BOOKS
update = """UPDATE BOOKS SET GENRE = "Fiction"
      WHERE LOCATION='Noida'"""
try:
    cursor.execute(update)
    db.commit()
except:
    db.rollback()
db.close()
