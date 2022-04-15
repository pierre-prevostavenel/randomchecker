# randomchecker
Un projet simple en Python pour vérifier que la fonction random.random() est aussi aléatoire que l'on puisse le mesurer.

Utilise les bibliothèques random et matplotlib.

Pour *tester une autre fonction d'aléatoire* que random.random(), remplacer à la ligne 9 cette fonction par celle à tester. 
Si la fonction testée ne retourne pas exclusivement des valeurs comprises entre 0 et 1, remplacer les 0.5 par la moyenne théorique ((Vmax - Vmin) / 2).

Exemple de fonctionnement du programme avec n = 15 :
![Des valeurs tendant vers 0 quand n augmente](https://raw.githubusercontent.com/pierre-prevostavenel/randomchecker/main/Exemple.png)
