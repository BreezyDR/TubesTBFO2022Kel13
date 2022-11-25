def sanitizeString(str: str) -> str:
    def sanitizeSpaces(str: str) -> str:
        while "  " in str:
            str = str.replace("  ", " ")

        return str

    return sanitizeSpaces(str.strip()) # TODO: reconsidering the usage of rstrip() over strip() to maintain \t inputs, 
                                        #       since it may leads to unwanted behaviors; NOTE: \t handling isnt rly needed for now

def sanitizeList(list: list[str]):
    return [(i).strip() for i in list if (i).strip() != '']

def isATerminal(string):
    terminal_array = [] # Nanti isi sama daftar string terminal
    return string in terminal_array

def isAVariable(string):
    return not isATerminal(string)