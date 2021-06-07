"""
Domain module
"""
from texttable import Texttable


class GameError(Exception):
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