#
class someByteObj:
    
    def __init__( self, dim ):
        self.dim = bytes( dim )
    
    
    def read( self, quantity ):
        print( hex( self.dim[ quantity ] )) 
    
    def seek():
        pass

    def tell():
        pass
    
    def edit( self, b ):
        self.dim = self.dim + b
    
    def __str__( self ):
        return f"My print >>> {self.dim }"
