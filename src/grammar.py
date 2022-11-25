import json
from src.file_reader import readFiles

data = json.loads(readFiles("src/json/grammar.json", True))
# NOTE: always put terminals with longer string bit more upper so it will be replaced first by parser
#       or in short, sort it by priority

# DONT IMPORT THESE
terminal    = data["terminal"] 
grammar     = data["grammar"] 

# IMPORT THESE INSTEAD
keywords    = terminal["keywords"]
brackets    = terminal["brackets"]
arith_ops   = terminal["arith_operator"]
logic_ops   = terminal["logic_operator"]
ternary_ops = terminal["ternary_operator"]
nullish_ops = terminal["nullish_operator"]
assign_ops  = terminal["assign_operator"]
comparison_ops = terminal["comparison_operator"]
bitwise_ops = terminal["bitwise_operator"]

CFG_GRAMMAR = {}

for i in grammar:
    CFG_GRAMMAR[i] = [[j] for j in grammar[i]]


