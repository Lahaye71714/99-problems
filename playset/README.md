                                    -------- Fonction playset --------

Ecrire une fonction qui reçoit en paramètre une chaîne de caractères.
Si la chaîne contient des doublons, la fonction renvoie "true", si elle n'en contient pas elle renvoie "false".


                                -------- Explication de la solution 1 --------

Nous sommes partie du postulat que pour trouver s'il y a des doublons dans la chaîne, il faut vérifier chaque élément contenue dans la chaîne et cela prend O(n) temps dans le meilleurs des cas. De plus si le premier élément de la chaîne n'a pas de doublon, il faudra parcourir de nouveau la chaîne de caratère "n" fois en partant de l'index "i+1" jusqu'à trouver un élément qui a des doublons. Cette fonction est donc de complexité temps O(n x n) soit O(n^2).
La complexité mémoire est constante O(1) étant donné qu'on ne fait que parcourir la chaîne de caractère.

                                         def playset(s):
                                             for i in range(0, len(s)):
                                                 count = 1
                                                 for j in range(i+1, len(s)):
                                                     if(s[i] == s[j] and s[i] != ''):
                                                              count = count + 1
                                                              if count > 1:
                                                                 return True
                                                              else:
                                                                i += 1
                                             return False
                                             

                                -------- Explication de la solution 2 --------

Pour arriver à la solution numéro deux nous nous sommes dit qu'il n'était pas nécessaire de parcourir toute la chaîne de caractères n fois. Une autre approche est de transformer la chaîne de caractères passée en paramètre en une chaîne de caractères qui ne contient pas de doublons et de comparer la longueur des deux chaînes de caractères. Ce qui donne:

                                       def playset(s):
                                           if len(s) == len(set(s)):
                                              return(False)
                                           else :
                                              return(True)

Pour transformer la première chaîne de caractères en une chaîne de caractères sans doublons nous opton pour le construteur set() pour créer un set car un set n'admet pas de valeurs redondantes.
Pour créer un set il est nécessaire de parcourir la chaîne de caractères d'origine en entier. Comme le temps de l'itération dépend de la longueur de la chaîne de caractère elle a une complexité temps O(n). Par contre il n'est pas nécessaire de parcourir la liste du set pour savoir si un élément y est présent ou pas, cette opération a donc une complexité temps O(1). La trasformation d'une chaîne de caractères en set a donc une complexité temps O(n + 1) soit O(n). Obtenir la longueur d'une chaîne de caractères nécessite de parcourir toute la chaîne da caractères, cette opération a une complexité temps O(n). La comparaison entre deux chiffres a une complexité temps constante O(1). Etant donné que ces opération s'exécutent les unes à la suite des autres, on obtient une complexité temps O(n + n + 1) soit O(n) dans le pire des cas.
En termes de complexité mémoire, étant donné qu'on crée une nouvelle chaîne de caractères composée de n éléments à partir d'une chaîne de caractères composée de n éléments, on a une complaxité mémoire O(n + n) soit O(n). De plus on compare entre eux deux chiffres ce qui représente une complexité mémoire constante O(2). La complexité méoire de cet algorithme est O(n + 2) soit O(n).

Nous considérons que cette solution est acceptable parce que l'algorihtme est plus performant en termes de complexité temps que celui de la première solution et que l'implémentation est plus élégante et plus compacte que celle de la première solution. Il est a noté qu'en termes de complexité mémoire la deuxième solution est plus gourmande que la première solution. La première solution est a privilégier lorsqu'on veut économiser de la mémoire.