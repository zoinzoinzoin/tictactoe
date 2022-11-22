# Jeu du morpion
# Le joueur commence a jouer en premier, l'ordinateur joue ensuite

# Import des bibliotheques necessaires au programme
from game import *
from player import *
from human import *
from computer import *

# Choix de la configuration
print("1 - Joueur contre joueur\n2 - Joueur contre ordinateur\n3 - Ordinateur contre joueur")
config = 0
while config < 1 or config > 4:
    config = int(input("Choisissez une configuration : "))

if config == 1:
    Game(3, Human("X"), Human("O")).start()
elif config == 2:
    Game(3, Human("X"), Computer("O")).start()
elif config == 3:
    Game(3, Computer("X"), Human("O")).start()
else:
    print("Lancement du supercalculateur militaire WOPR")
    Game(3, Computer("X"), Computer("O")).start()
