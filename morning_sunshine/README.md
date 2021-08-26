                                        -------- Fonction morning_sunshine --------


Cette fonction reçoit en premier paramètre un tableau d'entiers numbers.
Elle doit retourner un tableau qui contient uniquement les éléments du tableau reçu qui sont strictement supérieurs à tous ceux situés après eux.



                                       -------- Explication de la solution --------


                                       def morning_sunshine(numbers):
                                           new_list = []
                                           j = 0

                                           if len(numbers) < 2:
                                               return numbers
                                           elif len(numbers > 1):
                                               new_list.append(numbers[len(numbers) - 1])
                                               for i in numbers[::-1]:
                                                   if i > new_list[j]:
                                                      new_list.append(i)
                                                      j += 1
                                               new_list.reverse()

                                           return new_list


La première condition comprend une opération de comparaison de complexité temps O(1).
Les opérations d'ajout et la fonction len() ont une complexité temps en O(1).
La première boucle for parcourt la liste en entier une seule fois, elle dépend donc du nombre d'éléments n dans la liste. Elle a une complexité temps de base en O(n). Dans la boucle for il y a une opération de comparaison et une opération d'ajout qui sont tous deux de complxité temps contant O(1). La boucle for a donc une complexité temps en O(n).
La méthode reverse() dépend du nombre d'éléments  m de new_list, elle a donc une complexité en O(m).
Dans le pire des cas m = n. La fonction morning_sunshine a donc une complexité en O(n + m) soit O(n).
Du point de vue de la complexité mémoire, étant donné qu'on crée une nouvelle liste qui dans le pire des cas contiendra la même nombre d'éléments que la liste initiale, la fonction morning_sunshine à une complexité mémoire en O(n).
Au vu e de la complexité temps en O(n) et de la complexité mémoire en O(n), nous considérons que cette solution est acceptable.
