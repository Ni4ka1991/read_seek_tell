#! /usr/bin/env python3
from os import system
from byte_object import *
'''
f = open('text.txt' , 'br' )

# Pavel's solution >>>

def read_by_10( file_obj ):
    i = file_obj.read(10)
    while len(i) > 0:
        print(i)
        i = file_obj.read(10)

read_by_10( f )
'''
system("clear")
b = someByteObj(5)
print(b)
nb = b'\x05\x97\xa3'
b.edit( nb )
print( f"edited b >>> {b} " )
print( "*"*10 )

b.read()
b.read(2)
b.read(6)
print()
print("There will be an Error >>>")
print()
b.read(23)
