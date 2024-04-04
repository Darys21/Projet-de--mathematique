# Définition de la fonction pour saisir une matrice
def saisir_matrix():
    # Demander à l'utilisateur le nombre de lignes et le nombre de colonnes
    rows = int(input("Entrez le nombre de lignes : "))
    cols = int(input("Entrez le nombre de colonnes : "))

    # Initialiser une liste vide pour stocker la matrice
    matrix = []
    # Parcourir chaque ligne de la matrice
    for i in range(rows):
        # Demander à l'utilisateur d'entrer les éléments de la ligne
        row = list(map(int, input(f"Entrez les éléments de la ligne {i+1} : ").split()))
        # Vérifier si le nombre d'éléments entrés correspond au nombre de colonnes
        if len(row) != cols:
            raise ValueError("Le nombre d'éléments entrés ne correspond pas au nombre de colonnes.")
        # Ajouter la ligne à la matrice
        matrix.append(row)

    # Retourner la matrice saisie
    return matrix

# Définition de la fonction pour multiplier deux matrices
def produit_matrix(matrix1, matrix2):
    # Initialiser une matrice résultat remplie de zéros
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]

    # Parcourir les lignes de la première matrice
    for i in range(len(matrix1)):
        # Parcourir les colonnes de la deuxième matrice
        for j in range(len(matrix2[0])):
            # Parcourir les éléments communs pour effectuer la multiplication
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    # Retourner le produit des deux matrices
    return result

# Définition de la fonction pour obtenir la transposée d'une matrice
def transpose_matrix(matrix):
    # Utiliser une compréhension de liste pour obtenir la transposée
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Définition de la fonction principale du projet
def projet_dit():
    # Afficher les options du menu
    print("1. Calculer la transposée d'une matrice")
    print("2. Calculer le produit de deux matrices")

    # Demander à l'utilisateur de faire un choix
    choice = int(input("Entrez votre choix (1 ou 2) : "))

    # Si l'utilisateur choisit de calculer la transposée d'une matrice
    if choice == 1:
        # Saisir une matrice
        matrix = saisir_matrix()
        # Calculer la transposée de la matrice
        transpose = transpose_matrix(matrix)
        # Afficher la transposée de la matrice
        print("La transposée de la matrice est : ")
        for row in transpose:
            print(row)
    # Si l'utilisateur choisit de calculer le produit de deux matrices
    elif choice == 2:
        # Saisir les deux matrices
        matrix1 = saisir_matrix()
        matrix2 = saisir_matrix()

        # Vérifier la compatibilité des dimensions pour la multiplication
        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Le nombre de colonnes de la première matrice ne correspond pas au nombre de lignes de la deuxième matrice.")

        # Calculer le produit des deux matrices
        product = produit_matrix(matrix1, matrix2)
        # Afficher le produit des deux matrices
        print("Le produit des deux matrices est : ")
        for row in product:
            print(row)
    # Si l'utilisateur choisit une option invalide
    else:
        print("Choix invalide.")

# Appeler la fonction principale du projet pour démarrer le programme
projet_dit()