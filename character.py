'''
character.py

Contain the information for a character
'''


class Character(object):

    def __init__(self, player_id, manager_id, team):
        self.player_id = player_id
        self.manager_id = manager_id
        self.vision = 1
        self.team = team


class Warrior(Character):

    def __init__(self, player_id, manager_id, team):
        Character.__init__(self, player_id, manager_id, team)
        self.attack = 3
        self.influence = 3


class Archer(Character):

    def __init__(self, player_id, manager_id, team):
        Character.__init__(self, player_id, manager_id, team)
        self.attack = 2
        self.influence = 2


class Sprinter(Character):

    def __init__(self, player_id, manager_id, team):
        Character.__init__(self, player_id, manager_id, team)
        self.attack = 2
        self.influence = 4


class Builder(Character):

    def __init__(self, player_id, manager_id, team):
        Character.__init__(self, player_id, manager_id, team)
        self.attack = 1
        self.influence = 1
