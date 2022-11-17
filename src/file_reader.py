from src.utility import sanitizeString

def readFiles(filename : str, raw: bool = False) -> list[str]:
    with open(filename) as file:
        if not raw:
            result = [sanitizeString(i) for i in file.readlines()]
        else:
            result = file.read()
            
    return result
