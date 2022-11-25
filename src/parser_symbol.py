import re

from src.file_reader import readFiles
from src.utility import sanitizeString
from src.Literal import Literal, isTerminal

from src.grammar import keywords, brackets, arith_ops, logic_ops, ternary_ops, nullish_ops, assign_ops, comparison_ops, bitwise_ops
                                    
def parseText(text: list[str]) -> tuple[list[str], list[Literal]]:
    variable_pool = []
    in_a_comment = False

    # def isTerminal(val: str) -> bool:
        # check Literal.py
    
    def containsTerminal(text: list[str]):
        pass

    # def parseCommentSingle(sentence: str) -> str:
    #     if sentence.find("//") != -1 :
    #         sentence = sentence.split("//")[0] # we are supposed to ignore it so it wont distrupt the program flow
        
    #     sentence = re.sub("\\\*(.*)\*\\\"", " str_val ", sentence)
        
    #     return sentence

    # def parseCommentMulti(sentence: str) -> str:
    #     if not in_a_comment:
    #         if sentence.find("/*") != -1:
    #             if sentence.find("*/") == -1: #missing ending
    #                 in_a_comment = True
    #             sentence = sentence.split("/*")[0]
    #     else :
    #         if sentence.find("*/") != -1:
    #             sentence = sentence.split("*/")[1:]
    #             in_a_comment = False
    def removeComment(sentence : str):
        sentence = re.sub(r'(?:\/\*(?:[^\*]|\**[^\*\/])*\*+\/)|(?:\/\/[\S ]*)', ' ', sentence)
        
        return sentence
                

    def parseStaticString(sentence: str) -> str:
        formula = r'(?:\'(?:[^\*]|\**[^\*\/])*\')|(?:\"(?:[^\*]|\**[^\*\/])*\")|(?:\`(?:[^\*]|\**[^\*\/])*\`)'
        found_string = re.findall(formula, sentence)
        sentence = re.sub(formula, " str_val ", sentence)
        # NOTE: unstable regex formula
        # NOTE: regex should be allowed

        for i in found_string:
            if i not in variable_pool:
                variable_pool.append(i)

        return sentence

    def parseKeywords(sentence: str) -> str:
        for i in keywords:
            sentence = sentence.replace(" " + keywords[i] + " ", " " + i + " ")
        
        return sentence

    def parseBrackets(sentence: str) -> str:
        for i in brackets:
            sentence = sentence.replace(brackets[i], " " + i + " ")
                
        return sentence

    def parseOperators(sentence: str) -> str:
        every_ops = arith_ops | logic_ops | ternary_ops | nullish_ops | assign_ops | comparison_ops | bitwise_ops  # NOTE: watch for new operators to be added in the future!
        
        every_ops = dict(sorted(every_ops.items(), key=lambda x: len(x[1]), reverse=True)) # NOTE: making sure that the ops are sorted descendingly by length
        # print(every_ops, 'ev-ops')

        for i in every_ops :
            sentence = sentence.replace(every_ops[i], " " + i + " ")

        return sentence
    

    
    # parseVariable should always be the last method called
    def parseVariable(sentence: str) -> str:
        sentence = sanitizeString(sentence) # TODO: sanitization should actually be put last
                                            # but here, we actually needed it befor split()
        
        literal : Literal = sentence.split(' ')        

        for i in range(len(literal)):
            if (not isTerminal(literal[i]) and literal[i] != '' and literal[i] != "str_val"):
                if literal[i] not in variable_pool:
                    variable_pool.append(literal[i])
                
                # TODO: numeric constant will still be marked as vairable
                literal[i] = "variable_" + str(variable_pool.index(literal[i]))
        

        return ' '.join(literal)

    # TODO: nullish and ternary operator will scuff the result, need to handle it later
    return [parseVariable(parseKeywords(parseBrackets(parseOperators(parseStaticString(removeComment((" " + i + " "))))))) for i in text], variable_pool