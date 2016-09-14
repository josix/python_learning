# python3 use Unicode string.

# use \u and following four hexadecimal number to represent 256 BMP(Plane 0)
# first two number is plane number (00 is ASCII), and last two number is the index in that plane

# use \U and following eight hexadecimal number to represent higher planes' char, and leftest number must be zero
# all char could be represented by using \N{ name } to assign spefic name

# some functions in python's unicodedata module help us to convert
# lookup() name()

def unicode_test(value):
	import unicodedata
	name = unicodedata.name(value)
	value2 = unicodedata.lookup(name)
	print('value = "%s", name = "%s", value2 = "%s"' %(value, name, value2))

unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u20ac')
try:
	unicode_test('\u2603')
except UnicodeEncodeError as err: 
	print(err)
	
# when you are exchanging data with others, you need to do something :
# (1) to ecode char and string in byte
# (2) to decode byte in char and string
# UTF-8 is a dynamic encoding format. It let all unicode char use 1 to 4 bytes
# UTF-8 is standard text encodng of python, linux, HTML. It is the fastest, most complete format.

# use encode() to encode
print()
snowman = '\u2603'
print(len(snowman))
ds = snowman.encode('utf-8') # the first argument is the encoding name, like utf-8, ascii, latin-1, cp-1252, unicode-escape
print(ds, ':', len(ds), type(ds))

try:
	ds = snowman.encode('ascii')
except UnicodeEncodeError as err:
	print(err)

# the second argument help you avoid the encoding exception, its default is 'strict' and it will cause error when the char is not ascii char
ignore = snowman.encode('ascii', 'ignore') # ignore the unknow char
print(ignore)

replace = snowman.encode('ascii', 'replace') # replace the unknow char with '?'
print(replace)

backslashreplace = snowman.encode('ascii', 'backslashreplace') # replace the unknow char with python unicode string
print(backslashreplace)

# use decode() to decode
# you have to know what encoding format the bytes string use so you can decode it in original string
#( However, we can distinguish the encoding formats the bytes strings use )
place = 'caf\u20ac'
print(place, type(place))
place_bytes = place.encode('utf-8')
print(place_bytes) # six bytes
place2 = place_bytes.decode('utf-8') # must use the same encoding format
print(place2)

try: 
	place3 = place_bytes.decode('ascii')
except UnicodeDecodeError as  err:
	print(err)

# formatted output
# the old way: string % data 
print('%s' %42)
print('%d' %42)
print('%x' %42)
print('%o' %42)
'''
%s string
%d decimal
%x hexdecimal
%o octal
%f decimal float
%e exponent and float
%g decimal or float
%% the true '%'
'''
print('%s' %7.03)
print('%f' %7.03)
print('%e' %7.03)
print('%g' %7.03)

print('%d%%' %100)

# combine string with integer
actor = 'Richard Gere'
cat = 'Chester'
weight = 28
print("My wife's favorite acotr is %s" %actor)
print("Our cat %s weight %d pounds" %(cat, weight)) # more than one data elements need to put in tuple to unpack

# put some number in between % and specifier to set the maximum and minimum width
n = 42
f = 7.03
s = 'string cheese'
print('%d %f %s' %(n, f, s))
print("%10d %10f %10s" %(n, f, s)) # setting maximum width = 10
print("%-10d %-10f %-10s" %(n, f, s))# setting left
print("%10.4d %10.4f %10.4s" %(n, f, s)) # setting the maximum  char output = 4
print("%.4d %.4f %.4s" %(n, f, s)) # no maximum width
print("%*.*d %*.*f %*.*s" %(10, 4, n, 10, 4, f, 10, 4, s))

# the new way: using {} and format
print()
print("{} {} {}".format(n, f, s))
print("{} {} {}".format(f, n, s))
print("{n} {f} {s}".format(n = 4, f =1.3, s = 'test')) # you can use dict or named argument, and add their name in specifier
d = {'n' : 42,
	 'f' : 7.03,
	 's' : 'string cheese'}
print("{0[n]} {0[f]} {0[s]} {1}".format(d, 'other')) # {0} is all dict, {1} is 'other'
print("{0:d} {1:f} {2:s}".format(n, f, s)) # put type specifier behind colon
print("{n:d} {f:f} {s:s}".format(n = 23, f = 3.2, s = 'test'))
print("{0:10d} {1:10f} {2:10s}".format(n, f, s))
print("{0:>10d} {1:>10f} {2:>10s}".format(n, f, s)) # right
print("{0:<10d} {1:<10f} {2:<10s}".format(n, f, s)) # left
print("{0:^10d} {1:^10f} {2:^10s}".format(n, f, s)) # center
print("{0:>10d} {1:>10.4f} {2:>10.4s}".format(n, f, s)) # setting the maximum of char output and the accuracy of float
print("{:!^20s}".format('BIG ISSUE')) # setting the fill character