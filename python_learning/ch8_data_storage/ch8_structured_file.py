'''
Use some formats to distinguish different files:

separator(or delimiter): 		'\t' '|' ',' 		(Comma-Sperated Value CSV)
outside of tag: 				'<' '>' 			(HTML XML)
punctuation											(JavaScript Object Notation JSON)
indentation											(YAML)
others: setting file or program
'''
# CSV
# we use standard CSV module to analyze these file.
# Because......
# some file will use seperator '|' '\t' 
# some file will use escape sequence. \
#	(If content in the column has seperator, all the column will be enclosed by quotation, or adding some escape char before it)  
# file will use different end-of-line characters. Unix use '\n', Microsof use '\r \n', Apple use '\n'
# the first line may be the column name

# First, let's see how to read and write a series of 'rows'
import csv 
villains = [['Doctor', 'No'], ['Rosa', 'Klebb'], ['Mister', 'Big'], ['Auric', 'Goldfinger'], ['Ernst', 'Blofeld']] 
with open('villains', 'wt') as fout: # a context manager
	csvout = csv.writer(fout)
	csvout.writerows(villains)
# create a csv file named villains
# and then we read them back
with open('villains', 'rt') as fin:# a contextt manager
	cin = csv.reader(fin) # create a  object contains a series of 'rows'  
	villains = [row for row in cin] # list comprehension
print(villains)

# data also could be a dict by using DictReader()
print()
with open('villains', 'rt') as fin:
	cin = csv.DictReader(fin, fieldnames = ['first', 'last'])
	villains = [row for row in cin]
print(villains)

# use DictWriter() to override the csv file. And use writeheader() to write a fieldname at the begining.
print()
vaillains = [{"first":"Docter", "last": 'No'},
			 {"first":"Rosa", "last" : "Klebb"},
			 {"first":"Mister", "last" : "Big"},
			 {"first":"Auric", "last":"Goldfinger"},
			 {"first":"Ernst","last":"Blofeld"}]
import csv
with open('villains', 'wt') as fout:
	csvout = csv.DictWriter(fout, fieldnames = ['first', 'last'])
	csvout.writeheader()
	csvout.writerows(vaillains)

with open('villains', 'rt') as fin:
	cin = csv.DictReader(fin)
	villains_output = [row for row in cin]

print(villains_output)


# XML
# the CSV file only express two deminsion: clomns, and rows. 
# So if you want to pass file structure between programs, you need to encode classes, sets, sequence into text.
# XML is a markup format which is suitable for this purpose.
# Here are the merits of XML file:
#	(1) tag is begining with '<' .
#	(2) xml is often written in this format: <opening tag> contents.... </closing tag>
#	(3) ignore the space character
# 	(4) tags could be nested in other tags
# 	(5) there could appear optional attribute in the begining tag
#	(6) we could put the value in tags
# 	(7) if there is a tag named thing and it has no attribute, sub tags, and values. we coul express it in this way: <thing/> (== <thing></thing>)
#   (8)	you can arbitarily put the data(attribute, value, sub tags) 
# XML is often used for data feed and message.

# In python, the simplest way to anylaze XML is using ElementTree 
print()
import xml.etree.ElementTree as et
tree = et.ElementTree(file = 'menu.xml')
root = tree.getroot()
print(root.tag)
for child in root:
	print('tag:', child.tag, 'attributes:', child.attrib)
	for grandchild in child:
		print("\ttag:", grandchild.tag, 'attributes:', grandchild.attrib)
print(len(root)) # number of menu section
print(root[0].tag, len(root[0])) # number of breakfast items

# JSON -- a popular data exchange format
# JSON is a subset of JS, it is also legal for python so that it becomes a good option for exchange data between programs
# Differernt from xml, JSON has a main module-- json. It will save data to JSON string, and load JSON string to data.
menu = \
{
	"breakfast" :{
		"hours" : "7-11",
		"items" : {
				"breakfast burritos" : "$6.00",
				"pancakes" : "$4.00",
				}
			},
	"launch" : {
		"hours" : "11-3",
		"items" : {
				"hamburgers" : "$5.00"
				}
			},
	"dinner" : {
		"hours" : "3-10",
		"items" : {
				"spaghetti" : "$8.00"
		}
	}
} 

# use dumps() to encode data into JSON string
print()
import json
menu_json = json.dumps(menu)
print(menu_json)

# And we use loads() to decode JSON string into data 
menu2 = json.loads(menu_json)
print(menu2)

# YAML is similar to JSON, it also have key and value however it can deal with more data typing like date and time.
# use load() to decode YAML string into python data
# use dump() to encode python data into YAML string
print()
import yaml
with open('mcintyre.yaml', 'rt') as fin:
	text = fin.read()
data = yaml.load(text) # the true, faulse, on, off will be converted to boolean. Integer, string will be converted into equivalant python type
print(data)
print(data['details'])
print(len(data['poems']))
print(data['poems'][1]['title']) # use dict/list/dict to access the value of nested data

# use pickle() to serialize(convert data into file). pickle() could save and load any specfic binary format object
print()
import pickle
import datetime
now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)
print(now1)
print(now2)

class Tiny():
	def __str__(self):
		return 'tiny'
obj1 = Tiny()
print(obj1)
pickled = pickle.dumps(obj1) # pickled is a binary string made by obj1 
print(pickled)
obj2 = pickle.loads(pickled) # to make a dumplicate of obj1
print(obj2)
