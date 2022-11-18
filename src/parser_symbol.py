import json
from src.file_reader import readFiles
from src.utility import sanitizeString
from src.Literal import Literal, isTerminal

from src.grammar import keywords, brackets, arith_ops, logic_ops, ternary_ops, nullish_ops, assign_ops
                                    
def parseText(text: list[str]) -> list[str]:
    # def isTerminal(val: str) -> bool:
        # check Literal.py
    
    def containsTerminal(text: list[str]):
        pass

    def parseKeywords(sentence: str) -> str:
        for i in keywords:
            sentence = sentence.replace(keywords[i], " " + i + " ")
        
        return sentence

    def parseBrackets(sentence: str) -> str:
        for i in brackets:
            sentence = sentence.replace(brackets[i], " " + i + " ")
                
        return sentence

    def parseOperators(sentence: str) -> str:
        every_ops = arith_ops | logic_ops | ternary_ops | nullish_ops | assign_ops # NOTE: watch for new operators to be added in the future!
        # print(every_ops)

        for i in every_ops :
            sentence = sentence.replace(every_ops[i], " " + i + " ")

        return sentence
    

    variable_pool = []
    # parseVariable should always be the last method called
    def parseVariable(sentence: str) -> str:
        sentence = sanitizeString(sentence) # TODO: sanitization should actually be put last
                                            # but here, we actually needed it befor split()
        
        literal = sentence.split(' ')        

        for i in range(len(literal)):
            if not isTerminal(literal[i]) and literal[i] != '':
                if literal[i] not in variable_pool:
                    variable_pool.append(literal[i])
                
                # TODO: numeric constant will still be marked as vairable
                literal[i] = "variable_" + str(variable_pool.index(literal[i]))
        

        return ' '.join(literal)


    # TODO: nullish and ternary operator will scuff the result, need to handle it later
    return [parseVariable(parseKeywords(parseBrackets(parseOperators(i)))) for i in text]