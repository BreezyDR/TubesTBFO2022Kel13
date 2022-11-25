from src.grammar import keywords, arith_ops, brackets, logic_ops, ternary_ops, nullish_ops, assign_ops, comparison_ops, bitwise_ops, line_termination

class Literal(str):
    # NOTE:
    # NEVER CAST ANY VARIABLE INTO THIS CLASS!
    # THE SOLE PURPOSE OF THIS CLASS IS TO EXTEND STR METHOD AND GIVE DEFINITION FOR ANNOTATION
    pass


# helper functions
# decided that we dont really need it to be inside the Literal class
def isLiteral(value: Literal) -> bool:
        return True

def isTerminal(val: Literal) -> bool:
    # reserved keywords
    for i in keywords:
        if val == i:
            return True

    # brackets
    for i in brackets:
        if val == i:
            return True
    
    # operators
    every_ops = arith_ops | logic_ops | ternary_ops | nullish_ops | assign_ops | comparison_ops | bitwise_ops  # NOTE: watch for new operators to be added in the future!
    for i in every_ops:
        if val == i:
            return True
        

    for i in line_termination:
        if val == i:
            return True
    
    # dont parse newline
    if val == '\n' or val == 'ID':
        return True
    

    #else
    return False
