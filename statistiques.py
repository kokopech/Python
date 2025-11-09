import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def generer_statistiques(dossier="data", dossier_figures="figures"):

    # Lit les fichiers CSV contenant les livres et les utilisateurs, puis génère des graphiques dans le dossier 'figures'.

    dossier = Path(dossier)
    dossier_figures = Path(dossier_figures)
    dossier_figures.mkdir(exist_ok=True)

    # Lecture des fichiers CSV
    livres_fichier = dossier / "livres.csv"
    utilisateurs_fichier = dossier / "utilisateurs.csv"

    if not livres_fichier.exists() or not utilisateurs_fichier.exists():
        print("Les fichiers CSV sont introuvables. Aucune statistique générée.")
        return

    livres = pd.read_csv(livres_fichier)
    utilisateurs = pd.read_csv(utilisateurs_fichier)

    # 1. Graphique : nombre de livres par catégorie

    if "categorie" in livres.columns and "nbr_exemplaire_disp" in livres.columns:
        livres_par_cat = livres.groupby("categorie")["nbr_exemplaire_disp"].sum()
        plt.figure(figsize=(7, 4))
        livres_par_cat.plot(kind="bar", color="skyblue")
        plt.title("Nombre total de livres par catégorie")
        plt.xlabel("Catégorie")
        plt.ylabel("Nombre d'exemplaires")
        plt.tight_layout()
        plt.savefig(dossier_figures / "livres_par_categorie.png")
        plt.close()
        print("Graphique 'livres_par_categorie.png' généré.")
    else:
        print("Colonnes manquantes dans livres.csv (categorie, nbr_exemplaire_disp)")


    # 2. Graphique : répartition des utilisateurs par type

    if "type_utilisateur" in utilisateurs.columns:
        plt.figure(figsize=(6, 6))
        utilisateurs["type_utilisateur"].value_counts().plot(
            kind="pie", autopct="%1.0f%%", colors=["lightgreen", "lightcoral"])
        plt.title("Répartition des utilisateurs par type")
        plt.ylabel("")
        plt.tight_layout()
        plt.savefig(dossier_figures / "utilisateurs_par_type.png")
        plt.close()
        print("Graphique 'utilisateurs_par_type.png' généré.")
    else:
        print("Colonne 'type_utilisateur' absente du fichier utilisateurs.csv")
