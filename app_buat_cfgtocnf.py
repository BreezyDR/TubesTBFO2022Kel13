# ini cuma buat debugging, ntar dihapus
from src.cfgtocnf import ConvertCFGtoCNF

from src.grammar import CFG_GRAMMAR

if __name__ == "__main__":
    # print(CFG_GRAMMAR)
    print(ConvertCFGtoCNF(CFG_GRAMMAR))
    