                                -------- Fonction stormtroopers --------

La fonction stormtroopers doit renvoyer une nouvelle liste en ne conservant que les nombres qui figurent une seule fois dans la liste originale.

                          -------- Phases intermédiaires de la solution --------

                                    def stormtroopers(numbers):
                                        uniqueNumbers = [x for x in numbers if numbers.count(x) == 1]
                                        return uniqueNumbers

L'implentation ci-dessus est la forme condensée de :

                                    def stormtroopers(numbers):
                                        uniqueNumbers = []
                                        for x in numbers:
                                            if numbers.count(x) == 1:
                                               uniqueNumbers.append(x)
                                        return uniqueNumbers

La première boucle for parcours la liste en entier une fois. Elle dépend donc de la longueur de la liste. Sa complexité temps est de O(n).
La condition if contient la méthode count() qui dépend de la longueur de la liste et donc de complexité temps O(n). La condition if étant imbriquée dans la boucle for la liste va être parcourue en entier autant de fois que la longueur de la liste soit n x n. La comparaison et l'ajout d'un élément dans la  liste sont tous deux de complexité temps constant O(1). Cet algorithme a donc une complexité temps O(n^2). Il n'est pas optimal en terme de complexité temps. En terme de complexité mémoire on crée une nouvelle liste à partir de la première liste. Dans le pire des cas la deuxième liste sera de même longueur que la première liste. On double donc l'occupation en mémoire, on a donc une complexité mémoire O(2n) soit O(n).

Dans une tentative d'optimiser l'algorithme nous sommes passée par l'implémentation suivante :

                                    def stormtroopers(numbers):
	                                    if len(set(numbers)) == len(numbers):
		                                   return numbers
	                                    if len(set(numbers)) < len(numbers):
		                                   uniqueNumbers = [x for x in numbers if numbers.count(x) == 1]
		                                   return uniqueNumbers

La première condition comprends une suite d'instructions qui sont indépendantes les unes des autres et qui sont de complexité temps linéraire O(n). Dans le meilleur des cas l'algorithme aura une complexité temps O(n) et dans le pire des cas une complexité temps O(n^2). En terme de complexité mémoire comme on crée une nouvelle liste dans le deuxième cas on est également sur une complexité mémoire O(2n) soit O(n).

                                    -------- Solution finale --------

L'idée de cette solution est de créer un dictionnaire à partir de la liste initiale avec en clé les éléments du tableaux et associé à chaque clé le nombre d'occurrence de l'élément présent dans la liste.

                                    def stormtroopers(numbers):
	                                    hist = {}
	                                    for x in numbers:
		                                    hist[x] = hist.get(x, 0) + 1
                                        new_list = [x for x in hist if hist[x] == 1]
	                                    return new_list

La boucle for parcours la liste une seule fois en entier elle est donc de complexité temps O(n) et la vérification et l'incrémentation de la valeur dans le dictionnaire sont de temps constant O(1). La boucle for a donc une complexité temps O(n).
La transformation du dictionnaire en une nouvelle liste qui contient uniquement les valeurs qui ont une seule occurrence dépend de la longueur du dictionnaire. Cette opération a donc une complexité temps O(n). La comparaison présente dans le procéssus a une complexité temps constante O(1). La boucle for et la transformation du dictionnaire en liste étant des opérations indépendantes l'une de l'autre, l'algorithme a une complexité temps O(n + n) ou O(2n) soit O(n).
En terme de complexité mémoire, nous créons un dictionnaire à partir de la première liste et une liste à partir du dictionnaire. La création du dictionnaire demande dans le pire des cas deux fois plus de place en mémoire que la première liste. Cette opération a donc une complexité mémoire O(2n) soit O(n). La création de la liste à partir du dictionnaire dépend de la longueur du dictionnaire et demande dans le pire des cas autant de place en mémoire que la longueur du dictionnaire. Cette opération a donc une complexité mémoire O(n). La complexité mémoire de cet algorithme est de O(3n) soit O(n).
Nous pensons que cet algorithme est acceptable car il a une complexité temps linéraire O(n) et une complexité mémoire O(n).




