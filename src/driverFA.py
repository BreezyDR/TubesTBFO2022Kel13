from FA import *

var_pool = ['word', '=', '"moe"', ';', 'word', '+=', '"moe kyun"', ';']
#print(checkVarOps(var_pool))

if (checkVarOps(var_pool)):
    print("Accepted")
else:
    print("Syntax Error")