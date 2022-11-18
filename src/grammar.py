import json
from src.file_reader import readFiles

data = json.loads(readFiles("src/json/grammar.json", True))

# DONT IMPORT THESE
terminal = data["terminal"]
grammar = data["grammar"]


# IMPORT THESE INSTEAD
keywords = terminal["keywords"]
brackets = terminal["brackets"]
arith_ops = terminal["arith_operator"]
logic_ops = terminal["logic_operator"]
ternary_ops = terminal["ternary_operator"]
nullish_ops = terminal["nullish_operator"]




