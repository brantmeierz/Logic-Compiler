from enum import Enum
from symbols import Sym

class Token():
    
    def __init__(self, literal):
        this.literal = literal

class Parenthesis(Token):

    def __init__(self, type):
        this.type = type
        if type == Type.LEFT:
            super().__init__('(')
        elif type == Type.RIGHT:
            super().__init__(')')
    
    class Type(Enum):
        LEFT = 0
        RIGHT = 1
    
class Operator(Token):

    def __init__(self, type):
        this.type = type
        mapping = {
            Type.NOT: Sym.NOT_ANGLE
        }
        super().__init__(mapping[this.type])
        
    class Type(Enum):
        NOT = 0
        AND = 1
        OR = 2
        XOR = 3
        IMPLY = 4
        BICON = 5

# Replacement rules


print(Sym.POSSIBILITY_DIAMOND)

print(Sym.NOT_WEDGE)