#
# A Connect-Four Player class 
from main import Board


class Player:
    """ a data type (subclass of Board) for a Player in  Connect Four """ 
    def __init__(self,checker):
        """ This function initializes the Player class by establishing the 
                which checker the player will be.
            input: checker, a string of 'X' or 'O' 
        """
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """ This function takes the given value of 
                the Player's checker ('X' or 'O') and 
                returns what that player's checker is
        """
        if self.checker == "X":
            playerX = "Player X"
            return playerX
        if self.checker == "O":
            playerO = "Player O"
            return playerO
    
    def opponent_checker(self):
        """ This function takes in the Player's checker
                and returns the string of it's Opponenet's 
                checker (i.e. if Player is 'X', opponent's 
                         checker is 'O', and vice versa)
        """
        if self.checker == "X":
            return "O"
        elif self.checker == "O":
            return "X"
    
    def next_move(self, b):
        """ This function takes in the Player and the Board
                of which the Player is playing in. It then 
                asks the user to input a column number that 
                it would like to move in, and if that column
                is an invalid spot, the function will continuously
                ask the Player to choose a different column.
                Once the Players inputs a valid column,
                the function will return that column number.
            input: b, Board object of a specific height and width.
        """
        colMove = int(input("Enter a column: "))
        checkMove = b.can_add_to(colMove)
        while checkMove == False:
            print('Try again!')
            colMove = int(input("Enter a column: "))
            checkMove = b.can_add_to(colMove)
        self.num_moves+= 1
        return colMove
    
    
    
    
    
    
    