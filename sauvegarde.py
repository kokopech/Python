import json
import csv
from pathlib import Path


class Sauvegarde:

    def __init__(self, format_fichier="json", dossier="data"):
        self.format_fichier = format_fichier.lower()
        self.dossier = Path(dossier)
        self.dossier.mkdir(exist_ok=True)

        if self.format_fichier == "json":
            self.fichier_livres = self.dossier / "livres.json"
            self.fichier_utilisateurs = self.dossier / "utilisateurs.json"
        elif self.format_fichier == "csv":
            self.fichier_livres = self.dossier / "livres.csv"
            self.fichier_utilisateurs = self.dossier / "utilisateurs.csv"
        else:
            raise ValueError("Format invalide. Choisir 'json' ou 'csv'")

    def sauvegarder(self, livres_dicts, utilisateurs_dicts):
        if self.format_fichier == "json":
            self._sauvegarder_json(livres_dicts, utilisateurs_dicts)
        elif self.format_fichier == "csv":
            self._sauvegarder_csv(livres_dicts, utilisateurs_dicts)

    def _sauvegarder_json(self, livres_dicts, utilisateurs_dicts):
        with open(self.fichier_livres, 'w', encoding='utf-8') as f:
            json.dump(livres_dicts, f, indent=4, ensure_ascii=False)

        with open(self.fichier_utilisateurs, 'w', encoding='utf-8') as f:
            json.dump(utilisateurs_dicts, f, indent=4, ensure_ascii=False)

    def _sauvegarder_csv(self, livres_dicts, utilisateurs_dicts):
        if livres_dicts:
            with open(self.fichier_livres, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=livres_dicts[0].keys())
                writer.writeheader()
                writer.writerows(livres_dicts)

        if utilisateurs_dicts:
            with open(self.fichier_utilisateurs, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=utilisateurs_dicts[0].keys())
                writer.writeheader()
                writer.writerows(utilisateurs_dicts)

    def charger(self):
        if self.format_fichier == "json":
            return self._charger_json()
        elif self.format_fichier == "csv":
            return self._charger_csv()

    def _charger_json(self):
        data = {"livres": [], "utilisateurs": []}

        try:
            if self.fichier_livres.exists():
                with open(self.fichier_livres, 'r', encoding='utf-8') as f:
                    data["livres"] = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Erreur de chargement livres JSON : {e}")

        try:
            if self.fichier_utilisateurs.exists():
                with open(self.fichier_utilisateurs, 'r', encoding='utf-8') as f:
                    data["utilisateurs"] = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Erreur de chargement utilisateurs JSON : {e}")

        return data

    def _charger_csv(self):
        data = {"livres": [], "utilisateurs": []}

        try:
            if self.fichier_livres.exists():
                with open(self.fichier_livres, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    data["livres"] = list(reader)
        except (FileNotFoundError, csv.Error) as e:
            print(f"Erreur de chargement livres CSV : {e}")

        try:
            if self.fichier_utilisateurs.exists():
                with open(self.fichier_utilisateurs, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    data["utilisateurs"] = list(reader)
        except (FileNotFoundError, csv.Error) as e:
            print(f"Erreur de chargement utilisateurs CSV : {e}")

        return data