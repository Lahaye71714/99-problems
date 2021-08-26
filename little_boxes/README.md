                                        -------- Fonction little_boxes --------


Cette fonction reçoit en premier paramètre une chaîne de caractères ASCII.
Elle doit renvoyer une chaîne contenant les mêmes caractères que la chaîne originale, triés dans l'ordre ASCII


                              -------- Explication des solutions intermédiaires --------
                                      

En python il existe une fonction sorted() qui permet de trier les éléments de n'importe quel conteneur ou itérable.
On obtiens une fonction très compacte :

                                        def little_boxes(s):
                                        return(sorted(s))

La fonction sorted() est une fonction qui utilise un algorithme appelé Timsort qui est un algorithme de tri hybride dérivé du tri par fusion (merge sort) et du tri par insertion (insertion sort). L'algorithme procède en cherchant des parties de l'entrée déjà correctement ordonnées, et peut de cette manière trier efficacement l'ensemble des données en procédant par fusions successives. Elle est de complexité temps O(n log(n)) dans le pire des cas.
Cette fonction remvoie toujours une liste qui par défaut est triée par ordre croissant des éléments du conteneur.
Cet algorithme a une complexité temps O(n log(n)) et une complexité mémoire linéaire O(n) étant donné que la fonction sorted renvoie une nouvelle chaîne de cararctères qui est de la même taille que la chaîne de caractère entrée en paramètre. Cet algorithme n'est donc pas optimal en terme de complexité temps.


Dans un deuxième temps nous avons essayé de réduire la complexité mémoire de l'algorithme en utilisant la méthode sort(), ce qui donne l'implémentation suivante :


                                        def little_boxes(s):

                                            s = list(s)
                                            s.sort()
                                            s = "".join(s)
                                        
                                            return s


La méthode sort() s'applique surtout à des listes et pas à des conteneurs non mutables tels que les chaînes de caractères et les tuples, ni à des ensembles tels que les sets. Il est donc nécessaire de transformer la chaîne de caractère s en liste pour pouvoir utiliser la méthode sort(). La méthode sort() présente une complexité temps O(n log(n)) en python.
La méthode sort() modifie la liste initiale en la triant. Elle ne crée pas de nouvelle liste et ne renvoie rien. De ce point de vue elle pe
rmet de conserver une complexité mémoire constante O(1).
La méthode list() a une complexité temps linéraire O(n) car la durée de l'exécution dépend de la longueur de la chaîne de caractères.
La méthode join() permet de joindre les éléments d'un itérable en une chaîne de caractères. Elle a une complexité temps linéaire O(n) car la durée d'exécution dépend de la longueur de la liste.
Cet algorithme présente une complexité temps O(n log(n) + 2n) soit O(n log(n)). En terme de complexité mémoire, étant donné que la chaîne de caractères devient une liste et la liste de nouveau une chaîne de caractères, cet algorithme a une complexité mémoire constante O(1).
Il n'est toujours pas optimal du point de vue de la complexité temps. Cependant sa complexité mémoire est inférieure à celle de l'algorithme précédent.



Cette implémentation comprend deux fonctions. La fonction fusion et la fonction little_boxes qui fait appel à la fonction fusion :


                                      def fusion(liste1, liste2):
                                      
                                          liste = []
                                          i = 0
                                          j = 0
                                          
                                          while i < len(liste1) and j < len(liste2):
                                                if liste1[i] <= liste2[j]:
                                                    liste.append(liste1[i])
                                                    i += 1
                                                else:
                                                    liste.append(liste2[j])
                                                    j += 1

                                          while i < len(liste1):
                                                liste.append(liste1[i])
                                                i += 1
                                                
                                          while j < len(liste2):
                                                liste.append(liste2[j])
                                                j += 1

                                          return "".join(liste)



                                          def little_boxes(s):
                                          
                                              if len(s) < 1:
                                                 return s
                                              else:
                                                 liste1 = little_boxes(s[:len(s)//2])
                                                 liste2 = little_boxes(s[len(s)//2:])
                                                 
                                              return fusion(liste1, liste2)


Pour cette solution nous avons opté pour un tri fusion qui a une complexité temps en O(nlog(n)) dans le pire des cas.
La partie tri d'une fonction de type tri fusion consiste à séparer la chaîne de caractères en deux listes à peu près égales (à un élément prêt si les éléments de la chaîne de caractères sont en nombre impair). Les deux listes sont triées de manière récursive et chaque liste si elle contient un nombre délément supérieur à 1 est divisée en deux listes à peu près égale jusqu'à ce que chaque élément contenu dans les deux listes soit des listes contenant un élément. La division des deux listes en deux présente une complexité temps en O(log2(n)). Et comme cette opération dépend de la taille des listes elle est exécutée n fois. Le tri récursif a donc une complexité temps en O(n log2(n)) soit O(n log(n)).
La deuxième opération, qui est la fusion, a une complexité temps qui dépend de la somme de la taille des deux listes. Comme la somme de la taille des deux listes est égale à la taille de la chaîne de caractères initiale, l'opération de fusion a une complexité temps en O(n).
En terme de complexité mémoire, on crée tout d'abord deux nouvelles listes dont la somme des tailles est égale à la taille de la chaîne de caractères à trier, puis on crée une chaîne de caractères à partir des deux listes qui est de même taille que la chaîne de caractères initiale. La complexité mémoire de cet algorithme est en O(3n) soit O(n).



                                     -------- Explication de la solution finale --------


                                     def little_boxes(s):
                                     
                                         if len(s) < 2:
                                            return s
                                         else:
                                            output = [0 for i in range(128)]
                                            count = [0 for i in range(128)]
                                            s = list(s)
                                            for i in s:
                                                count[ord(i)] += 1
                                            for i in range(1, 128):
                                                count[i] += count[i-1]
                                            for i in range(1, len(s)):
                                                output[count[ord(s[i])]-1] = s[i]
                                                count[ord(s[i])] -= 1
                                            for i in range(len(s)):
                                                s[i] = str(output[i])
                                            s = "".join(s)
                                            
                                         return s


Nous avons opté ici pour un tri par comptage.
La première condition if contient une opération de comparaison en tant constant O(1).
On crée deux listes, output et count, de taille 128. La création de chacune des listes est de complexité temps linéraire O(m). La transformation de la chaîne de caractères avec la méthode list() dépend de la longueur n de la chaîne de caractères. Elle a donc une complexité temps en O(n). Trois boucles for dépendent de la longueur n de la chaîne de caractères et une boucle for dépend de la longueur m. Ces quatre boucles contiennent soit des opérations d'assignation et ou des opérations numériques qui sont de complexité temps constant O(1). Ces boucles for ont donc toutes une complexité temps en O(n). La transformation de la liste en chaîne de caractères avec la méthode join() dépend de la taille l de la liste qui est égale à la taille n de la chaîne de caractères. On peut donc dire que cette opération a une complexité temps en O(n). Au vue des complexités temps de l'ensemble des opérations contenues dans le fonction little_boxes, on peut dire que cette dernière a une complexité temps linéaire en O(m).
Du point de vue de la complexité mémoire, étant donné qu'on assigne à deux listes une taille m qui reste la même tout au long de l'exécution des opérations et que la chaîne de caractères est changée en liste puis de nouveau en chaîne de caractères, on peut dire que cet algorithme a une complexité mémoire constante O(1).
Au vue de la complexité temps linéaire O(n) et de la complexité mémoire constante O(1) qui répondent aux exigences de l'énoncé, nous considérons que cet algorithme est acceptable.





                                     -------- Explication de la solution bonus --------
                                     

Pour le plaisir une implémentation qui utilise la récursivité :
                                     
                                          def fusion(list1,list2):
                                              if list1==[] :
                                                 return list2
                                              if list2==[] :
                                                 return list1
                                              if list1[0]<list2[0] :
                                                 return [list1[0]]+fusion(list1[1:],list2)
                                              else :
                                                 return [list2[0]]+fusion(list1,list2[1:])

                                          def little_boxes(s):
                                              if len(s) < 2 :
                                                 return s
                                              list1=[s[x] for x in range(len(s)//2)]
                                              list2=[s[x] for x in range(len(s)//2,len(s))]
                                              return fusion(little_boxes(list1),little_boxes(list2))


L'output de cet algorithme est une liste. Nous n'avons pas réussi à transformer la liste en chaîne de caractères. ^^'
Le nombre de comparaisons dans la fonction fusion dépend de la taille des deux listes qui sont la moitié de s, donc chacune de longueur n/2 si on arrondi pour simplifier. Fusion demande à chaque appel au plus n/2 comparaisons. Soit C(n) le nombre de comparaisons C(n) <= 2 x C(n/2) + n/2 soit C(n) <= k*n + 1/2*n*log2(n) soit C(n) <= nlog(n).
La création des listes dans la fonction little_boxes est une opération qui dépend de la longueur de s, elle a donc un complexité temps linéaire O(n). La complexité temps de cet algorithme est égale à la complexité temps de la fonction fusion.
Cet algorithme a une complexité mémoire élévée car il y a de nombreuses recopies de tableaux lors des appels.