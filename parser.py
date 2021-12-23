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


# Syntax replacements
# |- to ⊢
# -> to →
syn_repl = [
    ['|-', '⊢'],
    ['|=', '⊨'],
    ['->', '→'],
    ['/\\', '∧'],
    ['\\/', '∨'],
    ['=>', '⇒'],
    ['<=>', '⇔'],
    ['<->', '⇔'],
    ['_|_', '⊥'],
    [' or ', '∨'],
    [' and ', '∧'],
    [' implies ', '→'],
    ['not ', '¬'],
    [' xor ', '⊕'],
    #['for all ', '∀'],
]
def first_pass(input_string):
    for rule in syn_repl:
        input_string = input_string.replace(rule[0], rule[1])
    return input_string

def tokenize(input_string):
    token_list = []
    for i in input_string:
        if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            token_list.append({'type': 'VAR', 'val': i})
        elif i in '(':
            token_list.append({'type': 'LPAREN', 'val': i})
        elif i in ')':
            token_list.append({'type': 'RPAREN', 'val': i})
        elif i in '+-∨∧→⇒⇔⊕⊻=&':
            token_list.append({'type': 'BINOP', 'val': i})
        elif i in '~∀∃∄¬':
            token_list.append({'type': 'UNOP', 'val': i})
        else:
            token_list.append({"type": 'UNKN', 'val': i})
    return token_list

input_string = '(A or B) xor (A and B) implies C'
post_replace = first_pass(input_string)
token_list = tokenize(post_replace)

print(input_string)
print(post_replace)
print(token_list)

#parse_string = "<>"


#print(Sym.POSSIBILITY_DIAMOND)

#print(Sym.AND_WEDGE)