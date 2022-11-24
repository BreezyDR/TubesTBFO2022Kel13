#from grammar import *

arith_ops = ['+', '-', '*', '**', '/', '%', '++', '--']
logic_ops = ['&&', '||', '!']
ternary_ops = ["ternary_operator"]
nullish_ops = ['??']
assign_ops = ['=', '+=', '-=', '*=', '/=', '%=', ':']
comparison_ops = ['==', '===', '!=', '!==', '>', '<', '>=', '<=']
bitwise_ops = ['&', '|', '~', '^', '<<', '>>', '>>>']

def isVariable(word: str) -> bool:
    isVar = True
    i = 1

    # Memeriksa karakter pertama dari string. jika karakter pertama bukan berupa huruf, $, atau _ maka string tersebut bukan variabel 
    if (word[0].isalpha() or word[0] == '$' or word[0] == '_'):
        # Memeriksa per karakter string. Jika karakter bukan huruf, $, _, atau digit maka string tersebut bukan variabel
        while (isVar and i < len(word)):
            if (word[i].isalpha() or word[i] == '$' or word[i] == '_' or word[i].isdigit()):
                i = i + 1
            else:
                isVar = False
    else:
        isVar = False
        
    return isVar

def isArithOps(array_of_words: list[str], i : int) -> bool:
    # KAMUS LOKAL
    isValid: bool
    arg1: str
    ops: str
    arg2: str
    
    # ALGORITMA
    isValid = True
    arg1 = array_of_words[i]
    ops = array_of_words[i+1]

    # Memeriksa operasi aritmetika selain pre increment dan pre decreement
    if ((isVariable(arg1) or arg1.isdigit()) and (ops != ';')):
        arg2 = array_of_words[i+2]
        if ((ops in arith_ops)):
            if (ops == '++' or ops == '--'):
                isValid = True
            elif (isVariable(arg2) or arg2.isdigit()):
                isValid = True
            else:
                isValid = False
        else:
            isValid = False
    # Memeriksa operasi aritmatika pre increment dan pre decrement
    elif (arg1 == '++' or arg1 == '--'): # Pada pre increment dan pre decreement, arg1 menjadi ops dan ops menjadi arg1
        if (not isVariable(ops)):
            isValid = False
    else:
        isValid = False

    return isValid

def isStringOps(array_of_words: list[str], i : int) -> bool:
    # KAMUS LOKAL
    isValid: bool
    arg1: str
    ops: str
    arg2: str
    
    # ALGORITMA
    isValid = True
    arg1 = array_of_words[i]
    ops = array_of_words[i+1]

    if ((isVariable(arg1) or isString(arg1)) and (ops != ';')):
        arg2 = array_of_words[i+2]
        if (ops == '+'):
            if (not (isVariable(arg2) or isVariable(arg2))):
                isValid = False
        elif (ops == '+='):
            if (not (isVariable(arg1) and (isVariable(arg2) or isVariable(arg2)))):
                isValid = False
        else:
            isValid = False
    else:
        isValid = False

    return isValid

def isAssignOps(array_of_words: list[str], i : int) -> bool:
    # KAMUS LOKAL
    isValid: bool
    arg1: str
    ops: str
    arg2: str
    
    # ALGORITMA
    isValid = True
    arg1 = array_of_words[i]
    ops = array_of_words[i+1]

    if (isVariable(arg1)):
        if (ops in assign_ops):
            arg2 = array_of_words[i+2]
            if (ops == '='):
                if (not (isVariable(arg2) or arg2.isdigit() or isString(arg2) or isArray(arg2))):
                    isValid = False
            elif (isVariable(arg2) or arg2.isdigit()):
                isValid = True
            else:
                isValid = False
        else:
            isValid = False
    else:
        isValid = False

    return isValid

def isCompareOps(array_of_words: list[str], i : int) -> bool:
    # KAMUS LOKAL
    isValid: bool
    arg1: str
    ops: str
    arg2: str
    
    # ALGORITMA
    isValid = True
    arg1 = array_of_words[i]
    ops = array_of_words[i+1]    

    if (isVariable(arg1) or arg1.isdigit() or isString(arg1)):
        if (ops in comparison_ops):
            arg2 = array_of_words[i+2]
            if (not (isVariable(arg2) or arg2.isdigit() or isString(arg2))):
                isValid = False
        else:
            isValid = False
    else:
        isValid = False

    return isValid

def isLogicOps(array_of_words: list[str], i : int) -> bool:
    # KAMUS LOKAL
    isValid: bool
    arg1: str
    ops: str
    arg2: str
    
    # ALGORITMA
    isValid = True
    arg1 = array_of_words[i]
    ops = array_of_words[i+1] 

    if (isVariable(arg1) or arg1.isdigit() or isString(arg1)):
        if (ops in logic_ops):
            arg2 = array_of_words[i+2]
            if (not (isVariable(arg2) or arg2.isdigit() or isString(arg2))):
                isValid = False
        else:
            isValid = False
    else:
        isValid = False

    return isValid

def isConditionalOps(array_of_words: list[str], i : int) -> bool:
    # KAMUS LOKAL
    isValid: bool
    ops1: str
    arg1: str
    ops2: str
    arg2: str
    
    # ALGORITMA
    isValid = True
    ops1 = array_of_words[i]    

    if (ops1 == '?'):
        arg1 = array_of_words[i+1]
        if (arg1.isdigit() or isVariable(arg1) or isString(arg1)):
            ops2 = array_of_words[i+2]
            if (ops2 == ':'):
                arg2 = array_of_words[i+3]
                if (not (arg2.isdigit() or isVariable(arg2) or isString(arg1))):
                    isValid = False
            else:
                isValid = False
        else:
            isValid = False
    else:
        isValid = False

    return isValid

def isTypeOps(array_of_words: list[str], i : int) -> bool:
    # KAMUS LOKAL
    isValid: bool
    ops: str
    arg: str
    
    # ALGORITMA
    isValid = True
    ops = array_of_words[i]
    arg = array_of_words[i+1]

    if (ops == 'typeof'):
        if (arg == ';'):
            isValid = False
    else:
        isValid = False

    return isValid

def isString(arg: str) -> bool:
    return (arg[0] == '"' and arg[len(arg)-1] == '"') or (arg[0] == "'" and arg[len(arg)-1] == "'")

def isBoolean(arg: str) -> bool:
    return (arg == 'false' or arg == 'true')

def isArray(arg: str) -> bool:
    return (arg[0] == '[' and arg[len(arg)-1] == ']')

var_pool = ["b", "=", '"true"', "==", "2"]
print(isAssignOps(var_pool, 0))