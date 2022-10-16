#! /usr/bin/env python3

from os import system

f = open('text.txt' , 'r' )

system("clear")
end = ""
i = 0
bytes_count = 0
while i != end:
    i = f.read(1)
    b = i.encode('utf-16')
    int_val = int.from_bytes( b, "big" )
    bytes_count += int_val
    print( f"char{type(i)} >>> {i}  :   bytes in hex{type(b)} >>> {b} : int value >>> {int_val}" )
#print( f"curent bytes count >>> {bytes_count/1024/1024} Mb" )

f.close()
