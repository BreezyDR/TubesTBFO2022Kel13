from src.grammar import keywords, arith_ops, brackets, logic_ops, ternary_ops, nullish_ops

class Literal(str):
    # NOTE:
    # NEVER CAST ANY VARIABLE INTO THIS CLASS!
    # THE SOLE PURPOSE OF THIS CLASS IS TO EXTEND STR METHOD AND GIVE DEFINITION FOR ANNOTATION
    pass


# helper functions
# decided that we dont really need it to be inside the Literal class
def isLiteral(value: str) -> bool:
        return True

def isTerminal(val: Literal) -> bool:
    # reserved keywords
    for i in keywords:
        if val == i:
            return True
    
    # arith_ops
    for i in arith_ops:
        if val == i:
            return True

    # brackets
    for i in brackets:
        if val == i:
            return True

    # logic_ops
    for i in logic_ops:
        if val == i:
            return True

    # ternary_ops
    for i in ternary_ops:
        if val == i:
            return True

    # nullish_ops
    for i in nullish_ops:
        if val == i:
            return True
    
    # dont parse newline
    if val == '\n':
        return True
    

    #else
    return False
