from icos import Icos
from character import *
from manager import Manager

map = Icos()
map.place_base()
map.place_base()
print(map.bases)

blueWar = Warrior(1, 1, 1)
redWar = Warrior(2, 1, 2)
blueArcher = Archer(3, 1, 1)
redArcher = Archer(4, 1, 2)
blueSprinter = Sprinter(5, 1, 1)
redSprinter = Sprinter(6, 1, 2)
blueBuilder = Builder(7, 1, 1)
redBuilder = Builder(8, 1, 2)

team1 = [blueWar, blueArcher, blueSprinter, blueBuilder]
team2 = [redWar, redArcher, redSprinter, redBuilder]

manager = Manager(9, [{'players': team1}, {'players': team2}])
