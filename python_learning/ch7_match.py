# Pattern Maching
# you have to define a string patter you want to match, and a objective string which is to matching
import re
result = re.match('You', 'Young Frankenstein') # 'You' is pattern, 'Young Frankenstein' is source
# match() will check if the source is beginnging with the assigned pattern
# another faster way
youpattern = re.compile('You') # compile your pattern will increase your vercity of matching  
result = youpattern.match('Young Frankenstein')

# use match() to get the matched element
import re
source = 'Young Frankenstein'
m = re.match('You', source) # match() will start from the begining of source
if m: # match() will retrun a object, and we see which elements are matched
	print(m.group())

m = re.match("^You", source) # do the same thing with the anchor(^)
if m:
	print(m.group())

m = re.match('Frank', source)
if m:
	print(m.group())
else:
	print("Nothing match") # because match just check the begining of source if matches the pattern

# correct
m = re.match('.*Frank', source)
if m:
	print(m.group())

# use search() to find the first one matched element
m = re.search('Frank', source)
if m: # search() return a object
	print(m.group())

# use findall() to match all
m = re.findall('n', source)
if m: # findall() will return a list
	print(m)
m = re.findall('n..', source)
if m:
	print(m)
m = re.findall('n.?', source)
if m :
	print(m)

# use split() to split
m = re.split('n', source)
if m:
	print(m)

# use sub() to replace matched element
m = re.sub('n', '?', source)
if m:
	print(m)

# Pattern : Metacharacter
'''
Metacharacters:

\d one number
\D one non-number
\w one alphanumeric
\W one non-alphanumeric
\s one space char
\S one non-space char
\b one word
\B one non-word
'''
# python string module have defined constant string
import string
printable = string.printable # printable contains the 100 printable ascii characters, like number, upper and lower alpha letter, punctuation
print(len(printable)) 
print(printable[:50])
print(printable[50:])

print(re.findall('\d', printable))
print(re.findall('\w', printable))
print(re.findall('\s',printable))

x = 'abc' + '-+*' + '\u00a2' + "\u20ac"
print(re.findall('\W', x)) # regular express is not only used for ascii

# Pattern : Specifier
print()
'''
pattern specifier:
abc					literal abc
(expr)				expr
expr1 | expr2		expr1 or expr2
. 					any char except \n
^					the begining of string
$					the ending of string
prev ? 				one or no prev
prev *				any number prev, the more the better
prev *?				any number prev, the less the better
prev + 				one or more prev, the more the better
prev +? 			one or more prev, the less the better
prev {m}			the m contiued prev
prev {m, n}			the m~n continued prev, the more the better
prev {m, n} 		the m~n continued prev, the less the better
[abc]				a or b or c
[^abc] 			not (a or b or c)
prev (?=next) 		prev, if following a next
prev (?!next) 		prev, if not following a next
(?<=prev) next		if prev is befer next, match next
(?<!prev) next 	if prev isn't before next, match next		
'''
source = '''I wish I may, I wish I might
Have a dish of fish tonight.'''
print(re.findall('wish', source))
print(re.findall('wish|fish', source))
print(re.findall('^wish', source))
print(re.findall('^I wish', source))
print(re.findall('fish$', source))
print(re.findall('fish tonight\.$', source)) # use \ to escape from re to represent the literal '.'
print(re.findall('[wf]ish', source))
print(re.findall('[wsh]+',source))
print(re.findall('[wsh]+?', source))
print(re.findall('ght\W', source))
print(re.findall('I (?=wish)', source))
print(re.findall('(?<=I) wish', source))

print(re.findall('\bfish',source))# the regualr express will comflict with python string's escape sequence
print(re.findall(r'\bfish', source))

# Pattern : Assign Matched Output
print()
m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group()) # when using search() or match(), they will return group().
print(m.groups()) # if you put pattern in (), they will return matched elements in tuple. And you could call them by groups()
m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source) # using (?P<NAME> expr) to store the matched elements in group NAME
print(m.group())
print(m.groups())
print(m.group('DISH'))
print(m.group('FISH'))