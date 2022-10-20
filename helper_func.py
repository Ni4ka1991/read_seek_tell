# Pavel's solution >>>

def read_by_10( file_obj ):
    i = file_obj.read(10)
    while len(i) > 0:
        print(i)
        i = file_obj.read(10)

def createBinFile():
    with open( "big.bin", 'wb' ) as fb:
        fb.write( b'\x80\x03]q\x00(K\x01\x88G@\x07\n=p\xa3\xd7\ne.' )
