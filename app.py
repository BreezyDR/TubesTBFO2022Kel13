from src.file_reader import readFiles

from src.parser_symbol import parseText
from src.parser_FA import extractExpression
from src.cfgtocnf import ConvertCFGtoCNF
from src.CYK import cyk
from src.FA import checkVarOps

from src.utility import sanitizeString

from src.grammar import CFG_GRAMMAR

if __name__ == "__main__":
    nyoba = readFiles("./nyoba.js")

    nyoba_ps, nyoba_pv = parseText(nyoba)
    
    if(cyk(ConvertCFGtoCNF(CFG_GRAMMAR), sanitizeString(' '.join(nyoba_ps))) and checkVarOps([extractExpression(nyoba, nyoba_pv)])):
        print("Accepted")
    else:
        print("Syntax Error")
    
    

