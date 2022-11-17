from src.file_reader import readFiles
from src.symbol_parser import parseText


if __name__ == "__main__":
    # prone to inoptimal reduction
    # needs a lot of improvements
    file : list[str] = readFiles("./toread.js")

    print("\t((raw text))")
    for i in file:
        print(i)

    file = parseText(file)


    ## TODO: parse brackets!
    ## TODO: problems with empty line parsed as variable
    print('\n\n\t((parsed text))')
    for i in file:
        print(i)
    
    