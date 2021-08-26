def la_bonne_paire(string, ouvrant, fermant):
    pile = []

    for i in range (len(string)):
        if string[i] == ouvrant:
            pile.append(string[i])
        elif string[i] == fermant:
            if len(pile) == 0:
                return False
            if pile[-1] == ouvrant:
                pile.pop()

    return True


def open_closed(s):

    if len(s) % 2 == 1:
        return False
    elif s.count('"') % 2 == 1 or s.count("'") % 2 == 1:
        return False
    elif s.count("(") != s.count(")") or s.count("[") != s.count("]"):
        return False
    else:
        retour = la_bonne_paire(s, "(", ")")
        if retour == False:
            return False
        retour = la_bonne_paire(s, "[", "]")
        if retour == False:
            return False

    return True       
                
            

