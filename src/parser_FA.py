import re

from src.grammar import brackets, keywords
from src.Literal import Literal
from src.utility import sanitizeList, sanitizeString
from src.grammar import *


# TODO: variable name is still parsed
# TODO: parse objects
def extractExpression(text: list[str], known_variables: list[Literal] = []):
    # how this works
    # 1. it accepts list of known_variables
    # 2. every variables will have itself distanced from any other element around them for 1 space
    # 3. split by 1 space
    # 4. return the result

    def removeComment(sentence : str):
        sentence = re.sub(r'(?:\/\*(?:[^\*]|\**[^\*\/])*\*+\/)|(?:\/\/[\S ]*)', ' ', sentence)
        
        return sentence
    def removeParentheses(sentence : str):
        for i in brackets:
            sentence = sentence.replace(brackets[i], ' ') # remove
        
        return sentence    
    def removeReservedKeywords(sentence : str):
        for i in keywords:
            if keywords[i] != 'false' and keywords[i]  != 'true':
                sentence = re.sub(rf'\b{keywords[i]}\b ', ' ', sentence)

        return sentence
        
    def parseIndividuals(sentence: str) :
        for i in known_variables:
            # sentence = sentence.replace(i, ' ' + i + ' ')
            # print(i, 'ini')
            sentence = re.sub(fr'\b{i}\b', f' {i} ', sentence)
        
        return sanitizeString(sentence).split(' ') + [';']
    def parseOperators(sentence: str) -> str:
        every_ops = arith_ops | logic_ops | ternary_ops | nullish_ops | assign_ops | comparison_ops | bitwise_ops  # NOTE: watch for new operators to be added in the future!
        
        every_ops = dict(sorted(every_ops.items(), key=lambda x: len(x[1]), reverse=True)) # NOTE: making sure that the ops are sorted descendingly by length
        # print(every_ops, 'ev-ops')

        for i in every_ops :
            sentence = sentence.replace(every_ops[i], " " + every_ops[i] + " ")

        return sentence
    def parseComma(sentence: str) -> str:
        sentence = sentence.replace(',', ';').replace('!', '')

        return sentence

    def parse(text: list[str]) -> list[Literal]:
        # print(text)
        text = [parseIndividuals((j)) for j in sanitizeList([parseComma(removeReservedKeywords(removeParentheses(removeComment(i)))) for i in text])]
        # print(text)
        text = [(i).strip('\"').strip("\'") for j in text for i in j]
        # print(text)

        return text

    return parse(text)