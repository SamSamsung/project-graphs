from graphes import *
from graphes_decidabilite import *

class Calcul():
    """
    La classe decide est prise en paramètre, elle a elle meme la classe graphe en paramètre
    On se sert de toutes les fonctions de la classe decide
    """
    def __init__(self, decidabilite):
        self.decide = decidabilite
        self.graphe = self.decide.graphe
        self.lettres = self.graphe.lettres
        self.length = self.graphe.length
        
        

    def __str__(self):
        # On utilise la fonction str de la classe decide
        return self.graphe.__str__()

    """
    On rajoute toutes ces fonctions qui n'ont pas besoin d'être réappelés pour que l'utilisateur puisse y acceder depuis ce fichier.
    """
    
    def brute_force(self, k):
        # On utilise la fonction brute_force de la classe decide
        return self.decide.brute_force(k)
    
    def tri_brute_force_doublons(self, k):
        # On utilise la fonction tri_brute_force_doublons de la classe decide
        return self.decide.tri_brute_force_doublons(k)


    def est_clique(self, k):
        # On utilise la fonction est_clique de la classe decide
        return self.decide.est_clique(k)


    def clique(self, k):
        """
        On modifie cette fonction par rapport à la fonction de la decidabilite pour qu'elle puisse renvoyer la liste et non un booléan
        """
        L = self.tri_brute_force_doublons(k)  # On récupère la liste des chemins triés
        for i in range(len(L)):
            est_clique = True
            for j in range(k):  # Pour chaque combinaison, on passe dessus le nb de sommets de la combinaison pour former le nombre de couples suffisants aux tests des voisins (k).
                for f in range(j+1,k):  # On fait commencer la boucle avec le sommet d'après pour ne pas prendre en compte lui meme.
                    if not self.graphe.est_voisin(L[i][j], L[i][f]):
                        est_clique = False
            if est_clique == True:
                return L[i] # On vérifie bien que tous les sommets de la combinaison sont voisins avant de mettre la liste.
        return None


    def clique_plus_grande(self):
        for i in range(1, self.length+2): # On fait +2 pour que s'il existe une clique de taille self.length, elle soit bien montrée.
            if not self.est_clique(i): # Si une clique de taille i n'existe pas,
                return self.clique(i-1) # On retourne la clique d'avant, étant la plus grande.





# Si l'on veut faire des tests
"""
C = Calcul(Decide(Graphe(nb_sommets, type_graphe, type_sommets_graphe)))
print(C)
"""

if __name__ == "__main__":
    print("Les fonction du fichier gaphes_calculabilite vont être expliquées.")
    print("On utilise la classe Decide et donc Graphe pour la classe Calcul.\n")
    
    n = int(input("Donnez le nombre de sommets d'un graphe pour l'explication de la résolution du problème: "))
    A = Calcul(Decide(Graphe(n)))
    
    time.sleep(1)
    print("On rappelle la forme de la matrice :")
    print(A)

    if inp:
        input() # Si inp est true, on attend que l'utilisateur appuie sur une touche avant de continuer.
    else:
        time.sleep(1) # Sinon on fait attendre.


    print("\nPour ce problème, le problème de calculabilité, on va utiliser la classe Decide qui va permettre de résoudre le problème.")
    print("On utilise donc les mêmes fonctions: brute_force(), __str__, tri_brute_force_doublons(), est_clique()...")
    
    if inp:
        input()
    else:
        time.sleep(3)

    print("\nOn va simplement utiliser le problème de décidabilité pour regarder toutes les cliques du graphe.")
    print("On va utiliser la fonction clique() pour retourner une clique de taille n//2.")
    
    if inp:
        input()
    else:
        time.sleep(2.5)
    
    print("\nIl faut d'abord vérifier s'il existe une clique de taille n//2 :", end="")

    
    time.sleep(1.5)


    if A.est_clique(n//2):
        print(" Oui")
        print(f"On retourne une clique de taille {n//2} : ", end="")
        
        time.sleep(1.5)
        
        print(A.clique(n//2))

    else:
        print(" Non")
        print(f"Une clique de taille {n//2} n'existe pas dans la grille.")
    
    
    if inp:
        input()
    else:
        time.sleep(2.5)
    
    print("\nOn va ensuite utiliser la fonction clique_plus_grande()")
    print("On va faire une boucle de 1 à la taille de la liste dans laquelle on vérifie qu'une clique existe.")
    
    if inp:
        input()
    else:
        time.sleep(3)
    
    print("\nDès que l'on voit qu'une clique de taille p n'existe pas, on retourne une clique de taille p-1.")
    print("On a donc retourné la plus grande clique du graphe.")

    if inp:
        input()
    else:
        time.sleep(3)
    
    print(f"\nQuelle est la plus grande clique du graphe avec {n} sommets ? :", end=" ")
    
    
    time.sleep(1.5)
    
    print(A.clique_plus_grande())

    if inp:
        input()
    else:
        time.sleep(5)
    

    # On montre le résultat des problèmes avec la génération d'instances de tailles différentes.
    print("\n\nNous allons tester la résolution du problème de calculabilité avec plusieurs matrices de taille différentes : ")
    
    for i in range(4,12):
        print("\nMatrice de taille :", i)
        
        if inp:
            input()
        else:
            time.sleep(2)    
        
        a = time.time()
        print("La clique la plus grande est :", Calcul(Decide(Graphe(i))).clique_plus_grande())
        b = time.time()
        print("L'execution a pris : ", str(b-a) + "s")