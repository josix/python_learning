# python3 use two types eight bits iterger sequencee to store value from 0 to 256:
# (1) byte: is immutable(like byte's tuple)
# (2) bytearray: is mutable(like byte's list)

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)
the_bytearray = bytearray(blist)
print(the_bytearray)
try:
	the_bytes[1] = 127 # byte is immutable
except TypeError as err:
	print(err)

the_bytearray[0] = 127
print(the_bytearray)

# their storage range
the_bytes = bytes(range(256))
the_bytearray = bytearray(range(256))
print('bytes:\n{0}\nbytearray:\n{1}'.format(the_bytes, the_bytearray))
# python will print things that aren't printable in \x xx
# python will print printable things in ASCII

# use struct to convert binary data
print()
import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'# a valid PNG image token(8 bytes)
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
if data[:8] == valid_png_header:
	print(data[16:20])
	print(data[20:24])
	width, height = struct.unpack('>LL', data[16:24])
	# width is the 16-20 bytes , and height is 21-24 byte
	# >LL is a formated string, it instruct unpack() how to interpret bytes sequence.
	# > means that integer stored in big-endian format.
	# L represents a 4-byte no sign long integer
	print("valid PNG, width", width, 'height', height)
else:
	print("Not a valid PNG")

# use pack() to convert data to byte 
print(struct.pack('>L', 154))
print(struct.pack('>L', 141))

'''
> big endian
< little endian
'''

'''
x 		skip one bytes					1 byte
b 		sign byte						1
B		non-sign bytes					1
h 		sign short integer				2
H 		non-sign integer				2
i 		sign integer					4
I 		non-sign iterger				4
l 		sign long iterger				4
L	 	non-sign long iterger			4
Q		non-sign long long integer		8
f 		single-precision float			4
d 		double-precision float 			8
s 		char							number
'''
print(struct.unpack('>2L', data[16:24])) # you can add number before the specifier to represent the number of the assigned data
print(struct.unpack('>16x2L6x', data))

# use binascii() to convert byte/string
print()
import binascii
valid_png_header = b'\x89PNG\r\n\x1a\n'
print(binascii.hexlify(valid_png_header)) # convert the python bytes(mixed with ascii and \x xx) into hex
print(binascii.unhexlify(b'89504e470d0a1a0a'))