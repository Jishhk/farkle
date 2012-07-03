import random, math

class Dice:
    '''Module to create a dice object with a given number of sides'''
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self, n=1):
        '''Returns n-length list of random ints
        with value from range one to self.sides'''
        return [int(math.floor(random.random() * 6) + 1) for _ in xrange(n)]