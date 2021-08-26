def la_bonne_paire_ouvrant_fermant(chaîne, pile, i, ouvrant, fermant):
    
    if chaîne[i] == ouvrant:
        pile.append(chaîne[i])
    elif chaîne[i] == fermant:
        if len(pile) == 0 or pile[-1] != ouvrant:
            return False
        elif pile[-1] == ouvrant:
            pile.pop()

                
def la_bonne_paire_guillemet(chaîne, pile, i, guillemet):
    
    if chaîne[i] == guillemet and len(pile) == 0:
        pile.append(chaîne[i])
    elif chaîne[i] == guillemet and len(pile) > 0 and pile[-1] != guillemet:
        pile.append(chaîne[i])
    elif chaîne[i] == guillemet and len(pile) > 0 and pile[-1] == guillemet:
        pile.pop()
    
    
def paire_bien_imbriquee(string, pile):
    
    for i in range (len(string)):
        retour = la_bonne_paire_ouvrant_fermant(string, pile, i, '(', ')')
        if retour == False:
            return False
        retour = la_bonne_paire_ouvrant_fermant(string, pile, i, '[', ']')
        if retour == False:
            return False
        la_bonne_paire_guillemet(string, pile, i, "'")
        la_bonne_paire_guillemet(string, pile, i, '"')

    return True


def yin_yang(s):

    if len(s) % 2 == 1:
        return False
    elif s.count('"') % 2 == 1 or s.count("'") % 2 == 1:
        return False
    elif s.count("(") != s.count(")") or s.count("[") != s.count("]"):
        return False
    else:
        pile = []
        retour = paire_bien_imbriquee(s, pile)
        if retour == False:
            return False

    return True
