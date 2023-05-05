# #
# from sqlite3 import connect
# with connect("Student.db") as db_file:
#     yonalish = db_file.cursor()
#     yonalish.execute("""create table if not exists Student(
#     ism varchar,
#     familia varchar,
#     baho int
#     )""")
#
# with connect("Student.db") as db_file:
#     yonalish = db_file.cursor()
#     yonalish.execute("""select * from Student where ism like "%ali%" """)
#     users = yonalish.fetchall()
#
#     print(users)

from sqlite3 import connect
with connect("Talaba.db") as db_file:
    yonalish = db_file.cursor()
    yonalish.execute("""create table if not exists Talaba1(
    ism varchar,
    fam varchar,
    baho int)""")
    yonalish.execute("""insert into Talaba1 values ("Ikromjon", "Ibrohimov", 15)""")


with connect("Talaba.db") as db_file:
    yonalish = db_file.cursor()
    yonalish.execute("""select * from Talaba1""")
    users = yonalish.fetchall()
    print(yonalish, users)





# with connect("Student.db") as db_file:
#     yonalish = db_file.cursor()
#     yonalish.execute("""insert into Student(ism, familia, baho)
#     values("Ali", "Valiyev", 5 )
#     """)

# with connect("Student.db") as db_file:
#     yonalish = db_file.cursor()
#     yonalish.execute("""insert into Student(ism, familia, baho)
#     values("Muhammadali", "Valijonev", 4 )
#     """)
#
# with connect("Student.db") as db_file:
#     yonalish = db_file.cursor()
#     yonalish.execute("""insert into Student(ism, familia, baho)
#     values("G'ani", "Valiyev", 2 )
#     """)
#
# with connect("Student.db") as db_file:
#     yonalish = db_file.cursor()
#     yonalish.execute("""insert into Student(ism, familia, baho)
#     values("Hasan", "husanov", 5 )
#     """)
#
# with connect("Student.db") as db_file:
#     yonalish = db_file.cursor()
#     yonalish.execute("""insert into Student(ism, familia, baho)
#     values("Husan", "Valiyev", 3 )
#     """)

# import sqlite3
# con = sqlite3.connect("tutorial1.db")
# cur = con.cursor()
# cur.execute("CREATE TABLE Student(ism, fam, bali)")
# res = cur.execute("SELECT name FROM Student")
# res.fetchone()
# res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
# res.fetchone() is None
# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)
# res = cur.execute("SELECT score FROM movie")
# res.fetchall()
# [(8.2,), (7.5,)]
# data = [
#     ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
#     ("Monty Python's The Meaning of Life", 1983, 7.5),
#     ("Monty Python's Life of Brian", 1979, 8.0),
# ]
# cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
# con.commit()  # Remember to commit the transaction after executing INSERT.
# for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
#     print(row)
#
