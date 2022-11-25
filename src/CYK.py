def cyk(cnf: dict[str,list[list]], read_input: str) -> bool:
    # KAMUS LOKAL
    list_of_words: list[str]
    n: int
    Table: list[list]
    r: int
    c: int
    i: int
    rule_length: int
    valid: bool

    # ALGORITMA
    list_of_words = read_input.split(" ")
    n = len(list_of_words)
    Table = [[set([]) for c in range(n)] for r in range (n)]

    for c in range (n):
        for head, body in cnf.items():
            for rule in body:
                rule_length = len(rule)
                if ((rule_length == 1) and (rule[0] == list_of_words[c])):
                    Table[c][c].add(head)

        for r in range (c, -1, -1):
            for i in range (r, c):
                for head, body in cnf.items():
                    for rule in body:
                        rule_length = len(rule)
                        if ((rule_length == 2) and (rule[0] in Table[r][i]) and (rule[1] in Table[i+1][c])):
                            Table[r][c].add(head)
    
    if (len(Table[0][n-1]) == 0):
        valid = False
    else:
        valid = True

    return valid