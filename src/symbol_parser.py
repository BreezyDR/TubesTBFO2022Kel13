import json
from src.file_reader import readFiles
from src.utility import sanitizeString
                                        
# def parseRules(file: list[str]) -> list[str]:
#     pass

def parseText(text: list[str]) -> list[str]:
    rules = json.loads(readFiles("src/json/grammar.json", True))

    terminal = rules["terminal"]
    grammar = rules["grammar"]

    keywords = terminal["keywords"]
    brackets = terminal["brackets"]
    operator = terminal["operator"]
    

    def isTerminal(val: str) -> bool:
        # butuh optimisasi baik dari fungsi maupun json structures
        # grammar
        for i in grammar:
            # print(rules["grammar"][i])
            if i in val.split(' ') or val.split(' ') in grammar[i]:
                return True
        
        #reserved keywords
        for i in terminal:
            for j in val.split():
                if j in terminal[i]:
                    return True
        
        # ops
        for i in operator:
            for j in operator[i]:
                if val == j:
                    return True

        #brackets
        for i in brackets:
            for j in brackets[i]:

                if val == j:
                    return True
        
        if val == '\n':
            return True
        
        return False
    
    def containsTerminal(text: list[str]):
        pass

    def parseBrackets(sentence: str) -> str:
        for i in terminal["brackets"]:
            for j in terminal["brackets"][i]:
                sentence = sentence.replace(j, " " + j + " ")
                

        return sentence

    def parseVariable(sentence: str) -> str:
        sentence = sanitizeString(sentence) #sanitization should be put last
        
        atoms = sentence.split(' ')
        

        for i in range(len(atoms)):
            if not isTerminal(atoms[i]) and atoms[i] != '':
                atoms[i] = "variable"

        return ' '.join(atoms)

    def parseRules(sentence: str) -> str:
        # fey = True
        # while(fey):
            for i in grammar:
                for j in grammar[i]:
                    # print(j, i)
                    sentence = sentence.replace(j, i)
                    # fey = False

            return sentence


    return [parseRules(parseVariable(parseBrackets(i))) for i in text]