def sanitizeString(str: str) -> str:
    def sanitizeSpaces(str: str) -> str:
        while "  " in str:
            str = str.replace("  ", " ")

        return str

    return sanitizeSpaces(str.strip()) # TODO: reconsidering the usage of rstrip() over strip() to maintain \t inputs, 
                                        #       since it may leads to unwanted behaviors; NOTE: \t handling isnt rly needed for now
