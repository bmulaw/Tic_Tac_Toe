#
# AI Player for use in Connect Four  
#

import random  
from playerClass import *

class AIPlayer(Player):
    """ A data type that inherits from Player class and makes an AI Player"""
    def __init__(self,checker, tiebreak, lookahead):
        """ This constructor initializes the AIPlayer class by
                taking in the given checker, tiebreak move,
                and the lookahead int.
            input:  checker, a string of "X" or "O"
                    tiebreak, a string of "LEFT", "RIGHT", or "RANDOM"
                    lookahead, an positive int greater or equal to 0
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahed = lookahead
        
    def __repr__(self):
       """ This method takes in the Player, its tiebreak move, and its
                lookahead int, and returns a string summarizing it.
        """
       a = self.tiebreak
       b = self.lookahed
       c = self.checker
       d = "Player " + str(c) + " ("+ str(a) + ", "+ str(b) + ")"
       return d
        
    def max_score_column(self,scores):
        """ THis method takes in a list of integers, and
                returns the index of the maximum integer
                in the array, based on user's selection
                of the far right, far left, or a random
                index.
            input: scores, a list of integers
        """
        arrIndex = []
        maxScore = max(scores)
        for i in range(len(scores)):
            if scores[i] == maxScore:
                arrIndex += [i]
        if self.tiebreak == "LEFT":
            return arrIndex[0]
        elif self.tiebreak == "RIGHT":
            return arrIndex[-1]
        elif self.tiebreak == "RANDOM":
            return random.choice(arrIndex)
        
    def scores_for(self,b):
        """ This method takes in the given board and the
                values of a player, tiebreak move, and
                lookahead int. It then calculates the outcomes
                of a move based on its next move (and depending
                on its lookahed, alos its opponent's next moves),
                and stores it in a list.
            input: b, a string of the board
        """
        scores = [-1] * len(range(b.width))
        c = self.checker
        d = self.opponent_checker()
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(c) == True:
                scores[col] = 100
            elif b.is_win_for(d) == True:
                scores[col] = 0
            elif self.lookahed == 0:
                scores[col] = 50
            else:
                b.add_checker(c, col)
                OppP = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahed -1)
                OppSc = OppP.scores_for(b)
                if max(OppSc) == 0:
                    scores[col] = 100
                elif max(OppSc) == 100:
                    scores[col] = 0
                elif max(OppSc) == 50:
                    scores[col] = 50
                b.remove_checker(col)
        return scores

    def next_move(self, b):
        """ This method allows the AI to make its next
                move by using the other methods in 
                this class. It bases its column decision
                based on the maximum score from the
                list built in scores_for method.
            input: b, a string of the board
        """
        self.num_moves += 1
        scores = self.scores_for(b)
        maxScoreIndex = self.max_score_column(scores)
        return maxScoreIndex



