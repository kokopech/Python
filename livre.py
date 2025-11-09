class Livre:
    compteur_id = 1

    def __init__(self, titre, auteur, categorie, nbr_exemplaire_disp, statut=False):
        self.__id = Livre.compteur_id
        Livre.compteur_id += 1
        self.__titre = titre
        self.__auteur = auteur
        self.__categorie = categorie
        self.__nbr_exemplaire_disp = nbr_exemplaire_disp
        self.__statut = statut

    @property
    def ID(self):
        return self.__id

    @property
    def titre(self):
        return self.__titre

    @property
    def auteur(self):
        return self.__auteur

    @property
    def categorie(self):
        return self.__categorie

    @property
    def nbr_exemplaire_disp(self):
        return self.__nbr_exemplaire_disp

    @property
    def statut(self):
        return self.__statut

    @titre.setter
    def titre(self, nouveau_titre):
        if len(nouveau_titre) >= 1:
            self.__titre = nouveau_titre
        else:
            print("Le titre ne peut pas etre vide")

    @auteur.setter
    def auteur(self, nouvel_auteur):
        if len(nouvel_auteur) >= 2:
            self.__auteur = nouvel_auteur
        else:
            print("Le nom de l'auteur doit contenir au moins 2 caracteres")

    @categorie.setter
    def categorie(self, nouvelle_categorie):
        categories_valides = ["roman", "science", "informatique", "fantasy",
                              "dystopie", "action", "histoire", "biographie"]
        if nouvelle_categorie.lower() in categories_valides:
            self.__categorie = nouvelle_categorie
        else:
            print(f"Categorie invalide. Categories valides : {', '.join(categories_valides)}")

    @nbr_exemplaire_disp.setter
    def nbr_exemplaire_disp(self, nouveau_nombre):
        if nouveau_nombre >= 0:
            self.__nbr_exemplaire_disp = nouveau_nombre
            self.__statut = (nouveau_nombre > 0)
        else:
            print("Le nombre d'exemplaires ne peut pas etre negatif")

    @statut.setter
    def statut(self, nouveau_statut):
        self.__statut = nouveau_statut

    def est_disponible(self):
        return self.__nbr_exemplaire_disp > 0

    def __str__(self):
        statut_txt = "Disponible" if self.__statut else "Emprunte"
        return (f"ID: {self.__id}, Titre: {self.__titre}, Auteur: {self.__auteur}, "
                f"Categorie: {self.__categorie}, Dispo: {self.__nbr_exemplaire_disp}, "
                f"Statut: {statut_txt}")

    def __repr__(self):
        return f"Livre(ID={self.__id}, titre='{self.__titre}')"