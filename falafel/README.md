                                       -------- Fonction Falafel --------

La fonction doit déterminer si une des permutations possible de la chaîne de caractères passée en paramètre est un palindrome.


                                 -------- Phase intermédiaire de la solution --------

L'idée de cette première solution est de vérifier si il y a deux lettres qui apparaissent un nombre de fois impair.

                                         def falafel(s):
                                             odd_count = 0
                                             for letter in s:
                                                 if s.count(letter) % 2 != 0:
                                                    odd_count += 1
                                             if odd_count > 1:
                                                return False
                                             return True

La boucle for parcourt toute la chaîne de caractères une fois. Elle dépend de la longueur de la chaîne de caractères et a donc une complexité temps O(n). La condition if imbriquée dans la boucle for contient la méthode count() qui parcourt toute la chaîne de caractères. Elle a donc une complexité temps O(n). Or comme l'éxécution de la condition est subordonnée à la boucle for, la vérification de la condition if s'effectuera n fois. La chaîne de caractères sera donc parcourue n x n fois. Le modulo a une complexité temps en O(log2(m)), m étant la taille de l'entier, soit O(log(m)). Les opérations de comparaison et d'addition ont une complexité temps constante O(1). Le bloc de la boucle for a pour complexité temps O(log(m) + n^2 + 3) soit O(n^2).
La deuxième condition if est indépendante de la boucle for. Elle effectue une comparaison qui est de complexité constante O(1).
La complexité temps de cet algorithme est O(n^2).
En terme de conplexité mémoire on ne fait qu'itérer dans la chaîne de caractères. Cet algorithme a donc une complexité mémoire constante O(1).

                                 -------- Explication de la solution finale --------

L'objectif est de réduire la compexité temps de la première étape à O(n). Pour se faire nous allons transformer la chaîne de caractères en dictionnaire de telle sorte que les éléments de la chaîne de caractères soient les clés et leur occurrence la valeur associée.
Ce qui donnne l'implémentation suivante :

                                        def falafel(s):
                                        
	                                        new_list = list(s)
	                                        hist = {}
	                                        for letter in new_list:
		                                        hist[letter] = hist.get(letter, 0) + 1
        
                                            odd_count = 0
	                                        for key in hist:
		                                        if hist[key] % 2 != 0:
			                                       odd_count += 1
	
                                            return odd_count <= 1

La première boucle for parcourt la liste une seule fois en entier elle est donc de complexité temps O(n) et la vérification et l'ajout de la valeur dans le dictionnaire sont de temps constant O(1). La première boucle for a donc une complexité temps O(n).
La deuxième boucle for est indépendante de la première boucle for. Elle dépend de la longueur du dictionnaire qui elle même dépend de la taille de la liste. Dans la condition if imbriquée dans la boucle for on a l'opération modulo. En python les entiers n'ayant pas une taille fixe le modulo est ici une opération de complexité temps O(log2(m)) soit O(log(m)) avec m qui correspond à la taille de l'entier concerné. Etant donné que l'opération modulo est exécutée n fois, la condition if a une complexité temps O(n*log(m)). Cependant on peut considérer que la complexité temps de l'opération modulo est négligeable tant qu'on ne l'applique pas à de très grands nombres et qu'elle se rapproche de O(1). La complexité temps de la condition if se rapproche alors de O(n). La comparaison et l'addition sont de complexité temps constant O(1). Cet algorithme a donc une complexité temps O(2n) soit O(n).

En terme de complexité mémoire la création du dictionnaire dépend de la taille de la liste. Dans le pire des cas où tous les éléments de la liste n'ont qu'une seule occurrence, il est nécessaire d'allouer au dictionnaire une taille en mémoire capable d'accueillir n éléments, n étant le nombre d'éléments contenu dans le liste. Dans ce cas la taille du dictionnaire sera égale à la taille de la liste. On aura donc une complexité mémoire O(n). Les opérations numériques et la comparaison ont une complexité mémoire constante O(1). Cet algorithme a donc une complexité mémoire O(n).

Au vue de la complexité temps O(n) et la complexité mémoire O(n) de cet algorithme, nous considérons qu'il est acceptable.