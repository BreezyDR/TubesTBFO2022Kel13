import json
from src.file_reader import readFiles
from src.utility import sanitizeString
                                        
def parseRules(file: list[str]) -> list[str]:
    pass

def parseText(text: list[str]) -> list[str]:
    rules = json.loads(readFiles("src/json/grammar.json", True))

    terminal = rules["terminal"]
    grammar = rules["grammar"]

    def isTerminal(val: str) -> bool:
        # butuh optimisasi baik dari fungsi maupun json structures
        for i in grammar:
            # print(rules["grammar"][i])
            if i in val.split(' ') or val.split(' ') in grammar[i]:
                return True
        
        for i in terminal:
            for j in val.split():
                if j in terminal[i]:
                    return True
        
        if val == '\n':
            return True
        
        return False
    
    def containsTerminal(text: list[str]):
        pass

    def parseVariable(atom: str) -> str:
        atom = sanitizeString(atom)
        
        temp_result = atom.split(' ')
        

        for i in range(len(temp_result)):
            if not isTerminal(temp_result[i]):
                temp_result[i] = "variable"

        return ' '.join(temp_result)


    return [parseVariable(i) for i in text]