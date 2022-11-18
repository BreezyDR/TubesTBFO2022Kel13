from src.file_reader import readFiles
from src.parser_symbol import parseText


if __name__ == "__main__":
    file : list[str] = readFiles("./toread.js")

    print("\t((raw text))")
    for i in file:
        print(i)

    file = parseText(file)


    # ## TODO: parse brackets!
    # ## TODO: problems with empty line parsed as variable
    print('\n\n\t((parsed text))')
    for i in file:
        print(i)

    
    



    
    