from graphes import *


class Decide():
    def __init__(self, classe_graphe):
        """
        On utilise la classe Graphe en paramètre donc on utilise les initialisations déja faites
        """
        self.graphe = classe_graphe
        self.lettres = self.graphe.lettres
        self.length = self.graphe.length
        
        # On gère le cas ou le graphe est sous forme de liste_adj et on la convertie en matrice
        self.graphe. convertisseur()

    def __str__(self):
        return self.graphe. __str__() # On utilise la fonction de la classe Graph


    def brute_force(self, k):
        """
        On génère, avec de la brute force en récurcivité, toutes les combinaisons possibles de chemin avec k sommets
        """
        if k == 0:
            return [""]
        else:
            res = []
            for i in range(self.length): 
                for j in self.brute_force(k-1):
                    res.extend([self.lettres[i] + j ]) # On récupère tous les chemins dans la liste res
            return res


    def tri_brute_force_doublons(self, k):
        """
        On tri les chemins retournés par la fonction brute force
        """
        L_final = []
        L = self.brute_force(k)
        for i in range(len(L)):
            doublons = False
            for j in range(len(L[i])-1):
                # Avec la condition, on évite les doublons (AAA, BBB, CCC) et les répétitions: (AB et BA)
                if not self.graphe.transformer(L[i][j]) < self.graphe.transformer(L[i][j+1]): 
                    doublons = True
            if doublons == False: # On vérifie bien à la fin de l'analyse du chemin s'il n'y a pas eu de doublons
                L_final.append(L[i])
        return L_final
            


    def est_clique(self, k):
        """
        Renvoie vrai si une clique de taille k existe
        """
        L = self.tri_brute_force_doublons(k)
        for i in range(len(L)):
            est_clique = True
            for j in range(k):  # Pour chaque combinaison, on passe dessus le nb de sommets de la combinaison pour former le nombre de couples suffisants aux tests des voisins (k)
                for f in range(j+1,k):  # On fait commencer la boucle avec le sommet d'après pour ne pas prendre en compte lui meme
                    if not self.graphe.est_voisin(L[i][j], L[i][f]):
                        est_clique = False
            if est_clique == True:
                return True # On vérifie bien que tous les sommets de la combinaison sont voisins avant de mettre True
        return False # On retourne faux sans boucle car si une clique de taille k n'existe pas, une clique de taille k+1, k+2, k+3... n'existe pas

    


# Si l'on veut faire des tests
"""
B = Decide(Graphe(nb_sommets, type_graphe, type_sommets_graphe))
print(B)
"""



if __name__ == "__main__":


    print("Les fonction du fichier gaphes_decidabilité vont être expliquées.")
    print("On utilise la classe Graphe pour la classe Decide.\n")

    n = int(input("Donnez le nombre de sommets d'un graphe pour l'explication de la résolution du problème: "))
    A = Decide(Graphe(n))

    time.sleep(1)
    print("On rappelle la forme de la matrice :")
    print(A)

    if inp:
        input() # Si inp est true, on attend que l'utilisateur appuie sur une touche avant de continuer
    else:
        time.sleep(2) # Sinon on fait attendre

    print("\nLa fonction brute force prend un entier k en paramètre pour choisir combien de sommets doivent constituer un chemin: 1 -> A, 2 -> AB, 3 -> ABC...")
    print(f"\nNous allons générons tous les chemins possibles sans distinction, des chemins constitués de {n//2} sommets :\n")
    a = time.time()
    print(A.brute_force(n//2))
    b = time.time()
    print("L'execution a pris : ", str(b-a) + "s")
    
    if inp:
        input()
    else:
        time.sleep(3.5)

    print("\nOn va ensuite trier cette liste, enlever les doublons (AAAA, BBB, AAB, BAB) et les répétitions de chemin (AB et BA):")
    print(A.tri_brute_force_doublons(n//2))
    
    if inp:
        input()
    else:
        time.sleep(2)
    
    print("\nOn va maintenant regarder s'il existe une clique de taille supérieure ou égale à k.")
    print("Il est important de noter que s'il n'existe pas de clique de taille k, il n'existe pas de clique de taille k+1 et de k+2 et de k+3...")
    
    if inp:
        input()
    else:
        time.sleep(2)
    
    print("Il suffit donc de regarder s'il existe une clique de taille k.")
    print("\nOn prend les chemins générés par la brute force avec comme paramètre k et on regarde si tous les sommets du chemin sont voisins.")
    
    if inp:
        input()
    else:
        time.sleep(2)
    
    print("Existe-t-il une clique de taille", n//2, "dans ce graphe :", end=" ")
    
    
    time.sleep(1.5)
    
    print(A.est_clique(n//2))

    if inp:
        input()
    else:
        time.sleep(4)
    

    # On montre le résultat des problèmes avec la génération d'instances positives et négatives de tailles différentes
    print("\n\nNous allons tester la résolution du problème de décidabilité avec plusieurs matrices de taille différentes : ")
    
    for i in range(4,12):
        print("\nMatrice de taille :", i)
        
        if inp:
            input()
        else:
            time.sleep(2)    
        
        a = time.time()
        print("Existe-t-il une clique de taille ",i//2, ":" , Decide(Graphe(i)).est_clique(i//2))
        b = time.time()
        print("L'execution a pris : ", str(b-a) + "s")

    if inp:
            input()
    else:
        time.sleep(1.5)   

    print("\nPrenons un graphe sous cette forme: ")
    print("""
        [
            [0,1,0,0]
            [1,0,0,0]
            [0,0,0,1]
            [0,0,1,0]
        ]
    """)

    print("Existe-t-il une clique de taille 3 ?: Non")
    print("Existe-t-il une clique de taille 2 ?: Oui")