                                                -------- Fonction tux --------


Cette fonction reçoit en premier paramètre un tableau d'entiers numbers.
Elle devra déterminer si le tableau est partitionné et retourner l'index d'un des pivots.
Si le tableau n'est pas partitionné, elle devra retourner -1.


                                   -------- Explication de la solution intermédiaire --------


                                         def tux(numbers):

                                             if len(numbers) == 0:
                                                 return -1

                                             index_min = numbers.index(min(numbers))
                                             index_max = numbers.index(max(numbers))
                                             index_mid = index_max - 1
                                             
                                             if len(numbers) == 0:
                                                 return -1
                                             if index_max == len(numbers) - 1:
                                                 return index_max
                                             if index_min == 0:
                                                 return index_min
                                             for i in range(index_max, len(numbers)):
                                                 if numbers[index_mid] > numbers[i]:
                                                     return -1
                                             for i in range(index_mid):
                                                 if numbers[i] >= numbers[index_mid]:
                                                     return -1

                                             return index_mid


Les trois première conditions comportent uniquement des opérations de complexité temps constant (O1). Elles ont donc une complexité temps en O(1).
La première boucle parcourt la liste de index_max à la fin de la liste. Dans le pire des cas cela reviendrait à parcourir quasiment toute la liste, cette boucle dépend donc de la longueur n de la liste. Dans cette boucle for la condition comprend une opération de comparaison de complexité temps en O(1). La première boucle for a une complexité temps en O(n + 1) soit O(n).
La deuxième boucle for parcourt la liste du début de la liste à index_mid. Dans le pire des cas cela reviendrait également à parcourir quasiment toute la liste. Cette boucle dépend donc de la longueur n de la liste. Dans cette boucle for la condition comprend une opération de comparaison de complexité temps en O(1). La deuxième boucle for a une complexité temps en O(n + 1) soit O(n).
La fonction tux a donc une complexité temps en O(2n + 2) soit O(n).

En terme de complexité mémoire, étant donné qu'on ne fait qu'itérer dans la liste ou la compter, la fonction tux a une complexité mémoire en O(1).

Cette solution ne renvoie pas le résulta attendue dans le cas suivant :
numbers = [1, 4, 6, 0, 10, 10, 10, 10, 10, 10, 18, 8067, 30, 42, 17]



                                       -------- Explication de la solution finale --------



Nous avons donc modifié la fonction pour prendre en compte les cas auxquels nous n'avions pas pensé. Ce qui donne :



                                         def tux(numbers):

                                             if len(numbers) == 0:
                                                 return -1

                                             index_min = numbers.index(min(numbers))
                                             index_max = numbers.index(max(numbers))
                                             index_pivot = index_min + 1

                                             if index_max == len(numbers) - 1:
                                                return index_max
                                             if index_min == 0:
                                                return index_min
                                             if index_min > index_max:
                                                return -1
                                                
                                             for i in range(index_pivot):
                                                 if numbers[index_pivot] <= numbers[i] and index_pivot != index_max:
                                                    index_pivot += 1
                                                    i = 0
                                                 if numbers[index_pivot] <= numbers[i] and index_pivot == index_max - 1:
                                                    return -1
                                             for i in range(index_pivot, len(numbers)):
                                                 if numbers[index_pivot] > numbers[i]:
                                                    return -1

                                             return index_pivot



La première condition comprend la fonction len() qui a une complexité temps constant O(1) et une opération de comparaison de complexité temps constant O(1). Cette condition a donc une complexité temps O(1). Les fonctions min() et max() ont uen complexité temps linéraire O(n). La deuxième, troisième et quatrième condition if comprennent chacune une opération de comparaison en temps constant O(1), elle ont donc une complexité temps en O(1). La première boucle for dépend de la position k du pivot dans le liste qui, dans le pire des cas, est égale à index_max - 1. Elle a donc une complexité temps O(k). A l'intérieur de cette boucle on a une première condition qui comprend une opération de comparaison, une incrémentation et une opération d'assignation qui sont tous en temsp constant O(1) et une deuxième condition qui comprend une opération de comparaison en temsp constant O(1). La première boucle for a donc une complexité O(k).
La deuxième boucle for a une complexité temps O(n - k). A l'intérieur de cette boucle, la condition if comprend une opération de comparaison qui a une complexité temps constant O(1). Cette deuxième boucle a don une complexité temps en O(n-k).
Etant donnné que la complexité temps d'un algorithme correspond à la complexité temps de l'opératio qui a la complexité temps la plus grande, la fonction tux a une complexité temps en O(n).
En terme de complexité mémoire, comme on ne fait que parcourir la liste, la fonction tux a une complexité mémoire constante.

Au vue de la complexité temps en O(n) et de la complexité mémoire en O(1) de la fonction tux, nous considérons que cet algorithme est acceptable.