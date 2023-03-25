#bonjour bonjour 

class Labyrinthe():
    def __init__(self):
        """variables à initialiser"""
        
        
    def initialisation_matrice_cases(self, taille_grille):
        """Renvoie une mat carrée de 0 dont la taille est calculée en fonction
        de la taille souhaitée du plateau de jeu final (diviser par 2?)
        paramètres : taille_grille
        renvoie : mat_cases"""
        
        
    def initialisation_mat_murs(self, taille_grille):
        """Renvoie une matrice où chaque ligne représente de manière alternée 
        les murs verticaux et horizontaux par des 0 (contours du labyrinthe exclus)
        paramètres : taille_grille
        renvoie : mat_murs"""

    def creation_murs(self, mat_cases, mat_murs):
    	"""parcours en profondeur de mat_cases jusqu’à que tous les 0 soient changés en 1
        ification simultanée de mat_murs qui remplace les murs détruits par des 1
        Paramètres : mat_cases, mat_murs
        renvoie : mat_murs_cassés"""

    def placement_cases_speciales (self, mat_cases):
        """écrit une matrice où des cases spéciales ont été générées aléatoirement
        place le départ (en fonction de l'arrivée précédente?) et l'arrivée 
        Appel de la fonction place_etoiles
        Appel de la fonction place_enigmes
        vérifie si la case aléatoire désignée est libre pour mettre une case spéciale
        paramètres : mat_cases
        renvoie : mat_cases_labyrinthe"""
        
    def place_étoiles(self, mat_cases):
        """fonction qui place une ou plusieurs étoiles sur des cases chemin de la matrice. 
        Renvoie la position (coordonnées) de ces étoiles dans la matrice """
    
    
    def place_enigmes(self, mat_cases):
    	"""fonction qui place une ou plusieurs étoiles sur des cases chemin de la matrice. 
        Renvoie la position (coordonnées) de ces énigmes dans la matrice"""

        
    def creation_labyrinthe (self, mat_murs_cassés, mat_cases_labyrinthe):
        """
        fusionne les deux matrices en paramètre pour renvoyer une matrice carrée 
        de la taille de la grille demandée qui est le labyrinthe final jouable
        signification des chiffres dans la matrice finale :
            0 chemin
            1 mur
            2 départ
            3 arrivée
            4 étoile
            5 énigme
        paramètres : mat_murs_cassés, mat_cases_labyrinthe
        renvoie : matrice_finale"""
