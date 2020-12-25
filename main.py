#
# A Connect Four Board class and Rules of Game
#


class Board:
    """ a data type for a Connect Four board with arbitrary dimensions """   

    def __init__(self,height,width):
        """ This function initializes the Board class by establishing the 
                dimensions of the Connect Four board based on user's input.
            input:  height, an integer for the num of rows for the board
                    width, an integer for the num of columns for the board
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string that represents a Board object. """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row
        for newcol in range((self.width*2)+1):
            s+= '-'
        s += '\n'       # breaks into new line
        for i in range(self.width):
            if i >= 10:
                i %= 10
                s+=  " " + str(i) 
            else:
                s+=  " " + str(i) 
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(col >= 0 and col < self.width)
        if "O" in checker:
            for r in range(self.height):
                if self.slots[r][col] != " ":
                    self.slots[r-1][col] = "O"
                    break
                else:
                    if r == self.height-1:
                        if self.slots[r][col] == " ":
                            self.slots[r][col] = "O"
                            break
        elif "X" in checker:
            for r in range(self.height):
                if self.slots[r][col] != " ":
                    self.slots[r-1][col] = "X"
                    break
                else:
                    if r == self.height-1:
                        if self.slots[r][col] == " ":
                            self.slots[r][col] = "X"
                            break
    
    def reset(self):
        """ This function takes in the given Board and resets it
                to an empty grid
        """
        self.slots = [[' '] * self.width for row in range(self.height)]
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
                checkers in those columns of the called Board object,
                starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'
        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self,col):
        """ This function takes in the given board and a col integer
                and returns a Boolean object determining if the 
                checker is allowed to move to the specified column.
            input: col, an integer
        """
        if 0 <= col < self.width:
            for r in range(self.height):
                if self.slots[r][col] == " ":
                    return True
            if self.slots[0][col] != " ":
                return False
        else:
            return False

    def is_full(self):
        """ This function takes in the given board and returns
                a Boolean object determining if the board is full
        """
        count = 0
        for c in range(self.width):
            if self.can_add_to(c) == False:
                count += 1
        if count == self.width:
            return True
        return False

    def remove_checker(self,col):
        """ This function takes in the given board and a col integer
                and removes the top most checker in the given col integer
                from the board.
            input: col, an integer
        """
        assert(0<= col < self.width)
        for r in range(self.height):
            if self.slots[r][col] != " ":
                self.slots[r][col] = " "
                break
    
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
                Returns a Boolean object after determining 
                whether or not there is a vertical win for the specified checker.
            input: checker, a string of 'X' or 'O' 
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                self.slots[row][col + 1] == checker and \
                self.slots[row][col + 2] == checker and \
                self.slots[row][col + 3] == checker:
                    return True
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
                Returns a Boolean object after determining 
                whether or not there is a vertical win for the specified checker.
            input: checker, a string of 'X' or 'O'
        """
        for col in range(self.width):
            for row in range(self.height-3):
                if self.slots[row][col] == checker and \
                    self.slots[row+1][col] == checker and \
                    self.slots[row+2][col] == checker and \
                    self.slots[row+3][col] == checker:
                        return True
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a down diagonal win for the specified checker.
                If condition is met for down diagonal win, the
                function will output True - and False otherwise.
            input: checker, a string of 'X' or 'O'
        """
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                    self.slots[row+1][col+1] == checker and \
                    self.slots[row+2][col+2] == checker and \
                    self.slots[row+3][col+3] == checker:
                        return True
        return False

    def is_up_diagonal_win(self, checker):
        """ Checks for a up diagonal win for the specified checker.
                If condition is met for up diagonal win, the
                function will output True - and False otherwise.
            input: checker, a string of 'X' or 'O'
        """
        for col in range(self.width-3):
            for row in range(3, self.height):
                if self.slots[row][col] == checker and \
                    self.slots[row-1][col+1] == checker and \
                    self.slots[row-2][col+2] == checker and \
                    self.slots[row-3][col+3] == checker:
                        return True
        return False

    def is_win_for(self,checker):
        """ This function takes in the given board and a checker as a parameter,
                and returns a Boolean object after determining if the 
                specified checker has won the Connect Four game.
            input: checker, a string of 'X' or 'O'
        """
        if self.is_horizontal_win(checker) == True or \
            self.is_down_diagonal_win(checker) == True or \
            self.is_vertical_win(checker) == True or \
            self.is_up_diagonal_win(checker) == True:
                return True
        return False

Board(4,5)