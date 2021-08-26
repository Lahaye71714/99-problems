                                  -------- Fonction roger_rabbit --------
                                                

Cette fonction doit générer les représentations en binaire de tous les nombres compris entre 1 et n inclus. Ces représentations doivent être retournées sous forme d'un tableau de chaînes de caractères, dans l'ordre croissant.


                            -------- Phase intermédiaire : une première solution --------

Pour cette première implémentation l'idée est de convertir chaque chiffre de 1 à n en leur représentation binaire par une série de calculs. 

                                      def roger_rabbit(n):
                                          new_list = []
    
                                          for i in range(1, n+1):
                                              res = ''
                                              while i != 0:
                                                    q = i // 2
                                                    r = i % 2
                                                    res = str(r) + res
                                                    i = q
                                              new_list.append(res)
       
                                          return new_list
                                          

Cet algorithme comporte deux boucles. La deuxième boucle est imbriquée dans la première boucle. La première boucle for dépend de n, elle a donc une complexité temps O(n). Dans la deuxième boucle les opérations correspondent à des divisions par 2. La complexité temps de ces opérations est log2(n). De plus cette boucle s'éxécute n fois. La boucle while à une complexité temps O(n*log2(n)) soit O(n*log(n)) étant donné que n est divisé par une valeur constante. La complexité temps d'un algorithme étant égale à la complexité temps de l'opération qui a la plus grande complexité temps, cet algorithme a une complexité temps O(n*log(n)).
En terme de complexité mémoire, la taille de la liste créée dépend de la variable n, donc cet algorithme a une complexité mémoire O(n).
Cette solution n'est pas optimale en terme de complexité temps.


                                 -------- Explication de la solution finale --------
                                                 

En cherchant à optimiser la complexité temps pour qu'elle soit de O(n), nous sommes arrivées à l'implémentation suivante:


                                      def roger_rabbit(n):
    
                                         new_list = []
    
                                         for i in range (0, n + 1):
                                             if i == 1:
                                                new_list.append('1')
                                             if i > 1 and i % 2 == 0:
                                                new_list.append(new_list[(i // 2) - 1] + '0')
                                             if i > 1 and i % 2 == 1:
                                                new_list.append(new_list[(i // 2) - 1] + '1')
 
                                         return new_list


Il est à noté que sous forme binaire chaque chiffre ou nombre pair se termine par 0 et que chaque chiffre ou nombre impair se termine par 1. De plus, pour une chiffre ou nombre pair, l'enchaînement de 1 et de 0 qui se trouvent avant le dernier 0 correspond à la représentaition binaire de sa moitié. C'est à dire que la forme représentation de 2 correspond à la représentation binaire de 1, à savoir "1", à laquelle on accole "0", ce qui donne "10". La représentation binaire de 4 correspond à la représentation binaire de 2, à savoir "10", à laquelle on accole "0", ce qui donne "100". Pour les chiffres et nombres impairs il suffit de reprendre la représentation binaire de la moitié du chiffre ou nombre pair qui les précède  et d'y accoler "1". Par exemple la représentation binaire de 5 correspond à la représentation binaire de 2 (qui est la moitié de 4), à savoir "10", à laquelle on accole "1", ce qui donne "101".
Dans cette implémentation il n'y a qu'une boucle for qui dépend de n, elle est donc de complexité temps O(n). Les opérations de concaténation ainsi de les opérations numériques sont de complexité temps constant O(1). Cet algorithme a donc une complexité temps O(n).
En terme de complexité mémoire, la taille de la liste dépend de n. Cet algorithme a donc une complexité mémoire O(n).
Au regard de la complexité temps et de la complexité mémoire qui sont tous deux O(n), nous considérons que cet algorithme est acceptable.