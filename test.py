#! /usr/bin/env python3

from os import system

f = open('text.txt' , 'br' )

system("clear")
i = f.read(40)
print( f"i(40) >>> {i}" )
f.close()

