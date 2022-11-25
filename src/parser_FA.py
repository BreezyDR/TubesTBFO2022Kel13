import re

from src.grammar import brackets, keywords
from src.Literal import Literal
from src.utility import sanitizeList, sanitizeString

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
            sentence = re.sub(rf'\b{keywords[i]}\b ', ' ', sentence)

        return sentence
    def parseIndividuals(sentence: str) :
        for i in known_variables:
            sentence = sentence.replace(i, ' ' + i + ' ')
        
        return sanitizeString(sentence).split(' ') + [';']

    def parse(text: list[str]) -> list[Literal]:
        text = [parseIndividuals(j) for j in sanitizeList([(removeReservedKeywords(removeParentheses(removeComment(i)))) for i in text])]
        text = [i for j in text for i in j]

        return text

    return parse(text)