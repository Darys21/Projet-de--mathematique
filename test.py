import unittest
import Projet_DIT

# Unittest pour le projet DIT

import unittest
from io import StringIO
from contextlib import redirect_stdout

class TestProjetDit(unittest.TestCase):
    def test_saisir_matrix(self):
        # Rediriger la sortie standard pour simuler l'entrée utilisateur
        with redirect_stdout(StringIO()) as f:
            input = ("3\n"
                     "4\n"
                     "1 2 3 4\n"
                     "5 6 7 8\n"
                     "9 10 11 12\n")
            matrix = saisir_matrix()
            self.assertEqual(matrix, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

    def test_produit_matrix(self):
        matrix1 = [[1, 2, 3], [4, 5, 6]]
        matrix2 = [[7, 8], [9, 10], [11, 12]]
        product = produit_matrix(matrix1, matrix2)
        self.assertEqual(product, [[58, 64], [139, 154]])

    def test_transpose_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        transpose = transpose_matrix(matrix)
        self.assertEqual(transpose, [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

if __name__ == '__main__':
    unittest.main()
