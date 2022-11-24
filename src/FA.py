# from parser_symbol import *

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
        if (ops == '+' or ops == '-' or ops == '*' or ops == '**' or ops == '/' or ops == '%' and i+2 < len(array_of_words)):
            arg2 = array_of_words[i+2]
            if (not (isVariable(arg2) or arg2.isdigit())):
                isValid = False
        elif (ops == '++' or ops == '--' and isVariable(arg1)):
            if (i+2 < len(array_of_words)):
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

def isAssignOps() -> bool:
    isValid = True

    return isValid

def isCompareOps() -> bool:
    isValid = True

    return isValid

def isLogicOps() -> bool:
    isValid = True

    return isValid

def isConditionalOps() -> bool:
    isValid = True

    return isValid

def isTypeOps() -> bool:
    isValid = True

    return isValid

var_pool = ["a", "++", "b", "++"]
print(isArithOps(var_pool, 0))