                                    -------- Fonction yin_yang --------
                                    

Cette fonction reçoit en premier paramètre une chaîne de caractères contenant n'importe quelle combinaison de parenthèses, de crochets ou de guillemets (simples ou doubles). Elle devra s'assurer que chaque caractère "ouvrant" de la chaîne possède bien un caractère "fermant" correspondant situé après lui dans la chaîne et que les paires de caractères correspondants sont correctement imbriquées.
Si c'est bien le cas, elle retourne true. Sinon, elle retourne false.


                               -------- Explication de la solution --------
                               

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


Dans les fonctions la_bonne_paire_ouvrant_fermant et la_bonne_paire_guillemet il y a uniquement des opérations de complexité temps en O(1).Ces deux fonctions ont donc de complexité temps en O(1). En terme de complexité mémoire, on crée une pile qui dépend de la longueur de la chaîne de caractères mais dont la longueur sera dans le pire des cas égale à la moitié de la longueur de la chapine de caractère. Ces deux fonctions ont une complexité mémoire en O(1/2n) soit O(n).

Dans le fonction paire_bien_imbriquee on a une boucle for qui parcourt toute la chaîne de caractères. Elle dépend de la longueur de la chaîne de caractères. Elle est donc de complexité temps O(n). Dans cette boucle for on fait appel deux fois à la fonction la_bonne_paire_ouvrant_fermant et et deux fois à la fonction la_bonne_paire_guillemet. Ces deux fonction on une compexité temps en O(1). La boucle for a donc une complexité temps en O(n + 4) soit O(n). La fonction paire_bien_imbriquee a donc une complexité temps en O(n). En terme de complexité mémoire, la fonction paire_bien_imbriquee hérite de la complexité mémoire des fonctions la_bonne_paire_ouvrant_fermant et la_bonne_paire_guillemet. Elle a donc une complexité mémoire en O(n).

Dans la fonction yin_yang, la première condition comprend la fonction len() qui est de complexité temps constant O(1), une opération modulo qui est de complexité temps O(log(m)), m étant la taille de l'entier, et d'un test de comparaison de complexité temps constant O(1). Cette première condition est donc de complexité temps O(1 + log(m)) soit O(log(m)).
La deuxième condition comprend deux fois la fonction count() qui a une complexité temps linéaire O(n), deux opérations de modulo de complexité temps en O(log(m)), m étant la taille de l'entier, et deux tests de comparaison de complexité temps constant O(1). Cette deuxième condition a donc une complexité temps en O(2n + 2log(m) + 2) soit O(n).
La troisième condition comprend quatre fois la fonction count() de complexité temps linéaire O(n) et de deux tests de comparaison de complexité temps constant O(1). Cette condition a donc une complexité temps en O(4n + 2) soit O(n).
Dans le else on a un appel de la fonction paire_bien_imbriquee. On sait que la fonction paire_bien_imbriquee est de complexité temps O(n). Les opérations de comparaison ont une complexité temps constant O(1). Else a une complexité temps en O(n).
Au vue de la complexité temps de toutes les conditions, la fonction yin_yang a une complexité temps en O(n). En terme de compexité mémoire elle hérite de la complexité mémoire de la fonction paire_bien_imbriquee. Elle a donc une complexité mémoire en O(n).

Au vue de la complexité temps en O(n) et de la complexité mémoire en O(n) de la fonction yin_yang, nous considérons que cette solution est acceptable.