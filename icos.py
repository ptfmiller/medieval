'''
icos.py

contains code for a truncated icosahedron, and provides functionality
for the game manager to interact with the modelled icosahedron
'''

import copy
import random


class Icos(object):

    def __init__(self):
        # valid faces
        self.faces_valid = range(32)

        # available faces
        self.faces_available = range(32)

        # map the number of sides on each face
        self.faces_sides = [6, 5, 6, 5, 6, 5, 6, 6, 6, 5, 6, 6, 5, 6, 6, 5, 6, 5, 6, 6, 5, 6, 6, 5, 6, 5, 6, 5, 6, 5, 6, 6]
        self.pentagons = [1, 3, 5, 9, 12, 15, 17, 20, 23, 25, 27, 29]

        # map the adjacent sides
        self.faces_adj = [[1, 2, 3, 4, 5, 6], [0, 2, 6, 7, 8], [0, 1, 3, 8, 9, 10], [0, 2, 4, 10, 11], [0, 3, 5, 11, 12, 13], [0, 4, 6, 13, 14], [0, 1, 5, 7, 14, 15], [1, 6, 8, 15, 16, 17], [1, 2, 7, 9, 17, 18], [2, 8, 10, 18, 19], [2, 3, 9, 11, 19, 20], [3, 4, 10, 12, 20, 21], [4, 11, 13, 21, 22], [4, 5, 12, 14, 22, 23], [5, 6, 13, 15, 23, 24], [6, 7, 14, 16, 24], [7, 15, 17, 24, 25, 26], [7, 8, 16, 18, 26], [8, 9, 17, 19, 26, 27], [9, 10, 18, 20, 27, 28], [10, 11, 19, 21, 28], [11, 12, 20, 22, 28, 29], [12, 13, 21, 23, 29, 30], [13, 14, 22, 24, 30], [14, 15, 16, 23, 25, 30], [16, 24, 26, 30, 31], [16, 17, 18, 25, 27, 31], [18, 19, 26, 28, 31], [19, 20, 21, 27, 29, 31], [21, 22, 28, 30, 31], [22, 23, 24, 25, 29, 31], [25, 26, 27, 28, 29, 30]]

        self.faces_dist = {0: {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 2, 8: 2, 9: 2, 10: 2, 11: 2, 12: 2, 13: 2, 14: 2, 15: 2, 16: 3, 17: 3, 18: 3, 19: 3, 20: 3, 21: 3, 22: 3, 23: 3, 24: 3, 25: 4, 26: 4, 27: 4, 28: 4, 29: 4, 30: 4, 31: 5}, 1: {0: 1, 1: 0, 2: 1, 3: 2, 4: 2, 5: 2, 6: 1, 7: 1, 8: 1, 9: 2, 10: 2, 11: 3, 12: 3, 13: 3, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2, 19: 3, 20: 3, 21: 4, 22: 4, 23: 3, 24: 3, 25: 3, 26: 3, 27: 3, 28: 4, 29: 5, 30: 4, 31: 4}, 2: {0: 1, 1: 1, 2: 0, 3: 1, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 1, 10: 1, 11: 2, 12: 3, 13: 3, 14: 3, 15: 3, 16: 3, 17: 2, 18: 2, 19: 2, 20: 2, 21: 3, 22: 4, 23: 4, 24: 4, 25: 4, 26: 3, 27: 3, 28: 3, 29: 4, 30: 5, 31: 4}, 3: {0: 1, 1: 2, 2: 1, 3: 0, 4: 1, 5: 2, 6: 2, 7: 3, 8: 2, 9: 2, 10: 1, 11: 1, 12: 2, 13: 2, 14: 3, 15: 3, 16: 4, 17: 3, 18: 3, 19: 2, 20: 2, 21: 2, 22: 3, 23: 3, 24: 4, 25: 5, 26: 4, 27: 3, 28: 3, 29: 3, 30: 4, 31: 4}, 4: {0: 1, 1: 2, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3, 8: 3, 9: 3, 10: 2, 11: 1, 12: 1, 13: 1, 14: 2, 15: 3, 16: 4, 17: 4, 18: 4, 19: 3, 20: 2, 21: 2, 22: 2, 23: 2, 24: 3, 25: 4, 26: 5, 27: 4, 28: 3, 29: 3, 30: 3, 31: 4}, 5: {0: 1, 1: 2, 2: 2, 3: 2, 4: 1, 5: 0, 6: 1, 7: 2, 8: 3, 9: 3, 10: 3, 11: 2, 12: 2, 13: 1, 14: 1, 15: 2, 16: 3, 17: 3, 18: 4, 19: 4, 20: 3, 21: 3, 22: 2, 23: 2, 24: 2, 25: 3, 26: 4, 27: 5, 28: 4, 29: 3, 30: 3, 31: 4}, 6: {0: 1, 1: 1, 2: 2, 3: 2, 4: 2, 5: 1, 6: 0, 7: 1, 8: 2, 9: 3, 10: 3, 11: 3, 12: 3, 13: 2, 14: 1, 15: 1, 16: 2, 17: 2, 18: 3, 19: 4, 20: 4, 21: 4, 22: 3, 23: 2, 24: 2, 25: 3, 26: 3, 27: 4, 28: 5, 29: 4, 30: 3, 31: 4}, 7: {0: 2, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 1, 9: 2, 10: 3, 11: 4, 12: 4, 13: 3, 14: 2, 15: 1, 16: 1, 17: 1, 18: 2, 19: 3, 20: 4, 21: 5, 22: 4, 23: 3, 24: 2, 25: 2, 26: 2, 27: 3, 28: 4, 29: 4, 30: 3, 31: 3}, 8: {0: 2, 1: 1, 2: 1, 3: 2, 4: 3, 5: 3, 6: 2, 7: 1, 8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 4, 14: 3, 15: 2, 16: 2, 17: 1, 18: 1, 19: 2, 20: 3, 21: 4, 22: 5, 23: 4, 24: 3, 25: 3, 26: 2, 27: 2, 28: 3, 29: 4, 30: 4, 31: 3}, 9: {0: 2, 1: 2, 2: 1, 3: 2, 4: 3, 5: 3, 6: 3, 7: 2, 8: 1, 9: 0, 10: 1, 11: 2, 12: 3, 13: 4, 14: 4, 15: 3, 16: 3, 17: 2, 18: 1, 19: 1, 20: 2, 21: 3, 22: 4, 23: 5, 24: 4, 25: 3, 26: 2, 27: 2, 28: 2, 29: 3, 30: 4, 31: 3}, 10: {0: 2, 1: 2, 2: 1, 3: 1, 4: 2, 5: 3, 6: 3, 7: 3, 8: 2, 9: 1, 10: 0, 11: 1, 12: 2, 13: 3, 14: 4, 15: 4, 16: 4, 17: 3, 18: 2, 19: 1, 20: 1, 21: 2, 22: 3, 23: 4, 24: 5, 25: 4, 26: 3, 27: 2, 28: 2, 29: 3, 30: 4, 31: 3}, 11: {0: 2, 1: 3, 2: 2, 3: 1, 4: 1, 5: 2, 6: 3, 7: 4, 8: 3, 9: 2, 10: 1, 11: 0, 12: 1, 13: 2, 14: 3, 15: 4, 16: 5, 17: 4, 18: 3, 19: 2, 20: 1, 21: 1, 22: 2, 23: 3, 24: 4, 25: 4, 26: 4, 27: 3, 28: 2, 29: 2, 30: 3, 31: 3}, 12: {0: 2, 1: 3, 2: 3, 3: 2, 4: 1, 5: 2, 6: 3, 7: 4, 8: 4, 9: 3, 10: 2, 11: 1, 12: 0, 13: 1, 14: 2, 15: 3, 16: 4, 17: 5, 18: 4, 19: 3, 20: 2, 21: 1, 22: 1, 23: 2, 24: 3, 25: 3, 26: 4, 27: 3, 28: 2, 29: 2, 30: 2, 31: 3}, 13: {0: 2, 1: 3, 2: 3, 3: 2, 4: 1, 5: 1, 6: 2, 7: 3, 8: 4, 9: 4, 10: 3, 11: 2, 12: 1, 13: 0, 14: 1, 15: 2, 16: 3, 17: 4, 18: 5, 19: 4, 20: 3, 21: 2, 22: 1, 23: 1, 24: 2, 25: 3, 26: 4, 27: 4, 28: 3, 29: 2, 30: 2, 31: 3}, 14: {0: 2, 1: 2, 2: 3, 3: 3, 4: 2, 5: 1, 6: 1, 7: 2, 8: 3, 9: 4, 10: 4, 11: 3, 12: 2, 13: 1, 14: 0, 15: 1, 16: 2, 17: 3, 18: 4, 19: 5, 20: 4, 21: 3, 22: 2, 23: 1, 24: 1, 25: 2, 26: 3, 27: 4, 28: 4, 29: 3, 30: 2, 31: 3}, 15: {0: 2, 1: 2, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 1, 8: 2, 9: 3, 10: 4, 11: 4, 12: 3, 13: 2, 14: 1, 15: 0, 16: 1, 17: 2, 18: 3, 19: 4, 20: 5, 21: 4, 22: 3, 23: 2, 24: 1, 25: 2, 26: 2, 27: 3, 28: 4, 29: 3, 30: 2, 31: 3}, 16: {0: 3, 1: 2, 2: 3, 3: 4, 4: 4, 5: 3, 6: 2, 7: 1, 8: 2, 9: 3, 10: 4, 11: 5, 12: 4, 13: 3, 14: 2, 15: 1, 16: 0, 17: 1, 18: 2, 19: 3, 20: 4, 21: 4, 22: 3, 23: 2, 24: 1, 25: 1, 26: 1, 27: 2, 28: 3, 29: 3, 30: 2, 31: 2}, 17: {0: 3, 1: 2, 2: 2, 3: 3, 4: 4, 5: 3, 6: 2, 7: 1, 8: 1, 9: 2, 10: 3, 11: 4, 12: 5, 13: 4, 14: 3, 15: 2, 16: 1, 17: 0, 18: 1, 19: 2, 20: 3, 21: 4, 22: 4, 23: 3, 24: 2, 25: 2, 26: 1, 27: 2, 28: 3, 29: 3, 30: 3, 31: 2}, 18: {0: 3, 1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 3, 7: 2, 8: 1, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 4, 15: 3, 16: 2, 17: 1, 18: 0, 19: 1, 20: 2, 21: 3, 22: 4, 23: 4, 24: 3, 25: 2, 26: 1, 27: 1, 28: 2, 29: 3, 30: 3, 31: 2}, 19: {0: 3, 1: 3, 2: 2, 3: 2, 4: 3, 5: 4, 6: 4, 7: 3, 8: 2, 9: 1, 10: 1, 11: 2, 12: 3, 13: 4, 14: 5, 15: 4, 16: 3, 17: 2, 18: 1, 19: 0, 20: 1, 21: 2, 22: 3, 23: 4, 24: 4, 25: 3, 26: 2, 27: 1, 28: 1, 29: 2, 30: 3, 31: 2}, 20: {0: 3, 1: 3, 2: 2, 3: 2, 4: 2, 5: 3, 6: 4, 7: 4, 8: 3, 9: 2, 10: 1, 11: 1, 12: 2, 13: 3, 14: 4, 15: 5, 16: 4, 17: 3, 18: 2, 19: 1, 20: 0, 21: 1, 22: 2, 23: 3, 24: 4, 25: 3, 26: 3, 27: 2, 28: 1, 29: 2, 30: 3, 31: 2}, 21: {0: 3, 1: 4, 2: 3, 3: 2, 4: 2, 5: 3, 6: 4, 7: 5, 8: 4, 9: 3, 10: 2, 11: 1, 12: 1, 13: 2, 14: 3, 15: 4, 16: 4, 17: 4, 18: 3, 19: 2, 20: 1, 21: 0, 22: 1, 23: 2, 24: 3, 25: 3, 26: 3, 27: 2, 28: 1, 29: 1, 30: 2, 31: 2}, 22: {0: 3, 1: 4, 2: 4, 3: 3, 4: 2, 5: 2, 6: 3, 7: 4, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1, 13: 1, 14: 2, 15: 3, 16: 3, 17: 4, 18: 4, 19: 3, 20: 2, 21: 1, 22: 0, 23: 1, 24: 2, 25: 2, 26: 3, 27: 3, 28: 2, 29: 1, 30: 1, 31: 2}, 23: {0: 3, 1: 3, 2: 4, 3: 3, 4: 2, 5: 2, 6: 2, 7: 3, 8: 4, 9: 5, 10: 4, 11: 3, 12: 2, 13: 1, 14: 1, 15: 2, 16: 2, 17: 3, 18: 4, 19: 4, 20: 3, 21: 2, 22: 1, 23: 0, 24: 1, 25: 2, 26: 3, 27: 3, 28: 3, 29: 2, 30: 1, 31: 2}, 24: {0: 3, 1: 3, 2: 4, 3: 4, 4: 3, 5: 2, 6: 2, 7: 2, 8: 3, 9: 4, 10: 5, 11: 4, 12: 3, 13: 2, 14: 1, 15: 1, 16: 1, 17: 2, 18: 3, 19: 4, 20: 4, 21: 3, 22: 2, 23: 1, 24: 0, 25: 1, 26: 2, 27: 3, 28: 3, 29: 2, 30: 1, 31: 2}, 25: {0: 4, 1: 3, 2: 4, 3: 5, 4: 4, 5: 3, 6: 3, 7: 2, 8: 3, 9: 3, 10: 4, 11: 4, 12: 3, 13: 3, 14: 2, 15: 2, 16: 1, 17: 2, 18: 2, 19: 3, 20: 3, 21: 3, 22: 2, 23: 2, 24: 1, 25: 0, 26: 1, 27: 2, 28: 2, 29: 2, 30: 1, 31: 1}, 26: {0: 4, 1: 3, 2: 3, 3: 4, 4: 5, 5: 4, 6: 3, 7: 2, 8: 2, 9: 2, 10: 3, 11: 4, 12: 4, 13: 4, 14: 3, 15: 2, 16: 1, 17: 1, 18: 1, 19: 2, 20: 3, 21: 3, 22: 3, 23: 3, 24: 2, 25: 1, 26: 0, 27: 1, 28: 2, 29: 2, 30: 2, 31: 1}, 27: {0: 4, 1: 3, 2: 3, 3: 3, 4: 4, 5: 5, 6: 4, 7: 3, 8: 2, 9: 2, 10: 2, 11: 3, 12: 3, 13: 4, 14: 4, 15: 3, 16: 2, 17: 2, 18: 1, 19: 1, 20: 2, 21: 2, 22: 3, 23: 3, 24: 3, 25: 2, 26: 1, 27: 0, 28: 1, 29: 2, 30: 2, 31: 1}, 28: {0: 4, 1: 4, 2: 3, 3: 3, 4: 3, 5: 4, 6: 5, 7: 4, 8: 3, 9: 2, 10: 2, 11: 2, 12: 2, 13: 3, 14: 4, 15: 4, 16: 3, 17: 3, 18: 2, 19: 1, 20: 1, 21: 1, 22: 2, 23: 3, 24: 3, 25: 2, 26: 2, 27: 1, 28: 0, 29: 1, 30: 2, 31: 1}, 29: {0: 4, 1: 5, 2: 4, 3: 3, 4: 3, 5: 3, 6: 4, 7: 4, 8: 4, 9: 3, 10: 3, 11: 2, 12: 2, 13: 2, 14: 3, 15: 3, 16: 3, 17: 3, 18: 3, 19: 2, 20: 2, 21: 1, 22: 1, 23: 2, 24: 2, 25: 2, 26: 2, 27: 2, 28: 1, 29: 0, 30: 1, 31: 1}, 30: {0: 4, 1: 4, 2: 5, 3: 4, 4: 3, 5: 3, 6: 3, 7: 3, 8: 4, 9: 4, 10: 4, 11: 3, 12: 2, 13: 2, 14: 2, 15: 2, 16: 2, 17: 3, 18: 3, 19: 3, 20: 3, 21: 2, 22: 1, 23: 1, 24: 1, 25: 1, 26: 2, 27: 2, 28: 2, 29: 1, 30: 0, 31: 1}, 31: {0: 5, 1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 3, 8: 3, 9: 3, 10: 3, 11: 3, 12: 3, 13: 3, 14: 3, 15: 3, 16: 2, 17: 2, 18: 2, 19: 2, 20: 2, 21: 2, 22: 2, 23: 2, 24: 2, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 0}}

        #self.faces_dist = {a: {b: self.calculate_distance(a, b, None) for b in range(32)} for a in range(32)}

        self.bases = []

        # tests
        '''
        for face, dists in self.faces_dist.iteritems():
            counts = [0, 0, 0, 0, 0, 0]
            if self.faces_sides[face] == 6:
                compare = [1, 6, 9, 9, 6, 1]
            elif self.faces_sides[face] == 5:
                compare = [1, 5, 10, 10, 5, 1]
            else:
                raise ValueError('Got a face with number of sides {0}, not 5 or 6.'.format(self.faces_sides[face]))
            for otherface, dist in dists.iteritems():
                counts[dist] += 1
            assert counts == compare, 'Failed for face {0}, got {1}'.format(face, counts)
        self.invalidate_face(31)
        self.invalidate_face(27)
        self.invalidate_face(25)
        self.invalidate_face(18)
        self.invalidate_face(16)
        trials1 = [26, 17, 26, 19]
        trials2 = [29, 29, 27, 24]
        answers = [6, 5, 1, 4]
        for i in range(len(trials1)):
            assert self.calculate_distance(trials1[i], trials2[i], None) == answers[i], 'Improper distances calculated with invalidated faces. Wrong on {0} to {1}'.format(trials1[i], trials2[i])

        self.invalidate_face(17)
        assert self.calculate_distance(26, 0, None) == 999, 'Encircled face should have no path'

        self.revalidate_face(31)
        self.revalidate_face(27)
        self.revalidate_face(25)
        self.revalidate_face(18)
        self.revalidate_face(16)
        self.revalidate_face(17)
        '''

    def calculate_distance(self, a, b, avoid):
        '''
        Recursive function.
        Do a search, mark faces to avoid so that we don't go to
        infinite depth
        '''
        if a == b:
            return 0
        elif b in self.faces_adj[a]:
            return 1
        else:
            if avoid is None:
                avoid = set(self.faces_valid) - set(self.faces_available)
            else:
                avoid = copy.copy(avoid)
            #print('at {0} avoiding {1}'.format(a, avoid))
            faces_left = copy.copy(self.faces_adj[a])
            for face in set(avoid) & set(faces_left):
                faces_left.remove(face)
            if len(faces_left) == 0:
                return 999
            for face in faces_left:
                avoid.add(face)
            avoid.add(a)
            distances = [self.calculate_distance(face, b, avoid) for face in faces_left]
            return min(distances) + 1

    def _check_face_exists(self, face):
        '''
        Ensure the face number is valid given the shape of the map
        '''
        if face not in self.faces_valid:
            raise ValueError('Invalid face value {0}, must be in range [0, {1}]'.format(face, len(self.faces_valid)))

    def is_adjacent(self, face1, face2):
        return face1 in self.faces_adj[face2]

    def is_edge(self, face1, face2):
        self._check_face_exists(face1)
        self._check_face_exists(face2)
        return self.is_adjacent(face1, face2)

    def is_vertex(self, face1, face2, face3):
        self._check_face_exists(face1)
        self._check_face_exists(face2)
        self._check_face_exists(face3)
        return self.is_adjacent(face1, face2) and self.is_adjacent(face1, face3) and self.is_adjacent(face2, face3)

    def faces_within(self, face, dist):
        '''
        Return a list of all the faces within dist of the face
        '''
        dists = self.faces_dist[face]
        faces_within_distance = []
        for possible_face, face_dist in dists.iteritems():
            if face_dist <= dist:
                faces_within_distance.append(possible_face)
        return faces_within_distance

    def face_available(self, face):
        '''
        Return whether the face is in play
        '''
        self._check_face_exists(face)
        return face in self.faces_available

    def invalidate_face(self, face):
        '''
        Remove a face from play
        '''
        # throws ValueError if it fails
        self.faces_available.remove(face)

        self.faces_dist = {a: {b: self.calculate_distance(a, b, None) for b in range(32)} for a in range(32)}

    def revalidate_face(self, face):
        self.faces_available.append(face)

        self.faces_dist = {a: {b: self.calculate_distance(a, b, None) for b in range(32)} for a in range(32)}

    def place_base(self, min_distance=3):
        '''
        Place a base, at least 3 spaces away from any other bases if possible
        '''
        pentagons = copy.copy(self.pentagons)
        for base in self.bases:
            pentagons.remove(base)

        while len(pentagons) > 0:
            picked_pentagon = pentagons[random.randint(0, len(pentagons) - 1)]
            too_close = False
            for base in self.bases:
                if self.calculate_distance(picked_pentagon, base, None) < min_distance:
                    too_close = True
            if too_close:
                pentagons.remove(picked_pentagon)
            else:
                self.bases.append(picked_pentagon)
                return picked_pentagon

        raise RuntimeError('Tried to place base number {0} but failed! Bases already present at {1}'.format(len(self.bases) + 1, self.bases))
