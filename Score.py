from labyrinthe import Labyrinthe
from Jeu import Jeu

class Score ():
    def __init__(self):
        """Initialisation des variables"""
        self.score=0
        self.labyrinthe=Labyrinthe()
        self.matrice_finale=[[]]
        self.position_etoiles=self.labyrinthe.place_etoiles(self.matrice_finale)
        self.position_enigmes=self.labyrinthe.place_enigmes(self.matrice_finale)
        
        self.jeu=Jeu()
        self.position_joueur= ...
        
    def sur_etoile (position_etoiles, position_joueur):
        ...

    def sur_enigme (position_enigmes, position_joueur):
        ...
        
        

    
        
        