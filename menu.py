from livre import Livre
from utilisateur import Lecteur, Bibliothecaire
from bibliotheque import Bibliotheque
from sauvegarde import Sauvegarde
from statistiques import generer_statistiques


def menu():

    bibliotheque = Bibliotheque()

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1) Gerer les livres")
        print("2) Gerer les utilisateurs")
        print("3) Gerer les emprunts")
        print("4) Sauvegarder / Charger les donnees")
        print("5) Visualiser les statistiques")
        print("0) Quitter")

        choix1 = input("Que voulez-vous faire ? ")

        match choix1:

            case "1":
                try:
                    id_utilisateur = int(input("ID de l'utilisateur : "))
                except ValueError:
                    print("ID invalide, saisir un autre ID (nombre entier)")
                    continue

                bibliothecaire = bibliotheque.rechercher_utilisateur(id_utilisateur)
                if not bibliothecaire:
                    print("Utilisateur introuvable")
                    continue

                if bibliothecaire.type_utilisateur.lower() != "bibliothecaire":
                    print("Acces refuse : Seuls les bibliothecaires peuvent gerer les livres")
                    continue

                while True:
                    print("\n=== GESTION DES LIVRES ===")
                    print("1) Ajouter un livre")
                    print("2) Modifier un livre")
                    print("3) Supprimer un livre")
                    print("4) Afficher les livres")
                    print("5) Rechercher un livre")
                    print("0) Retour")
                    choix2 = input("Que voulez-vous faire ? ")

                    match choix2:

                        case "1":
                            titre = input("Titre du livre : ")
                            auteur = input("Auteur du livre : ")
                            categorie = input("Categorie du livre : ")
                            try:
                                nb_ex = int(input("Nombre d'exemplaires du livre : "))
                            except ValueError:
                                print("Nombre invalide")
                                continue
                            livre = Livre(titre, auteur, categorie, nb_ex)
                            bibliothecaire.ajouter_livre(bibliotheque, livre)

                        case "2":
                            try:
                                id_livre = int(input("ID du livre a modifier : "))
                            except ValueError:
                                print("ID invalide, saisir un autre ID (nombre entier)")
                                continue

                            livre = None
                            for l in bibliotheque.livres:
                                if l.ID == id_livre:
                                    livre = l
                                    break

                            if livre is None:
                                print("Le livre est introuvable")
                                continue

                            print("Livre trouve :", livre)
                            print("Saisir les nouvelles informations (Vide si pas de modification):")
                            nouveau_titre = input("Nouveau titre : ").strip() or None
                            nouvel_auteur = input("Nouvel auteur : ").strip() or None
                            nouvelle_cat = input("Nouvelle categorie : ").strip() or None
                            nb_str = input("Nouveau nombre d'exemplaires : ").strip()
                            try:
                                nouveau_nbr = int(nb_str) if nb_str else None
                            except ValueError:
                                print("Valeur du stock invalide, pas de modification")
                                nouveau_nbr = None

                            bibliothecaire.modifier_livre(
                                livre,
                                nouveau_titre=nouveau_titre,
                                nouvel_auteur=nouvel_auteur,
                                nouvelle_categorie=nouvelle_cat,
                                nouveau_nbr=nouveau_nbr
                            )
                            print("Livre modifie !")

                        case "3":
                            try:
                                id_livre = int(input("ID du livre a supprimer : "))
                            except ValueError:
                                print("ID invalide. Saisir un autre ID (nombre entier)")
                                continue

                            livre = None
                            for l in bibliotheque.livres:
                                if l.ID == id_livre:
                                    livre = l
                                    break

                            if livre is None:
                                print("Le livre est introuvable")
                                continue

                            print("Livre trouve :", livre)
                            print("Voulez-vous supprimer ce livre ? (1 pour confirmer, 0 pour annuler)")
                            try:
                                c = int(input("Votre choix : "))
                            except ValueError:
                                print("Choix invalide")
                                continue
                            if c == 1:
                                bibliothecaire.supprimer_livre(bibliotheque, id_livre)
                                print("Livre supprime !")
                            elif c == 0:
                                print("Suppression annulee !")

                        case "4":
                            if len(bibliotheque.livres) == 0:
                                print("Aucun livre present dans la bibliotheque.")
                            else:
                                bibliotheque.afficher()

                        case "5":
                            mot = input("Entrer un mot (titre, auteur ou categorie) : ")
                            if mot.strip() == "":
                                print("Recherche vide, saisissez un mot.")
                            else:
                                bibliotheque.recherche(mot)

                        case "0":
                            break

                        case _:
                            print("Choix invalide")

            case "2":
                while True:
                    print("\n=== GESTION DES UTILISATEURS ===")
                    print("1) Ajouter un utilisateur")
                    print("2) Modifier un utilisateur")
                    print("3) Supprimer un utilisateur")
                    print("4) Afficher les utilisateurs")
                    print("5) Rechercher un utilisateur")
                    print("0) Retour")
                    choix2 = input("Que voulez-vous faire ? ")

                    match choix2:

                        case "1":
                            nom = input("Nom complet de l'utilisateur : ")
                            email = input("Email de l'utilisateur : ")
                            type_user = input("Lecteur ou Bibliothecaire : ").strip().lower()
                            if type_user == "lecteur":
                                utilisateur = Lecteur(nom, email)
                            elif type_user == "bibliothecaire":
                                utilisateur = Bibliothecaire(nom, email)
                            else:
                                print("Type invalide. Tape 'lecteur' ou 'bibliothecaire'.")
                                continue

                            bibliotheque.ajouter_utilisateur(utilisateur)

                        case "2":
                            try:
                                id_utilisateur = int(input("ID de l'utilisateur a modifier : "))
                            except ValueError:
                                print("ID invalide. Saisir un autre ID (nombre entier)")
                                continue

                            utilisateur = bibliotheque.rechercher_utilisateur(id_utilisateur)
                            if not utilisateur:
                                print("Utilisateur introuvable")
                                continue

                            print("Utilisateur trouve :", utilisateur)
                            print("Saisir les nouvelles informations (Vide si pas de modification):")
                            nouveau_nom = input("Nouveau Nom complet : ").strip() or None
                            nouvel_email = input("Nouvel email : ").strip() or None

                            bibliotheque.modifier_utilisateur(id_utilisateur, nouveau_nom, nouvel_email)
                            print("Utilisateur modifie !")

                        case "3":
                            try:
                                id_utilisateur = int(input("ID de l'utilisateur a supprimer : "))
                            except ValueError:
                                print("ID invalide. Saisir un autre ID (nombre entier)")
                                continue

                            utilisateur = bibliotheque.rechercher_utilisateur(id_utilisateur)
                            if not utilisateur:
                                print("Utilisateur introuvable")
                                continue

                            print("Utilisateur trouve :", utilisateur)
                            print("Voulez-vous supprimer cet utilisateur ? (1 pour confirmer, 0 pour annuler)")

                            try:
                                c = int(input("Votre choix : "))
                            except ValueError:
                                print("Choix invalide")
                                continue
                            if c == 1:
                                bibliotheque.supprimer_utilisateur(id_utilisateur)
                                print("Utilisateur supprime !")
                            elif c == 0:
                                print("Suppression annulee !")
                            else:
                                print("Choix invalide")

                        case "4":
                            bibliotheque.afficher_utilisateurs()

                        case "5":
                            try:
                                id_utilisateur = int(input("ID de l'utilisateur : "))
                            except ValueError:
                                print("ID invalide. Saisir un autre ID (nombre entier)")
                                continue

                            utilisateur = bibliotheque.rechercher_utilisateur(id_utilisateur)

                            if not utilisateur:
                                print("Utilisateur introuvable.")
                            else:
                                print("Utilisateur trouve :", utilisateur)

                        case "0":
                            break

                        case _:
                            print("Choix invalide")

            case "3":
                try:
                    id_utilisateur = int(input("Votre ID utilisateur : "))
                except ValueError:
                    print("ID invalide. Saisir un autre ID (nombre entier)")
                    continue

                utilisateur = bibliotheque.rechercher_utilisateur(id_utilisateur)
                if not utilisateur:
                    print("Utilisateur introuvable")
                    continue

                if utilisateur.type_utilisateur.lower() != "lecteur":
                    print("Il faut etre lecteur pour emprunter ou rendre des livres")
                    continue

                while True:
                    print("\n=== GESTION DES EMPRUNTS ===")
                    print("1) Emprunter un livre")
                    print("2) Rendre un livre")
                    print("3) Voir mes emprunts")
                    print("0) Retour")
                    choix2 = input("Que voulez-vous faire ? ")

                    match choix2:

                        case "1":
                            try:
                                id_livre = int(input("ID du livre a emprunter : "))
                            except ValueError:
                                print("ID invalide. Saisir un autre ID (nombre entier)")
                                continue

                            livre = None
                            for l in bibliotheque.livres:
                                if l.ID == id_livre:
                                    livre = l
                                    break

                            if livre is None:
                                print("Livre introuvable")
                                continue

                            utilisateur.emprunter_livre(livre)

                        case "2":
                            try:
                                id_livre = int(input("ID du livre a rendre : "))
                            except ValueError:
                                print("ID invalide. Saisir un autre ID (nombre entier)")
                                continue

                            livre = None
                            for l in bibliotheque.livres:
                                if l.ID == id_livre:
                                    livre = l
                                    break

                            if livre is None:
                                print("Livre introuvable")
                                continue
                            utilisateur.rendre_livre(livre)

                        case "3":
                            utilisateur.afficher_emprunts()

                        case "0":
                            break

                        case _:
                            print("Choix invalide")

            case "4":
                format_selectionne = None
                sauvegarde = None

                while True:
                    print("\n=== SAUVEGARDE / CHARGEMENT ===")
                    print("1) Choisir JSON")
                    print("2) Choisir CSV")
                    print("3) Sauvegarder")
                    print("4) Charger")
                    print("0) Retour")
                    choix2 = input("Choix : ")

                    match choix2:

                        case "1":
                            format_selectionne = "json"
                            sauvegarde = Sauvegarde(format_fichier="json")
                            print("Format JSON selectionne.")

                        case "2":
                            format_selectionne = "csv"
                            sauvegarde = Sauvegarde(format_fichier="csv")
                            print("Format CSV selectionne.")

                        case "3":
                            if not sauvegarde:
                                print("Choisissez d'abord JSON ou CSV (1 ou 2)")
                                continue

                            livres_dicts = []
                            for l in bibliotheque.livres:
                                livres_dicts.append({
                                    "ID": l.ID,
                                    "titre": l.titre,
                                    "auteur": l.auteur,
                                    "categorie": l.categorie,
                                    "nbr_exemplaire_disp": l.nbr_exemplaire_disp,
                                    "statut": l.statut
                                })

                            utilisateurs_dicts = []
                            for u in bibliotheque.utilisateurs.values():
                                utilisateurs_dicts.append({
                                    "id": u.id,
                                    "nom_complet": u.nom_complet,
                                    "email": u.email,
                                    "type_utilisateur": u.type_utilisateur
                                })

                            sauvegarde.sauvegarder(livres_dicts, utilisateurs_dicts)
                            print("Sauvegarde effectuee !")

                        case "4":
                            if not sauvegarde:
                                print("Choisissez d'abord JSON ou CSV (1 ou 2).")
                                continue

                            data = sauvegarde.charger()
                            bibliotheque = Bibliotheque()

                            for d in data.get("livres", []):
                                titre = d.get("titre", "")
                                auteur = d.get("auteur", "")
                                categorie = d.get("categorie", "")
                                try:
                                    nb = int(d.get("nbr_exemplaire_disp", 0))
                                except (ValueError, TypeError):
                                    nb = 0
                                livre = Livre(titre, auteur, categorie, nb)
                                bibliotheque._ajouter_livre_interne(livre)

                            for d in data.get("utilisateurs", []):
                                nom = d.get("nom_complet", "")
                                email = d.get("email", "")
                                t = str(d.get("type_utilisateur", "")).lower()
                                if t == "lecteur":
                                    user = Lecteur(nom, email)
                                else:
                                    user = Bibliothecaire(nom, email)
                                bibliotheque.ajouter_utilisateur(user)

                            print("Chargement effectue !")

                        case "0":
                            break

                        case _:
                            print("Choix invalide")

            case "5":
                print("Generation des statistiques...")
                generer_statistiques()

            case "0":
                print("Au revoir")
                break

            case _:
                print("Choix invalide")


if __name__ == "__main__":
    menu()