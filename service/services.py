"""
Here I will implement the functionalities needed for the game
"""
import random
from domain.entity import GameError


class Services:
    def __init__(self, repository, domain1, domain2):
        self._repository = repository
        self._entity1 = domain1
        self._entity2 = domain2

    def player1_move(self, first_coordinate, second_coordinate):
        letters = "abcdefghABCDEFGH"
        numbers = "12345678"
        if first_coordinate in letters and second_coordinate in numbers:
            if first_coordinate in "abcdefgh":
                first_coordinate = first_coordinate.upper()
            column = int(ord(first_coordinate) - 64)
            row = int(second_coordinate)
        elif first_coordinate in numbers and second_coordinate in letters:
            if second_coordinate in "abcdefgh":
                second_coordinate = second_coordinate.upper()
            column = int(ord(second_coordinate) - 64)
            row = int(first_coordinate)
        else:
            raise GameError("Invalid input! First and second coordinate cannot be both letters or numbers!")

        self._entity2.show_move(row, column)

    def player2_move(self, first_coordinate, second_coordinate):
        letters = "abcdefghABCDEFGH"
        numbers = "12345678"
        if first_coordinate in letters and second_coordinate in numbers:
            if first_coordinate in "abcdefgh":
                first_coordinate = first_coordinate.upper()
            column = int(ord(first_coordinate) - 64)
            row = int(second_coordinate)
        elif first_coordinate in numbers and second_coordinate in letters:
            if second_coordinate in "abcdefgh":
                second_coordinate = second_coordinate.upper()
            column = int(ord(second_coordinate) - 64)
            row = int(first_coordinate)
        else:
            raise GameError("Invalid input! First and second coordinate cannot be both letters or numbers!")

        self._entity1.show_move(row, column)

    def player1_input(self, first_coordinate, second_coordinate, orientation, length):
        letters = "abcdefghABCDEFGH"
        numbers = "12345678"
        directions = "updownleftright"
        if orientation in directions:
            if first_coordinate in letters and second_coordinate in numbers:
                if first_coordinate in "abcdefgh":
                    first_coordinate = first_coordinate.upper()
                column = int(ord(first_coordinate) - 64)
                row = int(second_coordinate)
            elif first_coordinate in numbers and second_coordinate in letters:
                if second_coordinate in "abcdefgh":
                    second_coordinate = second_coordinate.upper()
                column = int(ord(second_coordinate) - 64)
                row = int(first_coordinate)
            else:
                raise GameError("Invalid input! First and second coordinate cannot be both letters or numbers!")
        else:
            raise GameError("Direction input not valid!")

        self._entity1.place_battleship(row, column, orientation, length)

    def player2_input(self, first_coordinate, second_coordinate, orientation, length):
        letters = "abcdefghABCDEFGH"
        numbers = "12345678"
        directions = "updownleftright"
        if orientation in directions:
            if first_coordinate in letters and second_coordinate in numbers:
                if first_coordinate in "abcdefgh":
                    first_coordinate = first_coordinate.upper()
                column = int(ord(first_coordinate) - 64)
                row = int(second_coordinate)
            elif first_coordinate in numbers and second_coordinate in letters:
                if second_coordinate in "abcdefgh":
                    second_coordinate = second_coordinate.upper()
                column = int(ord(second_coordinate) - 64)
                row = int(first_coordinate)
            else:
                raise GameError("Invalid input! First and second coordinate cannot be both letters or numbers!")
        else:
            raise GameError("Direction input not valid!")

        self._entity2.place_battleship(row, column, orientation, length)

    def clear_board(self):
        for row in range(1, self._entity1._rows+1):
            for column in range(1, self._entity1._columns+1):
                self._entity1._board[row][column] = 0

        for row in range(1, self._entity2._rows + 1):
            for column in range(1, self._entity2._columns + 1):
                self._entity2._board[row][column] = 0

    @staticmethod
    def turn(counter, player1, player2):
        if counter % 2 == 1:
            return player1
        else:
            return player2

    def is_game_done(self):
        done = True
        for row in range(1, self._entity1._rows + 1):
            for column in range(1, self._entity1._columns + 1):
                if self._entity1._board[row][column] == 1:
                    done = False
        if done is False:
            for row in range(1, self._entity2._rows + 1):
                for column in range(1, self._entity2._columns + 1):
                    if self._entity2._board[row][column] == 1:
                        return False
            return True
        else:
            return True

    def print_board1(self):
        return self._entity1.__str__()

    def print_board2(self):
        return self._entity2.__str__()

    def print_board1_for_player2(self):
        board = []
        for row in range(1, self._entity1._rows + 1):
            new_row = []
            for column in range(1, self._entity1._columns + 1):
                if self._entity1._board[row][column] == 1:
                    new_row.append(0)
                else:
                    new_row.append(self._entity1._board[row][column])
            board.append(new_row)

        return board

    def print_board2_for_player1(self):
        board = []
        for row in range(1, self._entity2._rows + 1):
            new_row = []
            for column in range(1, self._entity2._columns + 1):
                if self._entity2._board[row][column] == 1:
                    new_row.append(0)
                else:
                    new_row.append(self._entity2._board[row][column])
            board.append(new_row)

        return board

    "----------------------------------------------AI DECISION MAKING--------------------------------------------------"

    def ai_input(self, length):
        directions = "up", "down", "left", "right"
        ai_moves = []
        while length > 1:
            first_coordinate = random.randint(1, 8)
            second_coordinate = random.randint(1, 8)
            orientation = random.choice(directions)
            # How to make ships not touch each other?
            move = [first_coordinate, second_coordinate, orientation, length]
            if move not in ai_moves:
                try:
                    self._entity2.place_battleship(first_coordinate, second_coordinate, orientation, length)
                except GameError:
                    length += 1
                ai_moves.append(move)
            length -= 1

    def ai_move(self):
        first_coordinate = random.randint(1, 8)
        second_coordinate = random.randint(1, 8)
        self._entity1.show_move(first_coordinate, second_coordinate)
