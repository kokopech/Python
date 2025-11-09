class Bibliotheque:

    def __init__(self):
        self.__livres = []
        self.__utilisateurs = {}

    @property
    def livres(self):
        return self.__livres.copy()

    @property
    def utilisateurs(self):
        return self.__utilisateurs.copy()

    def _ajouter_livre_interne(self, livre):
        self.__livres.append(livre)

    def _modifier_livre_interne(self, id_livre, nouveau_titre=None, nouvel_auteur=None,
                                nouvelle_categorie=None, nouveau_statut=None):
        for livre in self.__livres:
            if livre.ID == id_livre:
                if nouveau_titre:
                    livre.titre = nouveau_titre
                if nouvel_auteur:
                    livre.auteur = nouvel_auteur
                if nouvelle_categorie:
                    livre.categorie = nouvelle_categorie
                if nouveau_statut is not None:
                    livre.statut = nouveau_statut
                return True
        print(f"Livre ID {id_livre} non trouve")
        return False

    def _supprimer_livre_interne(self, id_livre):
        for livre in self.__livres:
            if livre.ID == id_livre:
                self.__livres.remove(livre)
                return True
        print(f"Livre ID {id_livre} non trouve")
        return False

    def afficher(self):
        if not self.__livres:
            print("La bibliotheque est vide")
            return

        for livre in self.__livres:
            print(livre)

    def recherche(self, mot):
        resultats = []

        for livre in self.__livres:
            statut_str = "Disponible" if livre.statut else "Emprunte"
            if (mot.lower() in livre.titre.lower() or
                mot.lower() in livre.auteur.lower() or
                mot.lower() in livre.categorie.lower() or
                mot.lower() in statut_str.lower()):
                resultats.append(livre)

        if resultats:
            for livre in resultats:
                print(livre)
        else:
            print("Aucun resultat trouve")

        return resultats

    def ajouter_utilisateur(self, utilisateur):
        self.__utilisateurs[utilisateur.id] = utilisateur
        print(f"Utilisateur '{utilisateur.nom_complet}' ajoute (ID: {utilisateur.id})")

    def supprimer_utilisateur(self, id_utilisateur):
        if id_utilisateur in self.__utilisateurs:
            user = self.__utilisateurs.pop(id_utilisateur)
            print(f"Utilisateur '{user.nom_complet}' supprime")
        else:
            print(f"Utilisateur ID {id_utilisateur} non trouve")

    def modifier_utilisateur(self, id_utilisateur, nouveau_nom=None, nouvel_email=None):
        if id_utilisateur in self.__utilisateurs:
            user = self.__utilisateurs[id_utilisateur]
            if nouveau_nom:
                user.nom_complet = nouveau_nom
            if nouvel_email:
                user.email = nouvel_email
            print(f"Utilisateur ID {id_utilisateur} modifie")
        else:
            print(f"Utilisateur ID {id_utilisateur} non trouve")

    def afficher_utilisateurs(self):
        if not self.__utilisateurs:
            print("Aucun utilisateur enregistre")
            return

        for user in self.__utilisateurs.values():
            print(user)

    def rechercher_utilisateur(self, id_utilisateur):
        return self.__utilisateurs.get(id_utilisateur)