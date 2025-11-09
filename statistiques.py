import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def generer_statistiques(dossier="data", dossier_figures="figures"):
    dossier = Path(dossier)
    dossier_figures = Path(dossier_figures)
    dossier_figures.mkdir(exist_ok=True)

    try:
        livres = pd.read_csv(dossier / "livres.csv")
        utilisateurs = pd.read_csv(dossier / "utilisateurs.csv")

        livres.groupby("categorie")["nbr_exemplaire_disp"].sum().plot(kind="bar", color="skyblue")
        plt.title("Livres par categorie")
        plt.xlabel("Categorie")
        plt.ylabel("Nombre d'exemplaires")
        plt.tight_layout()
        plt.savefig(dossier_figures / "livres_par_categorie.png")
        plt.close()

        utilisateurs["type"].value_counts().plot(kind="pie", autopct="%1.0f%%", colors=["lightgreen", "lightcoral"])
        plt.title("Repartition des utilisateurs")
        plt.ylabel("")
        plt.tight_layout()
        plt.savefig(dossier_figures / "utilisateurs_par_type.png")
        plt.close()

        print("Graphiques enregistres dans 'figures/'")

    except FileNotFoundError as e:
        print(f"Erreur : Fichier CSV introuvable - {e}")
    except Exception as e:
        print(f"Erreur lors de la generation des statistiques : {e}")