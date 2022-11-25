from src.file_reader import readFiles

from src.parser_symbol import parseText
from src.parser_FA import extractExpression


if __name__ == "__main__":
    file : list[str] = readFiles("./toread.js")

    # print("\t((raw text))")
    # for i in file:
    #     print(i)

    parsed_symbols, parsed_variables = parseText(file)
    # print(parsed_variables)


    # # ## TODO: parse brackets!
    # # ## TODO: problems with empty line parsed as variable
    # print('\n\n\t((parsed text))')
    # for i in parsed_symbols:
    #     print(i)

    
    print(extractExpression(file, parsed_variables))
    



    
    