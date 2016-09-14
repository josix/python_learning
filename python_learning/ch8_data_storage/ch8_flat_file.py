# the simplest persist mechanism is using flat file
# flat file is using a file name to store a byte sequence
# when you want to read a file, you will put it in memory, and then write the content of the memory into a file
  
'''
open a file

FILEOBJ = open(FILENAME, MODE)

# FILEOBJ is a object return by open() 
# FILENAME is the string name of this file
# MODE is a string which is used to instruct the type of file, and what to do.

the first word of MODE(operating) : 
	r 		read
	w 		write(if file is not existing, it will create one. Conversely, it will override it)
	x 		write(only for the file is not existing)
	a 		append(if file is existing)

the second word of MODE(typing of file):
	t(or omission)	a text file
	b 				a binary file

open file -> read/write(call function) -> close file
'''

poem = '''There was a younf lady named Bright,
Whose speed was far faster than light;
she started one day
In a relative way,
And returned on the previous night.'''

print(len(poem))

fout = open('relativity', 'wt')
print(fout.write(poem))# write() will return the written bytes  
fout.close()

fout = open('relativity_2', 'wt')
print(poem, file = fout) # you can also use print() to print to the text file
fout.close()
# the difference between print() and write() is that print() will add space between every quotation, and put new line at the end
# To make these two the same by adding two argument, sep (default is ' ')and end(default is '\n')
fout = open('relativity_3', 'wt')
print(poem, file = fout, sep = '', end = '')
fout.close()

# segmented writing
fout = open('relativity_4', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
	if offset > size:
		break
	print(fout.write(poem[offset:offset+chunk]))
	offset += chunk
fout.close()

# use mode x to avoid overriding it
try:
	fout = open('relativity', 'xt')
	fout.write('test')
except FileExistsError:
	print('relativity already exists!. That was a close one')

# use read() readline() readlines() to read text file
print()
fin = open('relativity', 'rt')
poem = fin.read() # read() will take all file a time( Be careful with the big file)
fin.close()
print(poem, ' (', len(poem), ')', sep = '')

# you can provide maximium char number to restrict the number that read() return everytime
print()
poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
	fragment = fin.read(chunk)
	if not fragment:
		break # when you read until the end, read() will return empty string
	poem += fragment
	print(poem, ' (', len(poem), ')', sep = '')
fin.close()

# use readline() to read a file
print()
poem = ''
fin = open('relativity', 'rt')
while True:
	line = fin.readline()
	if not line:
		break # readline() will also retun empty string when the file is end
	poem += line
	print(poem, ' (', len(poem), ')', sep = '')
fin.close()

# the simplest way to read file is using iterator:
print()
poem = ''
fin = open('relativity', 'rt')
for line in fin: # return one line a time
	poem += line
	print(poem, ' (', len(poem), ')', sep = '')
fin.close()

# readlines() will read one line and return one line string
print()
fin = open('relativity', 'rt')
lines = fin.readlines() # it will return a list
fin.close()
print(len(lines), 'lines read')
for line in lines:
	print(line, end = '')

# use write() to write binary file
print()
print()
bdata = bytes(range(256))
print(len(bdata))
fout = open('bfile', 'wb')
print(fout.write(bdata))
fout.close()

print()
fout = open("bfile_2", 'wb')
offset = 0
chunk = 100
size = len(bdata)
while True:
	if offset > size:
		break
	print(fout.write(bdata[offset:offset+chunk]))
	offset += chunk

fout.close()

# use read() to read binary file
print()
fin = open('bfile', 'rb')
bdata = fin.read()
fin.close()
print(bdata, len(bdata))

# use 'with' to close file automaticlly
# when you forget to close opening file and python won't refer to it again, it will close.
print()
with open('relativity', 'rt') as fin:
	poem = fin.read()
	print(poem)
# when you are out of the indentation, the file will close

# use seek() to change position
# when you are doing reading or writing file, python will trace your position.
# tell() will return the current index counting from the begining of file
# seek() will let you jump to the another byte's index in the same file
print()
fin = open('bfile', 'rb')
print(fin.tell())
print(fin.seek(255)) # seek() will also return current index
bdata = fin.read()
fin.close()
print(bdata[0], len(bdata))

# you can use the second argument: seek(offset, origin)
# if origin is 0(default), forward to the 'offset' bytes from begining
# if origin is 1, forward to the 'offset' bytes from current position
# if origin is 2, forward  to the index which is relative 'offset' bytes to the end
print()
import os # stardand os module also define these value
print(os.SEEK_SET, os.SEEK_CUR, os.SEEK_END)

print()
fin = open('bfile', 'rb')
fin.seek(-1, 2)# go to the last byte 
print(fin.tell())
bdata = fin.read()
print(len(bdata), bdata[0])	
fin.close()

print()
fin = open('bfile', 'rb')
fin.seek(254, 0)
print(fin.tell())
fin.seek(-1, 1)
print(fin.tell())
bdata = fin.read()
print(bdata)

# these function is suitable for using in binary file.
# Because you need to calculate how many bytes you need to forward
# (for those popular encoding system like utf-8, every char could use different bytes)
# (except ascii) 