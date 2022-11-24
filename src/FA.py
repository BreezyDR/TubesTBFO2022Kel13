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
    isValid = True
    arg1 = array_of_words[i]

    # Memeriksa operasi aritmetika selain pre increment dan pre decreement
    if ((isVariable(arg1) or arg1.isdigit()) and (i+1 < len(array_of_words))):
        ops = array_of_words[i+1]
        if (ops == '++' or ops == '--' and isVariable(arg1)):
            if (i+2 < len(array_of_words)):
                isValid = False
        elif ((ops in arith_ops) and (i+2 < len(array_of_words))):
            arg2 = array_of_words[i+2]
            if (not (isVariable(arg2) or arg2.isdigit())):
                isValid = False
        else:
            isValid = False
    # Memeriksa operasi aritmatika pre increment dan pre decrement
    elif (arg1 == '++' or arg1 == '--'):
        if (i+1 < len(array_of_words)):
            arg = array_of_words[i+1]
            if (not isVariable(arg)):
                isValid = False
    else:
        isValid = False

    return isValid

def isAssignOps(array_of_words: list[str], i : int) -> bool:
    isValid = True
    arg1 = array_of_words[i]
    ops = array_of_words[i+1]
    arg2 = array_of_words[i+2]

    if (isVariable(arg1)):
        if (ops in assign_ops):
            if (not (isVariable(arg2) or arg2.isdigit() or isArithOps(array_of_words, i+2))):
                isValid = False
        else:
            isValid = False
    else:
        isValid = False

    return isValid

def isCompareOps(array_of_words: list[str], i : int) -> bool:
    isValid = True
    arg1 = array_of_words[i]
    ops = array_of_words[i+1]
    arg2 = array_of_words[i+2]    

    if (isVariable(arg1) or arg1.isdigit()):
        if (ops in comparison_ops):
            if (not (isVariable(arg2) or isArithOps(array_of_words, i+2) or arg2.isdigit())):
                isValid = False
        else:
            isValid = False
    else:
        isValid = False

    return isValid

def isLogicOps(array_of_words: list[str], i : int) -> bool:
    isValid = True
    arg1 = array_of_words[i]
    ops = array_of_words[i+1]
    arg2 = array_of_words[i+2] 

    if (isVariable(arg1) or arg1.isdigit()):
        if (ops in logic_ops):
            if (not (isVariable(arg2) or arg2.isdigit())):
                isValid = False
        else:
            isValid = False
    else:
        isValid = False

    return isValid

def isConditionalOps(array_of_words: list[str], i : int) -> bool:
    isValid = True
    ops1 = array_of_words[i]
    arg1 = array_of_words[i+1]
    ops2 = array_of_words[i+2]
    arg2 = array_of_words[i+3]    

    if (ops1 == '?'):
        if (arg1.isdigit() or isVariable(arg1) or isString(arg1)):
            if (ops2 == ':'):
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
    isValid = True
    ops = array_of_words[i]
    arg = array_of_words[i+1]

    if (ops == 'typeof'):
        if (array_of_words[i+1] == ';'):
            isValid = False
    else:
        isValid = False

    return isValid

def isString(arg: str) -> bool:
    return (arg[0] == '"' and arg[len(arg)-1] == '"') or (arg[0] == "'" and arg[len(arg)-1] == "'")


var_pool = ["s", "+", "1", "==", "2"]
print(isCompareOps(var_pool, 0))