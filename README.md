# Projet Python


Ce projet consiste a crée un système de gestion d'une bibliothèque, cela permet ainsi de gérer :
- Les livres  
- Les utilisateurs  
- Les emprunts  
- Avoir une sauvegarde des données ainsi qu'un chargement 
- Une visualisation des statistiques par le biais de graphiques

## 1. Contenu du projet

Ce projet est composé de plusieurs fichié Python :

### 1.1 `menu.py`

C'est le fichier à exécuter pour lancer le programme, il gère l'interaction avec l'utilisateur en affichant les différents menus

### 1.2 `livre.py`

Il contient la classe `Livre` qui représente chaque livre de la bibliothèque.  

### 1.3 `utilisateur.py`

Il contient les classes liées aux utilisateurs

### 1.4 `bibliotheque.py`

Il gère toute la logique de la bibliothèque 

### 1.5 `Sauvegarde.py`

Il permet de conserver les données entre deux utilisations du programme.

### 1.6 `statistiques.py`

Il génère des statistiques et des graphiques concernant la bibliothèque 


Deux types d’utilisateurs existent :

- Bibliothécaire : qui gére les livres 
- Lecteur : qui emprunte ou rend des livres et peuvent consulter leurs emprunts


## 2. Fonctionnalités principales

### 2.1 Une gestion des livres (réservée aux bibliothécaires) qui permet :
- Ajouter un livre
- Modifier un livre
- Supprimer un livre
- Afficher tous les livres
- Rechercher les livre (par titre, auteur ou catégorie)

Chaque livre possède :
- un ID unique généré automatiquement
- un titre
- un auteur
- une catégorie
- un nombre d'exemplaires disponibles
- un statut d'emprunt (Disponible ou Indisponible)


### 2.2 Une gestion des utilisateurs

Opérations disponibles :
- Ajouter un utilisateur (Lecteur ou Bibliothécaire)
- Modifier un utilisateur
- Supprimer un utilisateur
- Afficher tous les utilisateurs
- Rechercher un utilisateur



### 2.3 Une gestion des emprunts (réservée aux lecteurs)
Un lecteur peut :
- emprunter un livre 
- rendre un livre
- consulter la liste de ses emprunts

Lors d’un emprunt :
- le livre passe en indisponible si plus aucun exemplaire est disponible
- la liste d’emprunts du lecteur est mise à jour  
- l’inventaire de la bibliothèque est mis à jour



### 2.4 Une Sauvegarde et Chargement des données
Les données peuvent être enregistrées et rechargées en :
- JSON
- CSV

Contenu sauvegardé :
- la liste des livres
- la liste des utilisateurs

Au chargement, les objets sont reconstruits automatiquement

### 2.5 Statistiques
Avec `statistiques.py`, le programme génère :
- Des graphiques sur les livres
- Des statistiques sur les utilisateurs  

Les graphiques sont enregistrés dans le dossier `/figures`

Afin d'utiliser les statistiques, il faut d'abord sauvegarder en CSV



## 3. Installation

### Bibliothèques importées
  - json
  - csv
  - matplotlib
  - collections
  - pathlib
  - pandas

