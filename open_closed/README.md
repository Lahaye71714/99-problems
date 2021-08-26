                                    -------- Fonction open_closed --------


Cette fonction reçoit en premier paramètre une chaîne de caractères contenant n'importe quelle combinaison de parenthèses, de crochets ou de guillemets (simples ou doubles).
Elle doit s'assurer que chaque caractère "ouvrant" de la chaîne possède bien un caractère "fermant" correspondant situé après lui dans la chaîne (et inversement : tout caractère "fermant" doit posséder un caractère "ouvrant" correspondant situé avant lui).
Si c'est bien le cas, elle devra retourner true. Sinon, elle devra retourner false.


                                  -------- Explication de la solution --------


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


Dans le fonction la_bonne_paire on a une boucle for qui parcourt toute la chaîne de caractères. Elle dépend de la longueur de la chaîne de caractères. Elle est donc de complexité temps O(n). Dans cette boucle for se trouvent quatre conditions qui comportent des comparaisons de complexité temps constant O(1). Une des conditions contient la fonction len() qui est de complexité temps O(1). Les méthodes append() et pop() sont de complexité temps constant O(1). La fonction la_bonne_paire est de complexité temps O(n + 7) soit O(n). En terme de complexité mémoire, comme on crée une pile qui, dans le pire des cas, est de la même longueur que la chaîne de caractères, la fonction a une complexité linéraire O(n).

Dans la fonction open_closed la première condition comprend la fonction len() qui est de complexité temps constant O(1), une opération modulo qui est de complexité temps O(log(m)), m étant la taille de l'entier, et d'un test de comparaison de complexité temps constant O(1). Cette première condition est donc de complexité temps O(log(m)).
La deuxième condition comprend deux fois la fonction count() qui a une complexité temps linéaire O(n), deux opérations de modulo de complexité temps en O(log(m)) et deux tests de comparaison de complexité temps constant O(1). Cette deuxième condition a donc une complexité temps O(2n + 2log(m) + 2) soit O(n).
La troisième condition comprend quatre fois la fonction count() de complexité temps linéaire O(n) et de deux tests de comparaison de complexité temps constant O(1). Cette condition a donc une complexité temps O(4n + 2) soit O(n).
Dans le else on a deux appels de la fonction la_bonne_paire l'une à la suite de l'autre. On sait que la fonction la_bonne_paire est de complexité temps O(n). Les opérations de comparaison ont une complexité temps constant O(1). Else a une complexité temps O(2n + 4) soit O(n).
Au vue de la complexité temps de toutes les conditions, la fonction open_closed a une complexité temps O(n). En terme de compexité mémoire elle hérite de la complexité mémoire de la fonction la_bonne_paire. Elle a donc une complexité mémoire en O(n).

Au vue de la complexité temps O(n) et de la complexité mémoire O(n) de la fonction open_closed, nous considérons que cette solution est acceptable.