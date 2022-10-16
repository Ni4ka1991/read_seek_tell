#! /usr/bin/env python3
from os import system

f = open('text.txt' , 'br' )

# Pavel's solution >>>

def read_by_10( file_obj ):
    i = file_obj.read(10)
    while len(i) > 0:
        print(i)
        i = file_obj.read(10)

read_by_10( f )

