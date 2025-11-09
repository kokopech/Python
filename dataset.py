import pandas as pd
from pathlib import Path


dossier_data = Path("data")
dossier_figures = Path("figures")
dossier_data.mkdir(exist_ok=True)
dossier_figures.mkdir(exist_ok=True)


livres = pd.DataFrame([
    {"id": 1, "titre": "Python pour les nuls", "auteur": "Paul Dupont", "categorie": "informatique", "nbr_exemplaire_disp": 3, "statut": True},
    {"id": 2, "titre": "Apprendre Java", "auteur": "Claire Dubois", "categorie": "informatique", "nbr_exemplaire_disp": 4, "statut": True},
    {"id": 3, "titre": "L'Univers en expansion", "auteur": "Jean-Pierre Lemoine", "categorie": "science", "nbr_exemplaire_disp": 2, "statut": True},
    {"id": 4, "titre": "Les Miserables", "auteur": "Victor Hugo", "categorie": "roman", "nbr_exemplaire_disp": 5, "statut": True},
    {"id": 5, "titre": "1984", "auteur": "George Orwell", "categorie": "dystopie", "nbr_exemplaire_disp": 3, "statut": True},
    {"id": 6, "titre": "Le Meilleur des Mondes", "auteur": "Aldous Huxley", "categorie": "dystopie", "nbr_exemplaire_disp": 2, "statut": True},
    {"id": 7, "titre": "Histoire de France", "auteur": "Jean Martin", "categorie": "histoire", "nbr_exemplaire_disp": 4, "statut": True},
    {"id": 8, "titre": "Les Grandes Batailles", "auteur": "Louis Bernard", "categorie": "histoire", "nbr_exemplaire_disp": 1, "statut": True},
    {"id": 9, "titre": "L'Odyssee", "auteur": "Homere", "categorie": "roman", "nbr_exemplaire_disp": 3, "statut": True},
    {"id": 10, "titre": "Le Seigneur des Anneaux", "auteur": "J.R.R. Tolkien", "categorie": "fantasy", "nbr_exemplaire_disp": 2, "statut": True},
    {"id": 11, "titre": "Harry Potter a l'ecole des sorciers", "auteur": "J.K. Rowling", "categorie": "fantasy", "nbr_exemplaire_disp": 5, "statut": True},
    {"id": 12, "titre": "La Machine a explorer le temps", "auteur": "H.G. Wells", "categorie": "science", "nbr_exemplaire_disp": 2, "statut": True},
    {"id": 13, "titre": "La Guerre des Mondes", "auteur": "H.G. Wells", "categorie": "science", "nbr_exemplaire_disp": 3, "statut": True},
    {"id": 14, "titre": "Les Robots", "auteur": "Isaac Asimov", "categorie": "informatique", "nbr_exemplaire_disp": 4, "statut": True},
    {"id": 15, "titre": "Fondation", "auteur": "Isaac Asimov", "categorie": "science", "nbr_exemplaire_disp": 3, "statut": True},
    {"id": 16, "titre": "L'Alchimiste", "auteur": "Paulo Coelho", "categorie": "roman", "nbr_exemplaire_disp": 4, "statut": True},
    {"id": 17, "titre": "Les Fleurs du Mal", "auteur": "Charles Baudelaire", "categorie": "roman", "nbr_exemplaire_disp": 3, "statut": True},
    {"id": 18, "titre": "Voyage au centre de la Terre", "auteur": "Jules Verne", "categorie": "science", "nbr_exemplaire_disp": 5, "statut": True},
    {"id": 19, "titre": "20 000 lieues sous les mers", "auteur": "Jules Verne", "categorie": "science", "nbr_exemplaire_disp": 2, "statut": True},
    {"id": 20, "titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupery", "categorie": "roman", "nbr_exemplaire_disp": 6, "statut": True},
])


utilisateurs = pd.DataFrame([
    {"id": 1, "nom": "Alice Martin", "email": "alice@mail.com", "type": "Lecteur"},
    {"id": 2, "nom": "Jean Dupuis", "email": "jean@mail.com", "type": "Bibliothecaire"},
    {"id": 3, "nom": "Louise Petit", "email": "louise@mail.com", "type": "Lecteur"},
    {"id": 4, "nom": "Marc Lefebvre", "email": "marc@mail.com", "type": "Bibliothecaire"},
    {"id": 5, "nom": "Lucie Bernard", "email": "lucie@mail.com", "type": "Lecteur"},
    {"id": 6, "nom": "Thomas Leroy", "email": "thomas@mail.com", "type": "Lecteur"},
    {"id": 7, "nom": "Camille Renault", "email": "camille@mail.com", "type": "Lecteur"},
    {"id": 8, "nom": "Nicolas Fabre", "email": "nicolas@mail.com", "type": "Lecteur"},
    {"id": 9, "nom": "Julie Caron", "email": "julie@mail.com", "type": "Lecteur"},
    {"id": 10, "nom": "Pauline Marchand", "email": "pauline@mail.com", "type": "Lecteur"},
])


livres.to_csv(dossier_data / "livres.csv", index=False, encoding="utf-8")
utilisateurs.to_csv(dossier_data / "utilisateurs.csv", index=False, encoding="utf-8")

print("Dataset cree : 20 livres et 10 utilisateurs enregistres dans 'data/'.")
