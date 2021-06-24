"""
Domain module
"""
from texttable import Texttable


class GameError(Exception):
    """
    Custom exception class which inherits from standard Exception class
    """
    def __init__(self, message):
        self._message = message


class GameBoard:
    """
    Here I will define the board needed for the game
    """
    def __init__(self, rows=8, columns=8):
        """
        Here I will initialise a board needed for the game
        """
        self._rows = rows
        self._columns = columns
        self._board = [[0 for column in range(self._columns + 2)] for row in range(self._rows + 2)]

    def show_move(self, row, column):
        """
        :param row: The row on the board on which the move was made
        :param column: The column on the board on which the move was made
        :return: True if there was a hit, False otherwise
        :exception: GameError when that move was already made
        """
        if row < 0 or row > self._rows or column < 0 or column > self._columns:
            return

        if self._board[row][column] == 0:
            self._board[row][column] = 'O'
            return False

        elif self._board[row][column] == 1:
            self._board[row][column] = 'X'
            return True

        else:
            raise GameError("You have already selected this move!")

    def place_battleship(self, first_coordinate, second_coordinate, orientation, length):
        """
        :param first_coordinate: The first coordinate of a move(either a digit or a letter)
        :param second_coordinate: The second coordinate of a move(either a letter or a digit)
        :param orientation: The orientation in which the boat will be placed(one of up, down, left or right)
        :param length: The length of the boat that will be placed(from 2 to 5)
        :return: -
        :exception: GameError when move is out of bounds
        """
        if orientation == "up":
            if first_coordinate < length or first_coordinate < 0 or first_coordinate > self._rows:
                raise GameError("Impossible move!")
            else:
                for column in range(1, self._columns+1):
                    for row in range(first_coordinate, 0, -1):
                        if length > 0 and column == second_coordinate:
                            self._board[row][column] = 1
                            length -= 1
        elif orientation == "down":
            if first_coordinate > self._rows - length + 1 or first_coordinate < 0 or first_coordinate > self._rows:
                raise GameError("Impossible move!")
            else:
                for column in range(1, self._columns+1):
                    for row in range(first_coordinate, self._rows+1):
                        if length > 0 and column == second_coordinate:
                            self._board[row][column] = 1
                            length -= 1
        elif orientation == "left":
            if second_coordinate < length or second_coordinate < 0 or second_coordinate > self._columns:
                raise GameError("Impossible move!")
            else:
                for row in range(1, self._rows+1):
                    for column in range(second_coordinate, 0, -1):
                        if length > 0 and row == first_coordinate:
                            self._board[row][column] = 1
                            length -= 1
        elif orientation == "right":
            if second_coordinate > self._columns - length + 1 or second_coordinate < 0 or second_coordinate > self._columns:
                raise GameError("Impossible move!")
            else:
                for row in range(1, self._rows+1):
                    for column in range(second_coordinate, self._columns+1):
                        if length > 0 and row == first_coordinate:
                            self._board[row][column] = 1
                            length -= 1

    def __str__(self):
        table = Texttable()
        # Build table header
        header = [' ']
        for h in range(self._columns):
            header.append(chr(65 + h))
        table.header(header)

        # Add each table row
        for row in range(1, self._rows + 1):
            data = []

            for val in self._board[row][1:-1]:
                if val == 'O':
                    data.append('O')
                elif val == 'X':
                    data.append('X')
                else:
                    data.append(str(val))
            table.add_row([row] + data)
        return table.draw()

"""
o = GameBoard()
o.show_move(3, 3)
print(str(o))
"""