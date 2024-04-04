# Projet DIT (Démonstration et Implémentation de la Transposée et du Produit de Matrices)

Ce projet a été réalisé par ANGUILET Joan-Yves Darys, étudiant en Master à Dakar Institute of Technologies (DIT), promotion Master Janvier 2024.

## Description
Le projet DIT est un programme Python qui permet de calculer la transposée d'une matrice et le produit de deux matrices. Il offre une interface utilisateur simple qui 
guide l'utilisateur à travers les différentes étapes de la saisie des matrices et du choix de l'opération à effectuer.

## Fonctionnalités
- Saisie d'une matrice : L'utilisateur peut saisir une matrice en entrant le nombre de lignes et de colonnes, puis les éléments de chaque ligne.
- Calcul de la transposée d'une matrice : Le programme calcule la transposée d'une matrice saisie par l'utilisateur et affiche le résultat.
- Calcul du produit de deux matrices : Le programme calcule le produit de deux matrices saisies par l'utilisateur, après avoir vérifié la compatibilité de leurs dimensions,
puis affiche le résultat.

## Utilisation
Pour exécuter le programme, il suffit de lancer le fichier `projet_dit.py`. L'utilisateur sera accueilli par un menu lui proposant de choisir entre le calcul de la transposée
d'une matrice et le calcul du produit de deux matrices. En fonction du choix de l'utilisateur, le programme demandera la saisie des matrices et affichera le résultat de l'opération 
choisie.

## Structure du code
Le code est organisé en quatre fonctions principales :
- `saisir_matrix()` : Cette fonction permet de saisir une matrice en demandant à l'utilisateur d'entrer le nombre de lignes, le nombre de colonnes, et les éléments de chaque ligne.
- `produit_matrix(matrix1, matrix2)` : Cette fonction calcule le produit de deux matrices en multipliant les éléments correspondants et en additionnant les résultats.
- `transpose_matrix(matrix)` : Cette fonction calcule la transposée d'une matrice en utilisant une compréhension de liste.
- `projet_dit()` : Cette fonction est la fonction principale du programme. Elle affiche le menu, demande à l'utilisateur de faire un choix, et appelle les fonctions appropriées en 
    fonction du choix de l'utilisateur.

## Tests unitaires
Des tests unitaires ont été réalisés pour vérifier le bon fonctionnement des fonctions `saisir_matrix()`, `produit_matrix()`, et `transpose_matrix()`. 
Ces tests sont disponibles dans le fichier `test_projet_dit.py`.

## Auteur
ANGUILET Joan-Yves Darys
Étudiant en Master à Dakar Institute of Technologies (DIT)
Promotion Master Janvier 2024
GitHub @Darys21