#
class someByteObj:
    
    def __init__( self, dim ):
        self.dim = bytes( dim )
    
    
    def read( self, quantity ):
        if quantity == 1:
            print( self.dim[0] ) 
    
    def seek():
        pass

    def tell():
        pass
    
    def edit( self, x, b ):
        
        if x < len( self.dim ):
            self.dim[x] = b
        else:
            print( "Some error occurred!!" )
    
    def __str__( self ):
        return f"My print >>> {self.dim }"
