from datetime import datetime


class Utilisateur:
    compteur_id = 1

    def __init__(self, nom_complet, email, type_utilisateur):
        self.__id = Utilisateur.compteur_id
        Utilisateur.compteur_id += 1
        self.__nom_complet = nom_complet
        self.__email = email
        self.__type_utilisateur = type_utilisateur

    @property
    def id(self):
        return self.__id

    @property
    def nom_complet(self):
        return self.__nom_complet

    @property
    def email(self):
        return self.__email

    @property
    def type_utilisateur(self):
        return self.__type_utilisateur

    @nom_complet.setter
    def nom_complet(self, nouveau_nom):
        if len(nouveau_nom) >= 3:
            self.__nom_complet = nouveau_nom
        else:
            print("Le nom doit contenir au moins 3 caracteres")

    @email.setter
    def email(self, nouvel_email):
        if "@" in nouvel_email and "." in nouvel_email:
            self.__email = nouvel_email
        else:
            print("Email invalide")

    def __str__(self):
        return f"ID: {self.__id}, Nom: {self.__nom_complet}, Email: {self.__email}, Type: {self.__type_utilisateur}"

    def _a_les_droits_bibliothecaire(self):
        return self.__type_utilisateur == "Bibliothecaire"


class Lecteur(Utilisateur):

    def __init__(self, nom_complet, email):
        super().__init__(nom_complet, email, "Lecteur")
        self.__livres_empruntes = {}

    @property
    def livres_empruntes(self):
        return self.__livres_empruntes.copy()

    def emprunter_livre(self, livre):
        if livre.est_disponible():
            livre.nbr_exemplaire_disp = livre.nbr_exemplaire_disp - 1
            self.__livres_empruntes[livre.ID] = datetime.now()
            print(f"{self.nom_complet} a emprunte '{livre.titre}'")
            return True
        else:
            print(f"Le livre '{livre.titre}' n'est pas disponible")
            return False

    def rendre_livre(self, livre):
        if livre.ID in self.__livres_empruntes:
            livre.nbr_exemplaire_disp = livre.nbr_exemplaire_disp + 1
            date_emprunt = self.__livres_empruntes[livre.ID]

            jours_emprunt = (datetime.now() - date_emprunt).days

            del self.__livres_empruntes[livre.ID]

            if jours_emprunt > 14:
                retard = jours_emprunt - 14
                print(f"ATTENTION : Retard de {retard} jour(s) !")
                print(f"{self.nom_complet} a rendu '{livre.titre}' apres {jours_emprunt} jours")
            else:
                print(f"{self.nom_complet} a rendu '{livre.titre}' apres {jours_emprunt} jour(s)")

            return True
        else:
            print(f"{self.nom_complet} n'a pas emprunte ce livre")
            return False

    def afficher_emprunts(self):
        if not self.__livres_empruntes:
            print(f"{self.nom_complet} n'a aucun livre emprunte")
        else:
            print(f"\nEmprunts de {self.nom_complet} :")
            for livre_id, date_emprunt in self.__livres_empruntes.items():
                jours_ecoules = (datetime.now() - date_emprunt).days
                statut_retard = ""
                if jours_ecoules > 14:
                    statut_retard = f" RETARD de {jours_ecoules - 14} jour(s)"
                print(
                    f"   - Livre ID {livre_id} emprunte le {date_emprunt.strftime('%d/%m/%Y')} ({jours_ecoules} jour(s)){statut_retard}")


class Bibliothecaire(Utilisateur):

    def __init__(self, nom_complet, email):
        super().__init__(nom_complet, email, "Bibliothecaire")

    def ajouter_livre(self, bibliotheque, livre):
        if not self._a_les_droits_bibliothecaire():
            print("Action refusee : droits insuffisants")
            return False

        bibliotheque._ajouter_livre_interne(livre)
        print(f"{self.nom_complet} (bibliothecaire) a ajoute le livre '{livre.titre}'")
        return True

    def modifier_livre(self, livre, nouveau_titre=None, nouvel_auteur=None,
                       nouvelle_categorie=None, nouveau_nbr=None):
        if not self._a_les_droits_bibliothecaire():
            print("Action refusee : droits insuffisants")
            return False
        if nouveau_titre:
            livre.titre = nouveau_titre
        if nouvel_auteur:
            livre.auteur = nouvel_auteur
        if nouvelle_categorie:
            livre.categorie = nouvelle_categorie
        if nouveau_nbr is not None:
            livre.nbr_exemplaire_disp = nouveau_nbr

        print(f"{self.nom_complet} (bibliothecaire) a modifie le livre '{livre.titre}'")
        return True

    def supprimer_livre(self, bibliotheque, id_livre):
        if not self._a_les_droits_bibliothecaire():
            print("Action refusee : droits insuffisants")
            return False

        if bibliotheque._supprimer_livre_interne(id_livre):
            print(f"{self.nom_complet} (bibliothecaire) a supprime le livre ID {id_livre}")
            return True
        return False