# module is a python program file, data type is like a word, statement like is a sentence, function is like a paragraph, and module is like a chapter
# when we say this book inroduces somthing in chapter 3, in programm this is like we refer to other module code
# use 'import' to import other module's program and variable
import sys # sys is sys.py and omit '.py'
print('Program arguments:', sys.argv)

# two ways to import: see weatherman.py andd report.py
#(1) In the head, import module and use the dot notation(use 'as' to import module in alias e.g import report as wr)
#(2) import specific function or variable. e.g from random import choice 
for place in sys.path:
	print('the searching path:', place)
