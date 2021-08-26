                                -------- Fonction yulaw --------

Cette fonction reçoit en paramètre une chaîne de caractères et doit retourner une chaîne de caractères dans laquelle les caractères identiques ont été fusionnés.


                                   -------- Partie 1 --------

Nous sommes parties du postulat que pour retourner une nouvelle chaîne de caractères sans doublons il fallait remplir une nouvelle chaîne de caractères grâce à une boucle. A chaque itération la fonction compare l'élément à l'index i avec les éléments contenus dans la nouvelle chaîne de caractère et ajoute l'élément dans la nouvelle chaîne de caratères s'il n'y figure pas. Ce qui donne :

                                def yulaw(s):
                                   unique = ("")
                                   for i in s:
                                       if i not in unique:
                                          unique += i
                                   return unique

Comme on doit vérifier chaque élément contenu dans la chaîne de caractère il faut parcourir au moins une fois la chaîne de caractères en entier. Dans cette fonction on a une boucle qui dépend de la longueur de la chaîne et comme on ne parcours la chaîne qu'une seule fois dans tous les cas, la complexité de cette itération est de 0(n) dans le pire des cas. Or à chaque itération la fonction parcours également la nouvelle chaîne de caractères composée de n éléments et elle la parcours n fois (ici n étant le nombre d'éléments contenus dans la première chaîne de caractères). La complexité de cette opération en temps est O(n^2) dans le pire des cas. La comparaison et l'ajout d'un élément ont chacun une complexité temps fixe O(1). La complexité en temps de cet algorithme est O(1 + 1 + n + n^2). Dans le calcul de la complexité en temps on ignore les constantes. De plus la complexité en temps d'un algorithme est égale à la complexité en temps de l'opération qui présente la complexité en temps la plus élevée. La complexité en temps de cet algorithme est donc O(n^2).

En termes de complexité mémoire cette fonction prend en paramètre une chaîne de caractères contenant n caractères et crée une nouvelle chaîne de caractères contenant elle aussi n caractères. Quand un élément est ajouté à la nouvelle chaîne de caractères cette dernière prend plus de place en mémoire. On peut dire que cette fonction a une complexité mémoire O(2n), soit O(n), en raison de la création de la nouvelle chaîne de caractères contenant n caractères.


                                -------- Partie 2 --------

Après réflexion, nous avons opté pour une autre méthode qui consiste à tranformer la chaîne de caractères en dictionnaire en utilisant chaque élément de la chaîne de caractères comme clé. Les dictionnaires ne peuvent contenir des clés en doublons, donc transformer la chaîne de caractère en dictionnaire va automatiquement faire disparaître les doublons. Etant donné qu'on ne peut transformer directement un dictionnaire en chaîne de caractère avec la fonction str(), nous avons choisi de concaténer les clés du dictionnaire à l'aide d'une boucle pour obtenir la nouvelle chaîne de caractère sans les doublons. Ce qui donne :

                            def yulaw(s):
                                 mydict = dict.fromkeys(s)
                                 concat = ""
                                 for x in mydict:
                                     concat +=  x
                                 return(concat)

Il existe cependant la méthode join() qui permet de joindre les éléments d'un dictionnaire en une chaîne de caractères. On obtiens une fonction qui selon nous semble la plus compacte possible. Ce qui donne:

                            def yulaw(s):
                                mydict = dict.fromkeys(s)
                                s = "".join(mydict)
                                return(s)

Les clés d'un dictionnaire sont générées par une fonciton de hachage. Si lors du parcours de la chaîne de caractère il y a des doublons la valeur en double remplacera la clé existante dans le dictionnaire. On parcoure une seule fois la chaîne de caractères pour créer le dictionnaire. Cela présente une complexité temps O(n). La création du dictionnaire ne nécessite pas de parcourir les éléments du dictionnaire parce que le dicitonnaire est une hashmap. Dans un hashmap vérifier la présence d'une clé est une opération de complexité temps O(1) parce qu'on accède directement à la clé. La transformation de la chaîne de caractère en dictionnaire a une complexité temps O(n).
Joindre les éléments du dictionnaire en une chaîne de caractères est un opération de complexité temps constant O(1). Pour joindre tous les éléments du dictionnaire il est nécessaire de parcourir tout le dictionnaire en entier et il n'est nécessaire de la parcourir qu'une seule fois. La transformation d'un dictionnaire en chaîne de caractères a une complexité temps O(n).
Si on considère les deux actions effectuées l'une à la suitre de l'autre, on obtiens pour cet algorithme une complexité temps 0(2n) soit O(n).

En termes de complexité mémoire on peut dire qu'elle est constante O(1)  bien que dans le cas où il y a des doublons le nombre d'éléments diminue.
Cet algorithme est beaucoup plus performant, aussi bien en termes de complexité temps qu'en termes de complaxité mémoire, que celui présenté dans la partie 1.
Nous pensons qu'il est acceptable du fait de sa complexité temps O(n) et de sa complexité mémoire constante.


