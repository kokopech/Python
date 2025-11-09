from livre import Livre
from utilisateur import Lecteur, Bibliothecaire
from bibliotheque import Bibliotheque
from Sauvegarde import Sauvegarde
from statistiques import generer_statistiques


def menu():

    bibliotheque = Bibliotheque()

    while True:
        print("1) Gérer les livres")
        print("2) Gérer les utilisateurs")
        print("3) Gérer les emprunts")
        print("4) Sauvegarder / Charger les données")
        print("5) Visualiser les statistiques")
        print("0) Quitter")

        choix1=input("Que voulez-faire ?")

        match choix1:

            case "1":
                try :
                    id_utilisateur = int(input("ID de l'utilisateur : "))
                except ValueError:
                    print("ID invalide. Saisir un autre ID (nombre entier)")
                    continue

                bibliothecaire = bibliotheque.rechercher_utilisateur(id_utilisateur)
                if not bibliothecaire:
                    print("Utilisateur introuvable.")
                    continue

                if bibliothecaire.type_utilisateur.lower() != "bibliothecaire":
                    print("Accès refusé : Seuls les bibliothécaires peuvent gérer les livres.")
                    continue

                while True:
                    print("1) Ajouter un livre")
                    print("2) Modifier un livre")
                    print("3) Supprimer un livre")
                    print("4) Afficher les livres")
                    print("5) Rechercher un livre")
                    print("0) Retour")
                    choix2=input("Que voulez-faire ?")

                    match choix2:

                        case "1":
                            titre = input("Titre du livre : ")
                            auteur = input("Auteur du livre : ")
                            categorie = input("Catégorie du livre : ")
                            nb_ex = int(input("Nombre d'exemplaires du livre : "))
                            livre = Livre(titre, auteur, categorie, nb_ex)
                            bibliothecaire.ajouter_livre(bibliotheque, livre)

                        case "2":

                            try :
                                id_livre = int(input("ID du livre à modifier : "))
                            except ValueError:
                                print("ID invalide. Saisir un autre ID (nombre entier)")
                                continue

                            livre = None  # Variable vide au départ car on ne sait pas si le livre existe
                            for l in bibliotheque.livres: # on parcourt chaque livre de la bibliotheque
                                if l.ID == id_livre:
                                    livre = l  # on sauvegarde le livre trouvé dans la variable livre
                                    break


                            if livre is None:
                                print("Le livre est introuvable")
                                continue

                            print("Livre trouvé :", livre)
                            print("Saisir les nouvelles informations (Vide si pas de modification):")
                            nouveau_titre = input("Nouveau titre : ").strip() or None #strip au cas ou il y a des espaces et None si on veut pas modifier
                            nouvel_auteur = input("Nouvel auteur : ").strip() or None
                            nouvelle_cat = input("Nouvelle catégorie : ").strip() or None
                            nb_str = input("Nouveau nombre d'exemplaires : ").strip()
                            try:
                                nouveau_nbr = int(nb_str) if nb_str else None
                            except ValueError:
                                print("Valeur du stock invalide, pas de moficiation")
                                nouveau_nbr = None

                            bibliothecaire.modifier_livre(
                                livre,
                                nouveau_titre=nouveau_titre,
                                nouvel_auteur=nouvel_auteur,
                                nouvelle_categorie=nouvelle_cat,
                                nouveau_nbr=nouveau_nbr
                            )
                            print("Livre modifié !")

                        case "3":

                            try :
                                id_livre = int(input("ID du livre à supprimer : "))
                            except ValueError:
                                print("ID invalide. Saisir un autre ID (nombre entier)")
                                continue

                            livre = None  # Variable vide au départ car on ne sait pas si le livre existe
                            for l in bibliotheque.livres: # on parcourt chaque livre de la bibliotheque
                                if l.ID == id_livre:
                                    livre = l  # on sauvegarde le livre trouvé dans la variable livre
                                    break


                            if livre is None:
                                print("Le livre est introuvable")
                                continue

                            print("Livre trouvé :", livre)
                            print("Voulez-vous supprimer ce livre ? : (1 pour confirmer, 0 pour annuler")
                            c=int(input("Votre choix : "))
                            if c == 1 :
                                bibliothecaire.supprimer_livre(bibliotheque, id_livre)
                                print("Livre supprimé !")
                            elif c == 0 :
                                print("Suppresion annulée !")

                        case "4":

                            if len(bibliotheque.livres) == 0:
                                print("Aucun livre présent dans la bibliothèque.")
                            else:
                                bibliotheque.afficher()

                        case "5":
                            mot = input("Entrer un mot (titre, auteur ou catégorie) : ")
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
                    print("1) Ajouter un utilisateur")
                    print("2) Modifier un utilisateur")
                    print("3) Supprimer un utilisateur")
                    print("4) Afficher les utilisateur")
                    print("5) Rechercher un utilisateur")
                    print("0) Retour")
                    choix2=input("Que voulez-faire ?")

                    match choix2:

                        case "1":
                            nom = input("Nom complet de  l'utilisateur : ")
                            email = input("Email de l'utilisateur : ")
                            type = input("Lecteur ou Bibliothecaire : ").strip().lower()
                            if type == "lecteur":
                                utilisateur = Lecteur(nom, email)
                            elif type == "bibliothecaire":
                                utilisateur = Bibliothecaire(nom, email)
                            else:
                                print("Type invalide. Tape 'lecteur' ou 'bibliothecaire'.")
                                continue

                            bibliotheque.ajouter_utilisateur(utilisateur)


                        case "2":

                            try :
                                id_utilisateur = int(input("ID de l'utilisateur à modifier : "))
                            except ValueError:
                                print("ID invalide. Saisir un autre ID (nombre entier)")
                                continue

                            utilisateur = bibliotheque.rechercher_utilisateur(id_utilisateur)
                            if not utilisateur:
                                print("Utilisateur introuvable ")
                                continue

                            print("Utilisateur trouvé :", utilisateur)
                            print("Saisir les nouvelles informations (Vide si pas de modification):")
                            nouveau_nom = input("Nouveau Nom complet : ").strip() or None #strip au cas ou il y a des espaces et None si on veut pas modifier
                            nouvel_email = input("Nouvel email : ").strip() or None

                            bibliotheque.modifier_utilisateur(id_utilisateur, nouveau_nom, nouvel_email)

                            print("Utilisateur modifié !")

                        case "3":

                            try :
                                id_utilisateur = int(input("ID de l'utilisateur à modifier : "))
                            except ValueError:
                                print("ID invalide. Saisir un autre ID (nombre entier)")
                                continue

                            utilisateur = bibliotheque.rechercher_utilisateur(id_utilisateur)
                            if not utilisateur:
                                print("Utilisateur introuvable ")
                                continue

                            print("Utilisateur trouvé :", utilisateur)

                            print("Voulez-vous supprimer cet utilisateur ? : (1 pour confirmer, 0 pour annuler")

                            try:
                                c=int(input("Votre choix : "))
                            except ValueError:
                                print("ID invalide. Saisir un autre ID (nombre entier)")
                                continue
                            if c == 1 :
                                bibliotheque.supprimer_utilisateur(id_utilisateur)
                                print("Utilisateur supprimé !")
                            elif c == 0 :
                                print("Suppresion annulée !")
                            else :
                                print("Choix invalide")

                        case "4":

                                bibliotheque.afficher_utilisateurs()

                        case "5":
                            try :
                                id_utilisateur = int(input("ID de l'utilisateur : "))
                            except ValueError:
                                print("ID invalide. Saisir un autre ID (nombre entier)")
                                continue

                            utilisateur=bibliotheque.rechercher_utilisateur(id_utilisateur)

                            if not utilisateur:
                                print("Utilisateur introuvable .")
                            else:
                                print("Utilisateur trouvé :", utilisateur)

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
                    print("Il faut être lecteur pour emprunter ou rendre des livres")
                    continue

                while True:
                    print("1) Emprunter un livre")
                    print("2) Rendre un livre")
                    print("3) Voir mes emprunts")
                    print("0) Retour")
                    choix2 = input("Que voulez-faire ? : ")

                    match choix2:

                        case "1":
                            try:
                                id_livre = int(input("ID du livre à emprunter : "))
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
                                id_livre = int(input("ID du livre à rendre : "))
                            except ValueError:
                                print("ID invalide. Saisir un autre ID (nombre entier)")
                                continue

                            # Recherche du livre
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
                            print("Format JSON sélectionné.")

                        case "2":
                            format_selectionne = "csv"
                            sauvegarde = Sauvegarde(format_fichier="csv")
                            print("Format CSV sélectionné.")

                        case "3":
                            if not sauvegarde:
                                print("Choisissez d’abord JSON ou CSV (1 ou 2).")
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
                            print("Sauvegardé !")

                        case "4":
                            if not sauvegarde:
                                print("Choisissez d’abord JSON ou CSV (1 ou 2).")
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

                            print("Chargement fait !")

                        case "0":
                            break

                        case _:
                            print("Choix invalide.")


            case "5":
                print("Génération des statistiques")
                generer_statistiques()

            case "0":
                print("Au revoir")
                break

            case _:
                print("Choix invalide")

menu()
