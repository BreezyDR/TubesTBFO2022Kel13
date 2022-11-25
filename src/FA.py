#from src.grammar import *

arith_ops = ['+', '-', '*', '**', '/', '%', '++', '--']
logic_ops = ['&&', '||', '!']
nullish_ops = ['??']
assign_ops = ['=', '+=', '-=', '*=', '/=', '%=', ':']
comparison_ops = ['==', '===', '!=', '!==', '>', '<', '>=', '<=']
bitwise_ops = ['&', '|', '~', '^', '<<', '>>', '>>>']

def checkVarOps(array_of_words: list[str]) -> bool:
    # KAMUS LOKAL
    valid: bool
    firstVar: bool
    prevVar: bool
    op: bool
    icdcop: bool
    negop: bool
    notop: bool
    i: int
    length: int    

    # ALGORITMA
    valid = True
    firstVar = True
    prevVar = False
    op = False
    icdcop = False
    negop = False
    notop = False
    i = 0
    length = len(array_of_words)-1

    while (i < length and valid):
        if (isAssignOps(array_of_words, i) and not prevVar):
            firstVar = False
            if (op == True):
                valid = False
            else:
                op = True
                i = i + 2
        elif ((isArithOps(array_of_words, i) or isStringOps(array_of_words, i) or isBitOps(array_of_words, i)) and not prevVar):
            firstVar = False
            op = True
            if (array_of_words[i] == '++' or  array_of_words[i] == '--' or array_of_words[i+1] == '++' or  array_of_words[i+1] == '--'):
                icdcop = True
            elif (array_of_words[i] == '~'):
                negop = True
            i = i + 2
        elif (isVariable(array_of_words[i]) and (icdcop or notop or negop)):
            valid = False
        elif ((isCompareOps(array_of_words, i, icdcop) or isLogicOps(array_of_words, i, icdcop) or isCompareOps(array_of_words, i, notop) or isLogicOps(array_of_words, i, notop) or isCompareOps(array_of_words, i, negop) or isLogicOps(array_of_words, i, negop)) and not prevVar):
            firstVar = False
            op = True
            if (icdcop or negop or notop):
                i = i + 1
                icdcop = False
                negop = False
                notop = False
            else:
                if (array_of_words[i] == '!'):
                    notop = True
                i = i + 2
        elif (array_of_words[i+1] == '?' and not prevVar):
            if (not (isConditionalOps(array_of_words, i+1))):
                valid = False
            else:
                firstVar = False
                op = True
                i = i + 3
        elif ((isVariable(array_of_words[i]) or array_of_words[i].isdigit() or isString(array_of_words[i]) or isNull(array_of_words[i]) or isArray(array_of_words[i])) and (firstVar or op) and not icdcop and not notop and not negop):
            firstVar = False
            prevVar = True
            op = False
            i = i + 1
        elif (isVariable(array_of_words[i]) and not firstVar and not op):
            valid = False
        elif (array_of_words[i] == ';'):
            firstVar = True
            prevVar = False
            op = False
            icdcop = False
            negop = False
            notop = False
            i = i + 1
        else:
            valid = False

    return valid

def isVariable(word: str) -> bool:
    # KAMUS LOKAL
    isVar: bool
    i: int

    # ALGORITMA
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
            if (not (isVariable(arg2) or isString(arg2))):
                isValid = False
        elif (ops == '+='):
            if (not (isVariable(arg1) and (isVariable(arg2) or isString(arg2)))):
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
                if (not (isVariable(arg2) or arg2.isdigit() or isString(arg2) or isArray(arg2) or isNull(arg2))):
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

def isCompareOps(array_of_words: list[str], i : int, displacement: bool) -> bool:
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
    elif (displacement):
        if (arg1 in comparison_ops):
            arg2 = array_of_words[i+1]
            if (not (isVariable(arg2) or arg2.isdigit() or isString(arg2))):
                isValid = False            
        else:
            isValid = False
    else:
        isValid = False

    return isValid

def isLogicOps(array_of_words: list[str], i : int, displacement: bool) -> bool:
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
    elif displacement:
        if (arg1 in logic_ops):
            arg2 = array_of_words[i+1]
            if (not (isVariable(arg2) or arg2.isdigit() or isString(arg2))):
                isValid = False            
        else:
            isValid = False
    elif (arg1 == '!'):
        if (not (isVariable(ops) or ops.isdigit() or isString(ops))):
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

def isBitOps(array_of_words: list[str], i : int) -> bool:
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
        if (ops in bitwise_ops):
            arg2 = array_of_words[i+2]
            if (not (isVariable(arg2) or arg2.isdigit() or isString(arg2))):
                isValid = False
        else:
            isValid = False
    elif (arg1 == '~'):
        if (not (isVariable(ops) or ops.isdigit() or isString(ops))):
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

def isNull(arg: str) -> bool:
    return (arg == 'null')