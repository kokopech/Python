import json
import csv
from pathlib import Path

class Sauvegarde:

    #Classe qui gère la sauvegarde et le chargement des données de la bibliothèque au format JSON ou CSV.

    def __init__(self, dossier="data", format_fichier="json"):
        # Création du dossier s'il n'existe pas
        self.dossier = Path(dossier)
        self.dossier.mkdir(exist_ok=True)
        self.format = format_fichier.lower()


    # SAUVEGARDE DES DONNÉES

    def sauvegarder(self, livres, utilisateurs):
        #Sauvegarde les données selon le format choisi (JSON ou CSV)
        if self.format == "json":
            self._sauvegarder_json("livres.json", livres)
            self._sauvegarder_json("utilisateurs.json", utilisateurs)
        elif self.format == "csv":
            self._sauvegarder_csv("livres.csv", livres)
            self._sauvegarder_csv("utilisateurs.csv", utilisateurs)

        print(f"Sauvegarde effectuée en {self.format.upper()} dans le dossier '{self.dossier}'.")


    # CHARGEMENT DES DONNÉES

    def charger(self):
        #Charge les données selon le format choisi (JSON ou CSV)
        data = {"livres": [], "utilisateurs": []}

        if self.format == "json":
            data["livres"] = self._charger_json("livres.json")
            data["utilisateurs"] = self._charger_json("utilisateurs.json")
        elif self.format == "csv":
            data["livres"] = self._charger_csv("livres.csv")
            data["utilisateurs"] = self._charger_csv("utilisateurs.csv")

        print(f"Chargement des données terminé ({self.format.upper()})")
        return data


    # MÉTHODES POUR JSON

    def _sauvegarder_json(self, nom_fichier, contenu):
        chemin = self.dossier / nom_fichier
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(contenu, f, ensure_ascii=False, indent=2)

    def _charger_json(self, nom_fichier):
        chemin = self.dossier / nom_fichier
        if chemin.exists():
            with open(chemin, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            print(f"Fichier {nom_fichier} non trouvé, aucune donnée chargée.")
            return []


    # MÉTHODES POUR CSV

    def _sauvegarder_csv(self, nom_fichier, contenu):
        chemin = self.dossier / nom_fichier
        if len(contenu) > 0:
            with open(chemin, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=contenu[0].keys())
                writer.writeheader()
                writer.writerows(contenu)
        else:
            with open(chemin, "w", newline="", encoding="utf-8") as f:
                f.write("")  # fichier vide si aucune donnée

    def _charger_csv(self, nom_fichier):
        chemin = self.dossier / nom_fichier
        if chemin.exists():
            with open(chemin, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                return list(reader)
        else:
            print(f"Fichier {nom_fichier} non trouvé, aucune donnée chargée.")
            return []
