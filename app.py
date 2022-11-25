from src.file_reader import readFiles

from src.parser_symbol import parseText
from src.parser_FA import extractExpression
from src.cfgtocnf import ConvertCFGtoCNF
from src.CYK import cyk
from src.FA import checkVarOps

from src.utility import sanitizeString

from src.grammar import CFG_GRAMMAR

if __name__ == "__main__":
    file : list[str] = readFiles("./toread.js")

    # # print("\t((raw text))")
    # # for i in file:
    # #     print(i)

    # parsed_symbols, parsed_variables = parseText(file)
    # print(parsed_variables)


    # print('\n\n\t((parsed text))')
    # for i in parsed_symbols:
    #     print(i)
    
    # print(checkVarOps([extractExpression(file, parsed_variables)]))
    


    # print(grammar)
    # print(CFG_GRAMMAR)
    # print(ConvertCFGtoCNF(CFG_GRAMMAR))

    nyoba = readFiles("./nyoba.js")

    nyoba_ps, nyoba_pv = parseText(nyoba)
    # print(' '.join(nyoba_ps))
    '''and checkVarOps([extractExpression(nyoba, nyoba_pv)])'''
    if(cyk(ConvertCFGtoCNF(CFG_GRAMMAR), sanitizeString(' '.join(nyoba_ps))) ):
        print("ACCEPTED")
    else:
        print("REJECTED")
    
    

