import json

def sanitizeString(str: str) -> str:
    def sanitizeSpaces(str: str) -> str:
        while "  " in str:
            str = str.replace("  ", " ")

        return str

    return sanitizeSpaces(str.strip()) # TODO: reconsidering the usage of rstrip() over strip() to maintain \t inputs, 
                                        #       since it may leads to unwanted behaviors; NOTE: \t doesnt even needed
                                        

def readFiles(filename : str, raw: bool = False) -> list[str]:
    
    with open(filename) as file:
        if not raw:
            result = [sanitizeString(i) for i in file.readlines()]
        else:
            result = file.read()
            
    return result

def parseRules(file: list[str]) -> list[str]:
    pass

def parseText(text: list[str]) -> list[str]:
    rules = json.loads(readFiles("./src/json/grammar.json", True))

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


if __name__ == "__main__":
    # prone to inoptimal reduction
    # needs a lot of improvements
    file : list[str] = readFiles("./toread.js")

    for i in file:
        print(i)

    file = parseText(file)

    ## TODO: parse brackets!
    ## TODO: problems with empty line parsed as variable
    for i in file:
        print(i)
    
    