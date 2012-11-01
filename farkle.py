import re, random

from dice import Dice

class Farkle:
    '''A dice game in which players attempt to reach 10,000 in score
    by rolling six 6-sided die.  Points are scored by rolling ones, fives,
    sets of three or more (in single roll), a full straight (in single roll),
    or three pairs (in single roll).  Full rules can be found at
    http://en.wikipedia.org/wiki/Farkle'''

    def __init__(self):
        print "Welcome to Farkle, also known as 10,000!"
        self.players = [] #initialize list of players
        self.num_players = int(raw_input("How many players? "))  #initialize number of players
        for i in xrange(self.num_players):
            #get name of player
            player = raw_input("Name of Player {0}: ".format(i+1))
            self.players.append(player) #append player to list of players

        #initialize scores, scores['_highest'][0] will hold the highest score
        self.scores = {'_highest':[0, '']}
        for player in self.players: #set each player's score to 0 in a dict
            self.scores[player] = 0

        self.round_count = 0 #initialize round counter
        self.dice = Dice()

    def Start(self):
        print "The game has %s players. Their names are:" % self.num_players
        self.player_scores()
        raw_input("Press enter if you are ready to begin!")

        while self.scores['_highest'][0] < 10000:
            self.Round()

        self.Finish()

    def Finish(self):
        print "Congratulations, {0}! You are the winner with a score of {1}.".format(self.scores['_highest'][1], self.scores['_highest'][0])
        print
        print "The total scores were:"
        self.player_scores()
        print

    def Round(self):
        self.round_count += 1
        print; print "="*18
        print " Starting round {0}".format(self.round_count)
        print "="*18; print
        if self.round_count > 1:
            print "{0} is currently in the lead with {1} points.".format(self.scores['_highest'][1], self.scores['_highest'][0]); print
            print "The total scores are:"
            self.player_scores(); print

        for player in self.players:
            self.Turn(player)
        print; raw_input("Press ENTER when you are ready to proceed to the next round")
        return

    def Turn(self, player):
        raw_input("{0}, it's your turn. Press enter when you are ready to roll.".format(player))

        score = random.randint(600, 2000)

        print "  You scored {0}".format(score)
        self.scores[player] += score

        print "  Your score is now: {0}".format(self.scores[player]); print

        if self.scores[player] > self.scores['_highest'][0]:
            self.scores['_highest'][0] = self.scores[player]
            self.scores['_highest'][1] = player
        return

    def player_scores(self):
        for player in self.players:
            print player + "; Score: " + str(self.scores[player])


if __name__ == '__main__':
    play = True
    while play:
        f = Farkle()
        f.Start()
        again = raw_input("Would you like to play again? ")
        while True:
            if again.upper() in ['Y', 'YE', 'YES']:
                break
            elif again.upper() in ['N', 'NO']:
                play = False
                break
            else:
                "Please enter yes or no"

