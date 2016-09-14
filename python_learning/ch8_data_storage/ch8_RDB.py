# SQLite is a high quality, light weight, and open source relational database.
# it is made as standaed python library and save database as general file. (Portability)
# it is like MySQL, PostgreSQL, it also have complete function and support for SQL.

# At the begining, you need to use connect() to connect to local SQLite database which you want to use or create.
# ":memory:" can only create it in memory, as you terminate the program the data will be erased also.

import sqlite3
conn = sqlite3.connect(":memory:")
# conn = sqlite3.connect("enterprise.db")
curs = conn.cursor()
curs.execute('''CREATE TABLE zoo 
	(critter VARCHAR(20) PRIMARY KEY,
	 count INT,
	 damages FLOAT)''') # triple quotes is useful for long string in SQL statement 
curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')
# another safe way to insert data(using specifier)
ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
curs.execute(ins, ('weasel', 1, 2000.0))
# read all columns and rows(all animals)
curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)

curs.execute('SELECT * FROM zoo ORDER BY count')
print(curs.fetchall())

curs.execute('SELECT * FROM zoo ORDER BY count DESC')
print(curs.fetchall())

curs.execute('SELECT * FROM zoo WHERE damages = (SELECT MAX(damages) FROM zoo)')
print(curs.fetchall())

curs.close()
conn.close()

# SQLAlchemy 
# you can use SQLAlchemy at three different levels: engine level, SQL Expression Language , ORC
# use "dialect + driver :// user : passward @ host : post / dbname" to connect different database sever . ( No need to import driver program.)
# dialect 			-> 	the type of data base 
# driver 			->	which spefic driver you want to use
# user, passward 	->	your data base verfication string
# host, port 		-> 	the position of the data base( when it isn't the standard sever setting, using : port)
# dbname 			-> 	connecting to the data base at beginging

# engine level( the bottom of SQLAlchemy )(function is much more than DB-API)
print()
import sqlalchemy as sa

conn = sa.create_engine("sqlite://")
# conn = sa.create_engine("sqlite + pysqlite :// /:memory:") 
# The connection string of SQLite skip host, post, user, password. 
# And dbname wil inform SQLite which file is used to store data base. (Omission for storing in memory)
conn.execute('''CREATE TABLE zoo
	(critter VARCHAR(20) PRIMARY KEY,
	 count INT,
	 damages FLOAT)''')# It will retrun a SQLALlchemy object named ResultProxy

ins = "INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)"
conn.execute(ins, ('duck', 10, 0.0))
conn.execute(ins, ('bear', 2, 1000.0))
conn.execute(ins, ('weasel', 1, 2000.0))
rows = conn.execute('SELECT * FROM zoo')# rows is not a list, it is a ojbect that is ResultProxy
print(rows) # it can't be printed directly
for row in rows:
	print(row) # we can iterate it and print row a time

# using engine is much better because we don't need to import db-dirver. Instead, SQLAlehemy can find it through connection string.
# And you only need to change the connection string so that you can take this program to other db-type for using. 
# Another merit is that using SQLAlchemy's connection pooling(連接池)

# SQL Expession Language(upper one layer)
# Expression Language deal with the SQL dialect difference much more than engine level does.
# you can see this level as a intermediary method in RDB application programs
print()
import sqlalchemy as sa

conn = sa.create_engine("sqlite://")
# We begin use Expression Language to replace SQL
meta = sa.MetaData()
zoo = sa.Table('zoo', meta,
	sa.Column('critter', sa.String, primary_key = True),
	sa.Column('count', sa.Integer),
	sa.Column('damages', sa.Float)
	) # it is the same as above example
# zoo is a miracle object bridge up the SQL database world and Python data structure world
meta.create_all(conn)

conn.execute(zoo.insert(("bear", 2, 1000.0)))
conn.execute(zoo.insert(('duck', 10, 0.0)))
conn.execute(zoo.insert(('weasel', 1, 2000.0)))
result = conn.execute(zoo.select())
rows = result.fetchall()
print(rows)

# the uppermost level is ORM(object-rational mapper) which is using SQL Expression Language but trying to real db mechianism not to show up
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

conn = sa.create_engine('sqlite:///zoo.db')

# Now we are in ORM.
Base = declarative_base()
class Zoo(Base):
	__tablename__ = 'zoo'
	critter = sa.Column('critter', sa.String, primary_key = True)
	count = sa.Column('count', sa.Integer)
	damages = sa.Column('damages', sa.Float)
	def __init__(self, critter, count, damages):
		self.critter = critter
		self.count = count
		self.damages = damages
	def __repr__(self):
		return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)

Base.metadata.create_all(conn)# this line will build up data table and data base

first = Zoo('duck', 10, 0.0)
second = Zoo('bear', 2, 1000.0)
third = Zoo('weasel', 1, 2000.0)
print(first)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn)
session = Session()
session.add(first)
session.add_all([second, third])
session.commit()