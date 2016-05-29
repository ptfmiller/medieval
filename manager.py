'''
manager.py

A manager for one game. Allows players to submit moves, coordinates
results, and provides information to player clients.
'''

from icos import Icos
import random


class Manager(object):

    def __init__(self, id, teams):
        # Record id
        self.id = id

        # Build map
        self.map = Icos()

        # Record players present
        self.teams = teams

        # Place bases and players


        # Place powerups

        # Record the beginning state

    def spaces_visible(self, player_id):
        '''
        Return a list of the spaces visible to this character. Used by
        objects_visible function
        '''
        pass

    def objects_visible(self, player_id):
        '''
        Return a list of all objects visible to a character, and their
        location
        '''
        pass
