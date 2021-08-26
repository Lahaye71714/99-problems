                                -------- Fonction set_et_match --------

Cette fonction doit déterminer si parmi les nombres entiers donnés en premier argument, il en existe deux qu'on peut additionner pour obtenir le nombre donné en second argument.


                                 -------- Phases intermédiaires de la solution --------


Phase 1:

La première implémentation de la fonction était la suivante:

                              def set_et_match(numbers, n):
                                  for i in numbers:
                                      for j in numbers:
                                          if i + j == n:
                                             return True
                                  return False


Pour arriver à cette solution nous nous sommes dit qu'il est nécessaire de parcourir le tableau plusieurs fois afin de comparer les différentes combinaisons d'addition possible entre deux chiffres dans le tableau avec l'entier passé en second paramètre.
Nous nous sommes rendues compte que la fonction ne renvoyait pas la valeur attendue dans certains cas parce que les variables i et j commencent sur le même index au début de chaque itération de la deuxième boucle for. Le résulat est que chaque chiffre du tableau se retrouve addidionné à lui-même au moins une fois. Nous avons donc procédé à une modification du code par l'utilisation de la fonction range() pour obtenir le décalage d'index entre les variables i et j au début de chaque itération de la deuxième boucle for.

Nous avons abouti à la deuxième implémentation de la fonction : 

                         def set_et_match(numbers, n):
                             for i in range(0, len(numbers)):
                                 for j in range(i+1, len(numbers)):
                                     if numbers[i] + numbers[j] == n:
                                        return True
                             return False

On a deux boucles qui dépendent de la longueur du tableau. Un première boucle qui parcoure le tableau entièrement et une seule fois. Cette première boucle a une complexité temps O(n). Et une deuxième boucle qui parcours n fois le tableau de longueur n. Cette deuxième boucle a une complexité temps O(n x n) soit O(n^2). L'addition et la comparaison ont une complexité temps constante. La complexité temps d'un algorithme est égale à la complexité en temps de l'opération qui présente la complexité temps la plus élevée. La complexité temps de cet algorithme est dont O(n^2).
En termes de complexité mémoire on peut dire qu'elle est constante puisqu'on ne fait que parcourir le tableau. Bien qu'il faille allouer de la mémoire pour effectuer l'addition et la comparaison, la place prise dans la mémoire par ces opérations est elle aussi constante.


Phase 2 :

Pour cette partie nous avons réfléchie autrement. Nous nous sommes dit qu'au lieu de chercher à additionner chaque chiffre de la liste avec les autres chiffres de la liste nous pouvions vérifier si le résultat de la soustraction du nombre n par chaque chiffre de la liste se trouvait dans la liste, ce qui donne :

                             def set_et_match(numbers, n):
                                 for i in range(0, len(numbers)):
                                     if (n - i) in numbers:
                                        return True
                                     else:
                                        i += 1
                                 return False


La boucle for dépend de la longueur de la liste, elle est donc de complexité O(n). La condition if contient une soustraction qui est de complexité constante O(1) et la recherche d'un élément dans une liste nécessite de parcourir la liste dans son entier. Cette opération dépend de la longueur de la liste, elle est donc de complexité O(n). La condition if est donc de complexité temps O(n). L'incrémentation est de temps constant O(1). La condition if étant imbriquée dans la boucle for la liste va être parcourue en entier autant de fois que la longueur de la liste soit n x n. Cet algorithme a donc une complexité temps O(n^2). Il n'est donc toujours pas optimal en terme de complexité temps. De plus, le problème de cette implémentation est que dans certains cas où i est la solution de la sousutraction n - i la fonction retournera True parce que i sera pris en compte lors de la vérification.  


                               -------- Explication de la solution finale --------


L'objectif est de  ramener l'opération de comparaison à un temps constant O(1) et de trouver un moyen pour contourner le fait que i est pris en compte lors de la comparaison. Ce qui donne l'implémentation suivante :

                               def set_et_match(numbers, n):
                                   number_dict = dict.fromkeys(numbers)
                                   solutions = [num for num in numbers
                                                if n - num in number_dict]
                                   return len(solutions) > 1

La transformation de la liste en dictionnaire dépend de la longueur de la liste, cette opération est de complexité O(n).
La boucle for parcours la liste en entier, elle dépend également de la longueur de la liste. Elle est donc de complexité temps O(n).
La condition if imbriquée dans la boucle for contient une soustration qui est de complexité temps constante O(1) ainsi que la recherche d'un élément dans un dictionnaire qui est aussi de complexité temps constant O(1), car dans un dictionnaire on accède directement à l'élément. Et l'ajout d'un élément à la fin d'une liste est également en tant constant O(1). Ce qui donne une complexité temps totale O(n).
La fonction len et la comparaison sont de complexité temps constant O(1).
Les opération de transformation de la liste en set et la boucle for étant indépendantes l'une de l'autre, on a un algorithme de complexité O(2n), soit O(n).
D'un point de vue de la complexité mémoire, dans le pire des cas on double la place prise dans la mémoire lors de la création du set.
Cette solution est plus optimale en terme de complexité temps que les implémentations précédentes. Nous pensons qu'un algorithme de complexité temps linéaire est une solution acceptable.
