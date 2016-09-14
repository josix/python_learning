test1 = "This is a test of the emergency text system"
fout = open('text.txt', 'wt')
fout.write(test1)
fout.close()

with open('text.txt', 'rt') as fin:
	data = fin.read()
	print(data)
	print(test1)

data = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
'''
with open("books.csv", "wt") as fout:
	fout.write(data)

import csv
with open('books.csv', "rt") as fin:
	cin = csv.DictReader(fin)
	books = [row for row in cin]
print(books)

data = '''title,author,year
The Weiredstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Mi.ville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
'''
with open('books2.csv', 'wt') as fout:
	fout.write(data)

import sqlite3
conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('''CREATE TABLE books
	(title VARCHAR(20) PRIMARY KEY,
	 author VARCHAR(20),
	 year INT)''')
ins = "INSERT INTO books (title, author, year) VALUES (?, ?, ?)"
with open('books2.csv', 'rt') as fin:
	cin = csv.DictReader(fin)
	for row in cin :
		cur.execute(ins, (row['title'], row['author'], row['year']))

cur.execute("SELECT * FROM books")
print(cur.fetchall())
cur.execute("SELECT * FROM books ORDER BY title")
print(cur.fetchall())
cur.execute("SELECT * FROM books ORDER BY year")
print(cur.fetchall())

cur.close()
conn.close()