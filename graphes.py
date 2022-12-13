# Creer un graphe avec signalisations


# On importe le module random pour génerer (dans la mesure du possible) aléatoirement des graphes
import random
# On importe en chaine de caractère, les lettres de l'alphabet pour les utiliser en tant que sommet.
import string
# On import le module time pour expliquer le programme étape par étape
import time


class Graphe():
    def __init__(self, taille, type="matrice", type_sommets="alph"):
        self.lettres = list(string.ascii_uppercase) # On creer une liste avec comme éléments les lettres de l'alphabet
        self.length = taille  # On initialise la taille de la liste
        self.type = type # On initialise le type de la matrice
        self.type_sommets = type_sommets # On initialise le type des sommets
        if self.verif_type_liste_adj(): # On génère différement chaque graphe en fonction des paramètres
            if self.type_sommets == "nombres":
                self.memoire = self.generer_liste_adj()
            else:
                self.memoire = self.generer_liste_adj_alph()
        else:
            self.memoire = self.generer_matrice() 


    # [[0,1,1,1,1], [1,0,1,1,1], [1,1,0,1,1],[1,1,1,0,1], [1,1,1,1,0]] -> Matrice avec clique de la taille de la matrice, utile pour tester
    def __str__(self):
        return str(self.memoire) # On retourne le str, pour le print

    def recup_sommets(self):
        """
        Retourne sous forme de liste, tous les sommets du graphe
        """
        L = []
        if self.verif_type_sommets_nombres():
            # On gère le cas ou les sommets sont des nombres
            for i in range(self.length):
                L.append(i)
        else:
            # On gère le cas ou les sommets sont des lettres de l'alphabet.
            for i in range(self.length):
                L.append(self.transformer_autre_sens(i)) # On prend l'index et on le transforme à la lettre qui lui correspond
        return L

    def est_voisin(self, sommet1, sommet2):
        """
        Redirige les fonctions en fonctions du type du graphe et du type des sommets du graphe
        """
        if self.verif_type_liste_adj():
            if not self.verif_type_sommets_nombres() and isinstance(sommet1, str): # Si les sommets sont des nombres et si c'est une liste adjacente:
                sommet1 = self.transformer(sommet1)  # On transforme le sommet1 en index
            return self.est_voisin_liste_adj(sommet1, sommet2)
        else:
            if not self.verif_type_sommets_nombres() and isinstance(sommet1, str):
                sommet1 = self.transformer(sommet1)  # On transforme le sommet1 en index
                sommet2 = self.transformer(sommet2)  # On transforme le sommet2 en index
            return self.est_voisin_matrice(sommet1, sommet2)




    """
    On genere des listes adjacentes ou des matrices avec comme sommets des nombres ou des lettres
    """

    def generer_liste_adj(self):
        L = [[] for x in range(self.length)] # On genere une liste vide pour ranger les sommets
        for i in range(self.length):
            for _ in range(random.randint(1, (self.length-1)//3)):
                sommet = random.randint(0,self.length-1)
                while sommet in L[i] or sommet == i:  # Tant que le sommet est déja dans la liste et que le nouveau sommet n'est pas égale a la liste dans laquelle on se trouve
                    sommet = random.randint(0,self.length-1)  # On recreer un nombre aléatoire
                if not i in L[sommet]: # and random.randint(0,100) >= 50: On rend aléatoire le double sens mais on ne le fait pas car on utilise les arbres ponderes
                    L[sommet].append(i)  # On rajoute le sommet a double sens dans l'autre 
                L[i].append(sommet)  # On rajoute des sommet aléatoires
        return L

    def generer_liste_adj_alph(self):
        L = [[[]] for x in range(self.length)] # On genere une liste vide avec encore une liste vide pour ranger les sommets et une autre pour les connexions
        for i in range(self.length):
            L[i].append(self.lettres[i]) # On range les lettres commes sommets sous la forme: [[[....], "A"], [[....], "B"]]
            
        for i in range(self.length):
            for _ in range(random.randint(1, (self.length-1)//3)):
                sommet_index = random.randint(0,self.length-1)
                sommet = self.lettres[sommet_index]
                while sommet in L[i][0] or sommet == L[i][1]:  # Tant que le sommet est déja dans la liste et que le nouveau sommet n'est pas égale a la liste dans laquelle on se trouve
                    sommet_index = random.randint(0,self.length-1)  # On recreer un nombre aléatoire
                    sommet = self.lettres[sommet_index]
                if not i in L[sommet_index][0]: #and random.randint(0,100) >= 50:   #On rend aléatoire le double sens
                    L[sommet_index][0].append(self.lettres[i])  # On rajoute le sommet a double sens dans l'autre 
                L[i][0].append(sommet)  # On rajoute des sommet aléatoires
        return L
        
    def generer_matrice(self):
        L = [[0 for x in range(self.length)] for x in range(self.length)]
        for i in range(self.length):
            for j in range(i, self.length): # On ne change qu'une seule partie de la matrice car elle est symetrique
                if i == j:  # Un sommet n'est pas connecte a lui meme donc on met 0
                    L[i][j] = 0
                elif random.randint(1,2) == 1:
                    L[i][j] = 1 # On rend la matrice aleatoire avec une chance sur deux que des sommets soient connectes
                L[j][i] = L[i][j] # On utilise la symetrie pour remplacer               
        return L









    """
    Ces 2 fonctions retournent vrai si les deux sommets sont connectes
    Fonctions appeles differements si on utilise des matrices ou alors des listes adjacentes avec comme sommets des lettres ou des nombres
    """

    def est_voisin_liste_adj(self, sommet1, sommet2):
        """
        Retourne vrai si deux sommets sont voisins, dans le cas d'une liste adjacente
        """
        for j in range(len(self.memoire[sommet1])):
            if self.memoire[sommet1][j] == sommet2:
                return True
        return False

  
    def est_voisin_matrice(self, sommet1, sommet2):
        """
        Retourne vrai si deux sommets sont voisins, dans le cas d'une matrice
        """
        return self.memoire[sommet1][sommet2] == 1






    def verif_type_liste_adj(self):
        # On verifie si le type de graphe choisi est une liste ajacente
        if self.type == "liste_adj":
            return True
        else:
            return False


    def verif_type_sommets_nombres(self):
        # On verifie si les types des sommets du graphe sont des nombres
        if self.type_sommets == "nombres":
            return True
        else:
            return False

    




    def transformer(self, lettre):
        """
        On transforme la lettre en son index dans l'alphabet: 
        Ex: A -> 0,      B -> 1,      C -> 2,       D -> 3,      E -> 4
        """
        for i in range(len(self.lettres)):
            if lettre == self.lettres[i]:
                return i
                    


    def transformer_autre_sens(self, index):
        """
        On fait l'inverse de la fonction transformer:
        Ex: 0 -> A,      1 -> B,      2 -> C,       3 -> D,      4 -> E
        """
        return self.lettres[index]






    def get_lettres(self):
        """
        Recuperer la liste des lettres des sommets utilises
        """
        return self.lettres


    def convertisseur(self):
        """
        On redirige la conversion en fonction des types de graphs et des types de sommet.
        """
        if self.verif_type_liste_adj():
            if not self.verif_type_sommets_nombres():
                # Si le type de sommet etait alphabétique, on convertie le graphe en liste adjacente en nombre
                self.convertisseur_liste_adj_alph_vers_nombres()
            # On prend une liste adjacente en nombre pour la convertir en matrice
            self.convertisseur_liste_adj_nombres_vers_matrice_nombres()
        # On converti de la matrice nombre à la matrice alphabétique
        self.convertisseur_matrice_nombres_vers_matrice_alph()



    def convertisseur_liste_adj_alph_vers_nombres(self):
        """
        Converti le graphe originallement, liste adjacente alph en liste adjacente avec des nombres
        """
        L = [[] for x in range(self.length)]
        # On génère une liste avec comme taille le nombre de sommets mais vide
        for i in range(self.length):
            for j in range(len(self.memoire[i][0])):
                # On transforme les lettres en index qui les correspondent
                nombre = self.transformer(self.memoire[i][0][j])
                L[i].append(nombre)
        self.memoire = L
        self.type_sommets = "nombres"

    def convertisseur_liste_adj_nombres_vers_matrice_nombres(self):
        """
        Converti le graphe originallement, liste adjacente nombres en matrice
        """
        # On crée une liste avec que des 0 pour pouvoir les remplacer
        L = [[0 for x in range(self.length)] for x in range(self.length)]
        for i in range(self.length):
            for j in range(len(self.memoire[i])):
                # Les éléments de la liste adjacente nombres sert d'index pour remplacer les zéros.
                L[i][self.memoire[i][j]] = 1
        self.memoire = L
        self.type = "matrice"


    def convertisseur_matrice_nombres_vers_matrice_alph(self):
        # La matrice ne changeant pas en fonction des sommets, seul son type de sommets change
        self.type_sommets = "alph"
    



    def test_est_voisin(self):
        """
        Une fonction pour retourner un exemple de deux sommets voisins
        """
        for i in range(self.length):
            for j in range(len(self.memoire[i])):
                if self.memoire[i][j] == 1:
                    return i, j
            

# Si l'on veut faire des tests
"""
A = Graphe(nb_sommets, type_graphe, type_sommets_graphe)
print(A)
"""


inp = True # Pour l'explication sur ordinateur, pour pouvoir expliquer étape par étape

if __name__ == "__main__":
    print("Les fonction du fichier gaphes vont être expliquées.\n")
    
    
    
    n = int(input("Veuillez donner le nombre de sommets d'un graphe aléatoire à tester : "))
    
    

    print("On génère un graphe avec {} sommets.".format(n))
    print("Nous allons générer des graphs de 4 manières différentes:")
    
    if inp:
        input() # Si inp est true, on attend que l'utilisateur appuie sur une touche avant de continuer
    else:
        time.sleep(2) # Sinon on fait attendre

    A = Graphe(n, "liste_adj", "alph")

    print("\n\nD'abord, générons le graphe sous une forme de liste adjacente avec des sommets alphabétiques :")
    
    time.sleep(1)
    
    print(A)
    
    if inp:
        input()
    else:
        time.sleep(1.5)
    
    print("\nRécupérons les sommets :")
    
    time.sleep(1)

    print(A.recup_sommets())
    
    if inp:
        input()
    else:
        time.sleep(2.5)

    
    print("\n\nMaintenant, générons le graphe sous une forme de liste adjacente avec des sommets numérotés :")
    
    time.sleep(1.5)
    
    A.convertisseur_liste_adj_alph_vers_nombres()
    print(A)
    
    if inp:
        input()
    else:
        time.sleep(1.5)
    
    print("\nRécupérons les sommets :")
    
    time.sleep(1)
    
    print(A.recup_sommets())
    
    if inp:
        input()
    else:
        time.sleep(2.5)


    print("\n\nEnsuite, générons le graphe sous une forme de matrice avec des sommets numérotés :")
    A.convertisseur_liste_adj_nombres_vers_matrice_nombres()
    
    time.sleep(1)
    
    print(A)
    
    if inp:
        input()
    else:
        time.sleep(1.5)
    
    print("\nRécupérons les sommets :")
    
    time.sleep(1)
    
    print(A.recup_sommets())
    
    if inp:
        input()
    else:
        time.sleep(2.5)
    
    
    
    
    print("\n\nFinalement, générons le graphe sous une forme de matrice avec des sommets alphabétiques; étant écris de la meme façon, la matrice sera la même :")
    A.convertisseur_matrice_nombres_vers_matrice_alph()
    

    time.sleep(1)
    
    print(A)
    
    if inp:
        input()
    else:
        time.sleep(1.5)
    
    print("\nSeulement les sommets sont différents : ")
    print("Récupérons les sommets :")
    
    time.sleep(1)
    
    print(A.recup_sommets())
    
    if inp:
        input()
    else:
        time.sleep(2.5)


    print("\nNous allons à présent utiliser des matrices avec des sommets alphabétiques.")
    print("Nous allons regarder si certains sommets sont voisins.")
    
    if inp:
        input()
    else:
        time.sleep(1.5)
    
    test_voisin = A.test_est_voisin()
    
    print("\n" + str(A.memoire))
    print(f"En effet, nous pouvons voir que dans la {test_voisin[0]+1} liste, se trouve à la {test_voisin[1]+1} position un 1.")
    print(f"Nous pouvons aussi voir qu'à la {test_voisin[1]+1} liste, se trouve à la {test_voisin[0]+1} position un 1.")
    print(f"\nDonc nous pouvons voir que {A.transformer_autre_sens(test_voisin[0])} est voisin avec {A.transformer_autre_sens(test_voisin[1])}.")
    print("C'est cette méthode qui sera utilisée pour la résolution des deux problèmes.")