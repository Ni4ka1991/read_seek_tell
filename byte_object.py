#
class someByteObj:
    
    def __init__( self, dim ):
        self.dim = bytes( dim )
    
    
    def read( self, quantity = None ):
        
        if quantity == None:
            print( self.dim )
        
        elif( quantity > len( self.dim )):
            raise ValueError( "Your number out of range" )
        
        else:
            i = 0
            while i <= quantity:
                print( hex(self.dim[i] ), end = '' )
                i += 1
            print()

    def seek():
        pass

    def tell():
        pass
    
    def edit( self, b ):
        self.dim = self.dim + b
    
    def __str__( self ):
        return f"My print >>> {self.dim }"
