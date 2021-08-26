                                -------- Fonction do_a_barrel_roll --------

La fonciton reçoit en premier paramètre un tableau d'entier et en second paramètre un entier k.
La fonciton doit effecuter K rotations vers la gauche de chaque élément du tableau.



                               -------- Explication des étapes intermédiaires --------

L'implémentation de la fonction do_a_barrel_roll :

                                     def do_a_barrel_roll(numbers, k):

                                         list1 = [numbers[x] for x in range(0, k)]
                                         list2 = [numbers[x] for x in range(k, len(numbers))]
                                         list2.extend(list1)

                                         return list2
                                         
Cette implémentation pose problème car la fonction essaie d'accéder à un index qui est en dehors de la liste.


Après correction de l'implémentation on obtient :


                                    def do_a_barrel_roll(numbers, k):

	                                    list1 = [x for x in range(0, k)]
	                                    list2 = [x for x in range(k, len(numbers))]
	                                    list2.extend(list1)

	                                    return list2

Pour créer les deux nouvelles listes à partir de la première liste, nous utilisons deux boucles for qui sont indépendantes l'une de l'autre et qui sont exécutées l'une à la suite de l'autre. La boucle for de la list1 a une complexité temps O(k) dans le meilleur des cas ou O(n) dans le pire des cas. La boucle for de la liste2 a une complexité temps O(n - k) dans le meilleur des cas ou O(n) dans le pire des cas. La méthode extend() a une compexité temps liénaire O(n) et l'ajout d'un élément de la list1 à la list2 ne nécessite qu'un nombre constant d'opérations. Cet algorithme a donc une complexité temps linéraire O(n).
Du point de vue de la complexité mémoire on crée deux nouvelles listes qui a elles deux prennent autant de place en mémoire que la liste de départ O(k + n - k) soit O(n). Lorsqu'on ajoute les éléments de list1 à list2 on ne crée pas une nouvelle liste mais on modifie list2 dont la longueur finale est len(list2)+len(list1), O(n+n) soit O(n). Cet algorithme a donc une complexité mémoire O(n + n) soit O(n).

Cette solution ne fonctionne pas si k est supérieur à len(numbers) et si la liste est vide elle renvoie une liste contenant les chiffres de 0 à k non compris à cause de la création de list1. Par exemple si k == 4 la fonction renverra [0, 1, 2, 3]. Il nous faut donc un algorithme qui prenne en compte ces cas.


                               -------- Explication de la solution proposée --------


                                     def do_a_barrel_roll(numbers, k):

                                         if k == 0 or numbers == []:
                                            return numbers

                                         if k > len(numbers):
                                             while k > len(numbers):
                                                 k = k - len(numbers)

                                         if k == len(numbers):
                                             return numbers

                                         if k < len(numbers):
                                             list1 = [x for x in range(0, k)]
                                             list2 = [x for x in range(k, len(numbers))]
                                             list2.extend(list1)

                                             return list2


La solution proposée permet de prendre en compte quatre situations rencontrées en fonction de K. l'enchaînement des condition a été pensée pour gagner du temps d'exécution. La première condition est de complexité constante O(1) la vérification et le renvoie de la liste sont des opérations en temps constant O(1). La deuxième condition comprend une boucle while imbriquée. La valeur de k décroit de façon linéraire de la longueur de la liste numbers. Si on dessine un graphique on obtient une droite. Cette condition a donc une complexité temps linéraire O(n). La troisième condition a une complexité temps constante O(1) car la comparaison et renvoyer la liste sont des opérations en temps constant O(1). La complexité temps et la complexité mémoire de la troisième condition sont exactement les mêmes que celles de la solution intermédiaire. Cet algorithme concerve une complexité temps linéraire O(n) et une complexité mémoire O(n). C'est pour cela que nous pensons que cette solution est acceptable.