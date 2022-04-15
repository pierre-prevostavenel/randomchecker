import matplotlib.pyplot as plt
import random


def randomtester(n: int) -> float:
    """Retourne l'écart entre la moyenne théorique obtenue aléatoirement et la moyenne effectivement obtenue"""
    # En théorie, quand n → +∞, le pourcentage d'erreur → 0

    return abs(0.5 - sum([random.random() for _ in range(n)]) / n) / 0.5
    # On prend n fois un nombre aléatoire
    # Ensuite, on en calcule la moyenne (somme des nombres aléatoires / n)
    # Enfin, on calcule l'erreur (entre 0 et 1), qu'on retourne


if __name__ == "__main__":
    tests = range(15)  # On veut effectuer 15 tests
    erreurs = [randomtester(2 ** j) for j in tests]  # Pour chaque test, on prend la puissance de 2 correspondante

    plt.plot(tests, erreurs)
    plt.ylabel("Erreur constatée")
    plt.xlabel("Taille de l'échantillon (en puissance de 2)")
    plt.show()
