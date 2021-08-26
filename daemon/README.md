                                -------- Fonction daemon --------

Cette fonction permet de déterminer si un tableau est partitionné par rapport à un pivot donné.

Sachant qu'un tableau est patitionné si et seulement si tous les éléments qui précèdent le pivot sont strictement inférieurs au pivot et tous les éléments qui suivent le pivot sont supérieurs ou égals au pivot, il est nécessaire de parcourir tout le tableau afin de comparer chaque élément au pivot donné. Donc le temps d'éxécution de l'algorithme dépend du nombre d'éléments contenus dans le tableau.
Si on appelle 'n' le nombre d'éléments contenu dans le tableau, on va devoir itérer n fois dans le tableau. De plus on ne passe qu'une seule fois sur chaque élément du tableau pour effectuer la comparaison. La complexité en temps de cet algorithme est donc O(n) dans le pire des cas. L'algorithme que nous proposons est donc acceptable.
En ce qui concerne la complexité mémoire celle-ci est constante puisqu'on ne fait qu'itérer dans le tableau. Cette complexité peut-être notée O(1).

Nous sommes arrivées à cette solution directement, en prenant en compte la définition donnée dans l'exercice de ce qu'est un tableau partitionné, et le fait que l'index du pivot soit pris en paramètre par la fonction. Le fait que le pivot soit donné d'emblé réduit les opérations à une suite de comparaisons entre chaque élément du tableau et le pivot. C'est la solution qui nous paraît la plus simple et la plus adaptée au sujet.

                            def daemon(numbers, k):
                                x = 0
 
                                while x < k:
                                   if numbers[x] >= numbers[k]:
                                      return(False)
                                   else:
                                      x += 1

                                if x == k:
                                   x += 1

                                while x < len(numbers):
                                   if numbers[x] < numbers[k]:
                                      return(False)
                                   else:
                                      x += 1
            
                                return(True)


Pour l'implémentation nous avons choisi d'utiliser des boucles while car elles sont plus faciles à utiliser et à comprendre de prime abord pour nous que les boucles for. Il est cependant possible d'écrire la fonction en utilisant des boucles for.


                           def daemon(numbers, k):
                           
                                for x in range(0, k):
                                    if numbers[x] >= numbers[k]:
                                        return False
                                        
                                for x in range(k+1, len(numbers)):
                                    if numbers[x] < numbers[k]:
                                        return False
                                        
                                return True