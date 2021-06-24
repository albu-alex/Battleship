"""
Here I will implement the functionalities needed for the game
"""
import random
from domain.entity import GameError
from texttable import Texttable


class Services:
    def __init__(self, repository, domain1, domain2):
        self._repository = repository
        self._entity1 = domain1
        self._entity2 = domain2

    def player1_move(self, first_coordinate, second_coordinate):
        """
        Takes the coordinates of the move of a player in string and gives them to _determine_move
        :param first_coordinate: The first coordinate of a move(either a digit or a letter)
        :param second_coordinate: The second coordinate of a move(either a letter or a digit)
        :return: -
        """
        row, column = self._determine_move(first_coordinate, second_coordinate)

        self._entity2.show_move(row, column)

    def player2_move(self, first_coordinate, second_coordinate):
        """
        Takes the coordinates of the move of a player in string and gives them to _determine_move
        :param first_coordinate: The first coordinate of a move(either a digit or a letter)
        :param second_coordinate: The second coordinate of a move(either a letter or a digit)
        :return: -
        """
        row, column = self._determine_move(first_coordinate, second_coordinate)

        self._entity1.show_move(row, column)

    @staticmethod
    def _determine_move(first_coordinate, second_coordinate):
        """
        Function translates the coordinates that the user gave in two integers(row and column) on the board
        :param first_coordinate: The first coordinate of a move(either a digit or a letter)
        :param second_coordinate: The second coordinate of a move(either a letter or a digit)
        :return: The row and column corresponding to user input
        :exception: GameError when both coordinates are either a digit or a letter
        """
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
        return row, column

    def _determine_input(self, first_coordinate, second_coordinate, orientation):
        """
        :param first_coordinate: The first coordinate of a move(either a digit or a letter)
        :param second_coordinate: The second coordinate of a move(either a letter or a digit)
        :param orientation: The orientation in which the boat will be placed(one of up, down, left or right)
        :return: The row and column corresponding to user input
        """
        directions = "updownleftright"
        if orientation in directions and len(orientation) > 0:
            row, column = self._determine_move(first_coordinate, second_coordinate)
        else:
            raise GameError("Direction input not valid!")

        return row, column

    def player1_input(self, first_coordinate, second_coordinate, orientation, length):
        """
        Function calls the place_battleship method from the entity of player 1
        :param first_coordinate: The first coordinate of a move(either a digit or a letter)
        :param second_coordinate: The second coordinate of a move(either a letter or a digit)
        :param orientation: The orientation in which the boat will be placed(one of up, down, left or right)
        :param length: The length of the boat that will be placed(from 2 to 5)
        :return: -
        """
        row, column = self._determine_input(first_coordinate, second_coordinate, orientation)

        self._entity1.place_battleship(row, column, orientation, length)

    def player2_input(self, first_coordinate, second_coordinate, orientation, length):
        """
        Function calls the place_battleship method from the entity of player 2
        :param first_coordinate: The first coordinate of a move(either a digit or a letter)
        :param second_coordinate: The second coordinate of a move(either a letter or a digit)
        :param orientation: The orientation in which the boat will be placed(one of up, down, left or right)
        :param length: The length of the boat that will be placed(from 2 to 5)
        :return: -
        """
        row, column = self._determine_input(first_coordinate, second_coordinate, orientation)

        self._entity2.place_battleship(row, column, orientation, length)

    def clear_board(self):
        """
        Function clears the boards for both players(sets all the values from the board to 0)
        :return: -
        """
        for row in range(1, self._entity1._rows+1):
            for column in range(1, self._entity1._columns+1):
                self._entity1._board[row][column] = 0

        for row in range(1, self._entity2._rows + 1):
            for column in range(1, self._entity2._columns + 1):
                self._entity2._board[row][column] = 0

    @staticmethod
    def turn(counter, player1, player2):
        """
        :param counter: An integer for which the parity will decide which player's turn it is
        :param player1: The name of the first player
        :param player2: The name of the second player
        :return: The name of the player that is in turn
        """
        if counter % 2 == 1:
            return player1
        else:
            return player2

    def is_game_done(self):
        """
        The game is done if all the values from both boards are equal to 0
        :return: True is the game is done, false otherwise
        """
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
        """
        :return: The Texttable(__str__) method from the entity of player 1
        """
        return self._entity1.__str__()

    def print_board2(self):
        """
        :return: The Texttable(__str__) method from the entity of player 1
        """
        return self._entity2.__str__()

    @staticmethod
    def _turn_board_into_matrix(entityBoard):
        """
        Function manipulates the data from a player's board such that the other player cannot see ship placement
        :param entityBoard: The board of a given player
        :return: the modified board
        """
        board = []
        for row in range(1, entityBoard + 1):
            new_row = []
            for column in range(1, entityBoard + 1):
                if entityBoard[row][column] == 1:
                    new_row.append(0)
                else:
                    new_row.append(entityBoard[row][column])
            board.append(new_row)
        return board

    def print_board1_for_player2(self):
        """
        :return: the user friendly visualisation of the board(in Texttable format)
        __str__ from entity cannot be directly returned in the function
        """
        board = self._turn_board_into_matrix(self._entity1._board)

        table = Texttable()
        for row in range(len(board)):
            table.add_row(board[row])
        return table.draw()

    def print_board2_for_player1(self):
        """
        :return: the user friendly visualisation of the board(in Texttable format)
        __str__ from entity cannot be directly returned in the function
        """
        board = self._turn_board_into_matrix(self._entity2._board)

        table = Texttable()
        for row in range(len(board)):
            table.add_row(board[row])
        return table.draw()


    "----------------------------------------------AI DECISION MAKING--------------------------------------------------"

    def ai_input(self, length):
        """
        Execution is stopped when the last ship placed has length 2
        :param length: Takes the standard length given from start function(by default, 5)
        :return: -
        """
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

    def ai_move(self, ai_moves):
        """
        Function takes the last move the AI did and goes through all it's neighbours until one of it's neighbours has
        the ship placed on it
        If there's no neighbours that contains a boat, a random move is made
        :param ai_moves: An array which stores the coordinates of all previous moves that the AI did
        :return: The coordinates of the move and the result of that move(Hit or no Hit)
        :var: result is true when there's a hit and false when there isn't a hit
        :exception: GameError when the random move is invalid
        """
        if len(ai_moves) <= 0:
            first_coordinate = random.randint(1, 8)
            second_coordinate = random.randint(1, 8)
            result = self._entity1.show_move(first_coordinate, second_coordinate)
            return first_coordinate, second_coordinate, result
        values = ai_moves[-1]
        former_first_coordinate = values[0]
        former_second_coordinate = values[1]
        former_result = values[2]
        if not former_result:
            first_coordinate = random.randint(1, 8)
            second_coordinate = random.randint(1, 8)
            try:
                result = self._entity1.show_move(first_coordinate, second_coordinate)
                return first_coordinate, second_coordinate, result
            except GameError:
                self.ai_move(ai_moves)
        if former_second_coordinate + 1 <= 8:
            second_coordinate = former_second_coordinate + 1
            result = self._entity1.show_move(former_first_coordinate, second_coordinate)
            if result:
                return former_first_coordinate, second_coordinate, result
        if former_second_coordinate - 1 >= 1:
            second_coordinate = former_second_coordinate - 1
            result = self._entity1.show_move(former_first_coordinate, second_coordinate)
            if result:
                return former_first_coordinate, second_coordinate, result
        if former_first_coordinate + 1 <= 8:
            first_coordinate = former_first_coordinate + 1
            result = self._entity1.show_move(first_coordinate, former_second_coordinate)
            if result:
                return first_coordinate, former_second_coordinate, result
        if former_first_coordinate - 1 >= 1:
            first_coordinate = former_first_coordinate - 1
            result = self._entity1.show_move(first_coordinate, former_second_coordinate)
            if result:
                return first_coordinate, former_second_coordinate, result
