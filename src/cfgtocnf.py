from utility import isTerminal, isVariable

# File: cfgtocnf.py 
# Mengkonversi CFG ke CNF

def ConvertCFGtoCNF(cfg):
    head = list(cfg.keys())
    body = list(cfg.values())
    startSymbol = head[0]
    startSymbolInRule = False
    isUnitInRule = True
    productionAdditionA = {}
    productionRemovalA = {}
    productionAdditionB = {}
    productionRemovalB = {}
    symbolAmount = 0
    p = 0
    q = 0

    for rules in body:
        for rule in rules:
            if startSymbol in rule:
                startSymbolInRule = True
                break
        if startSymbolInRule:
            break
    
    if startSymbolInRule:
        new_production = {"S_accent" : [[startSymbol]]}
        new_production.update(cfg)
        cfg = new_production
    
    while isUnitInRule:
        unitProductions = {}
        for key, value in cfg.items():
            for rule in value:
                if (isVariable(rule[0]) and len(rule) == 1):
                    if (key not in unitProductions.keys()):
                        unitProductions[key] = [[rule[0]]]
                    else:
                        unitProductions[key] += [[rule[0]]]
                else:
                    isUnitInRule = False
        for keyUnit, valueUnit in unitProductions.items():
            for ruleUnit in valueUnit:
                for key, value in cfg.items():
                    if (key == ruleUnit[0] and len(ruleUnit) == 1):
                        new_production_unit = {keyUnit : value}
                        if (keyUnit not in cfg.keys()):
                            cfg[keyUnit] = value
                        else:
                            for rule in value:
                                if rule not in cfg[keyUnit]:
                                    cfg[keyUnit] += [rule]
        for keyUnit, valueUnit in unitProductions.items():
            for ruleUnit in valueUnit:
                if len(ruleUnit) == 1:
                    cfg[keyUnit].remove(ruleUnit)
        
        
        for key, value in cfg.items():
            for rule in value:
                keySymbol = key
                ruleStorage = [x for x in rule]
                if len(ruleStorage) > 2:
                    while len(ruleStorage) > 2:
                        newSymbol = "X%d" % (symbolAmount)
                        if keySymbol in productionAdditionA.keys():
                            productionAdditionA[keySymbol] += [[ruleStorage[0], newSymbol]]
                        else:
                            productionAdditionA[keySymbol] = [[ruleStorage[0], newSymbol]]
                        keySymbol = newSymbol
                        ruleStorage.remove(ruleStorage[0])
                        symbolAmount += 1
                    else: 
                        if keySymbol in productionAdditionA.keys():
                            productionAdditionA[keySymbol] += [ruleStorage]
                        else:
                            productionAdditionA[keySymbol] = [ruleStorage]
                        
                        if key in productionRemovalA.keys():
                            productionRemovalA[key] += [rule]
                        else:
                            productionRemovalA[key] = [rule]
        
        for a, b in productionAdditionA.items():
            if a in cfg.keys():
                cfg[a].extend(b)
            else:
                cfg[a] = b
        for c, d in productionRemovalA.items():
            for e in d:
                cfg[c].remove(e)
        
        for key, value in cfg.items():
            for rule in value:
                if len(rule) == 2:
                    if isTerminal(rule[0]) and isTerminal(rule[1]):
                        new_Y = "Y%d" % (p)
                        new_Z = "Z%d" % (q)
                        if key in productionAdditionB.keys():
                            productionAdditionB[key] += [[new_Y, new_Z]]
                        else:
                            productionAdditionB[key] = [[new_Y, new_Z]]
                        productionAdditionB[new_Y] = [[rule[0]]]
                        productionAdditionB[new_Z] = [[rule[1]]]
                        if key in productionRemovalB.keys():
                            productionRemovalB[key] += [rule]
                        else:
                            productionRemovalB[key] = [rule]
                        p += 1
                        q += 1

                    elif isTerminal(rule[1]):
                        new_Z = "Z%d" % (q)
                        if key in productionAdditionB.keys():
                            productionAdditionB[key] += [[rule[0], new_Z]]
                        else:
                            productionAdditionB[key] = [[rule[0], new_Z]]
                        productionAdditionB[new_Z] = [[rule[1]]]
                        if key in productionRemovalB.keys():
                            productionRemovalB[key] += [rule]
                        else:
                            productionRemovalB[key] = [rule]
                        q += 1
                    
                    elif isTerminal(rule[0]):
                        new_Y = "Y%d" % (p)
                        if key in productionAdditionB.keys():
                            productionAdditionB[key] += [[new_Y, rule[1]]]
                        else:
                            productionAdditionB[key] = [[new_Y, rule[1]]]
                        productionAdditionB[new_Y] = [[rule[0]]]
                        if key in productionRemovalB.keys():
                            productionRemovalB[key] += [rule]
                        else:
                            productionRemovalB[key] = [rule]
                        p += 1
                    
                    else:
                        pass
                        
                else:
                    pass
        for a, b in productionAdditionB.items():
            if a in cfg.keys():
                cfg[a].extend(b)
            else:
                cfg[a] = b
        for c, d in productionRemovalB.items():
            for e in d:
                cfg[c].remove(e)
        
        return cfg

