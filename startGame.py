#
#
# Function to Start Playing the Game 
#   

#from Main Class - Rules of Game import Board
from playerClass import Player
from main import *
from aiPlayer import *
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

def process_move(p,b):
    """ This method function takes in a string "X" or "O",
            the given board, b, and asks the player to 
            select a column that they would like to move in.
            The function then processes those selections,
            updates the board, and ask the next player for its
            move. Once there is a winner or a tie, the
            function will end and congratulate the winner.
        inputs: p, a string "X" or "O"
                b, a string of the board
    """
    print(str(p),"'s turn")
    nextMove = p.next_move(b)
    b.add_checker(p.checker,nextMove)
    print()
    print(b)
    if b.is_win_for("X") == True:
        print("X wins in "+str(p.num_moves) + " moves")
        print('Congratulations!')
        return True
    elif b.is_win_for("O") == True:
        print("O wins in "+str(p.num_moves) + " moves" )
        print('Congratulations!')
        return True
    elif b.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False

class RandomPlayer(Player):
    """ a data type (subclass of Player class) for a Random Computer playing Connect Four"""
    def next_move(self,b):
        """ This method function takes the player "X" or "O"
                and the given board, and makes a random selection
                of where to place its next checker based on the 
                validity of the move.
            input: b, a string of the board
        """
        if b.is_full() == True:
            return -1
        else:
            choice = random.choice(range(b.width))
            if b.can_add_to(choice) == True:
                return choice
            else:
                while b.can_add_to(choice) == False:
                    choice = random.choice(range(b.width))
                return choice
    
    
    
    
    
    connect_four(Player("X"), AIPlayer("O", "LEFT", 2))
    
    
    
    
    
    
    
    
    
    
    