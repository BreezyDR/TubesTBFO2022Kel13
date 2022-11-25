# debug doang, ntar dihapus
# act like a function driver
from src.CYK import cyk
from src.cfgtocnf import ConvertCFGtoCNF
from src.grammar import CFG_GRAMMAR


this_grammar = {'S' : [['A', 'B'], ['B', 'C']], 'A' : [['B', 'A'], ['a']], 'B' : [['C', 'C'], ['b']], 'C' : [['A', 'B'], ['a']]}
print(CFG_GRAMMAR)
print(this_grammar)
# print(ConvertCFGtoCNF(this_grammar)) #reference by address, take care
print(cyk(this_grammar, 'a b'))
print(cyk(CFG_GRAMMAR, 'ID ADD ID'))