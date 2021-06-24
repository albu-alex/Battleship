"""
UI module
"""
import time
from domain.entity import GameError


class UI:
    def __init__(self, services):
        self._services = services

    def player1_input_ui(self, length):
        print("Please enter put your ships on the board!")
        if length > 1:
            self.print_board1_ui()
            first_coordinate = input("Enter your first coordinate(1-8 or A-H): ")
            second_coordinate = input("Enter your second coordinate(A-H or 1-8): ")
            orientation = input("Enter the orientation of the ship(UP, DOWN, LEFT, RIGHT): ")
            orientation = orientation.lower()
            try:
                self._services.player1_input(first_coordinate, second_coordinate, orientation, length)
            except GameError as error_message:
                print(str(error_message) + " Try again!")
                length += 1
            self.player1_input_ui(length-1)
        else:
            return

    def player2_input_ui(self, length):
        print("Please enter put your ships on the board!")
        if length > 1:
            self.print_board2_ui()
            first_coordinate = input("Enter your first coordinate(1-8 or A-H): ")
            second_coordinate = input("Enter your second coordinate(A-H or 1-8): ")
            orientation = input("Enter the orientation of the ship(UP, DOWN, LEFT, RIGHT): ")
            orientation = orientation.lower()
            try:
                self._services.player2_input(first_coordinate, second_coordinate, orientation, length)
            except GameError as error_message:
                print(str(error_message) + " Try again!")
                length += 1
            self.player2_input_ui(length-1)
        else:
            return

    def ai_input_ui(self, length):
        print("Now it's my turn!")
        self._services.ai_input(length)

    def player_move_ui(self, counter):
        first_coordinate = input("Enter your first coordinate(1-8 or A-H): ")
        second_coordinate = input("Enter your second coordinate(A-H or 1-8): ")
        if counter % 2 == 1:
            try:
                self._services.player1_move(first_coordinate, second_coordinate)
            except GameError as error_message:
                print(str(error_message) + " Try again!")
                self.player_move_ui(counter)
        else:
            try:
                self._services.player2_move(first_coordinate, second_coordinate)
            except GameError as error_message:
                print(str(error_message) + " Try again!")
                self.player_move_ui(counter)

    def ai_move_ui(self, ai_moves):
        values = self._services.ai_move(ai_moves)
        ai_moves.append(values)

    def multiplayer_start_ui(self):
        player1, player2 = self.players_name_multiplayer()
        self.player1_input_ui(5)
        self.print_board1_ui()
        self.player2_input_ui(5)
        self.print_board2_ui()
        counter = 1
        while True:
            self.player_turn_ui(counter, player1, player2)
            self.player_move_ui(counter)
            if self._services.is_game_done():
                self.winner_is_ui(counter, player1, player2)
                break
            if counter % 2 == 1:
                self.print_board2_for_player1_ui()
            else:
                self.print_board1_for_player2_ui()
            counter += 1
        print(player1)
        self.print_board1_ui()
        print(player2)
        self.print_board2_ui()

    def singleplayer_start_ui(self):
        player1, player2 = self.players_name_singleplayer()
        self.player1_input_ui(5)
        self.print_board1_ui()
        self.ai_input_ui(5)
        counter = 1
        ai_moves = []
        while True:
            self.player_turn_ui(counter, player1, player2)
            if self._services.is_game_done():
                self.winner_is_ui(counter, player1, player2)
                break
            if counter % 2 == 1:
                self.player_move_ui(counter)
                self.print_board2_for_player1_ui()
            else:
                self.ai_move_ui(ai_moves)
                self.print_board1_for_player2_ui()
            counter += 1
        print(player1)
        self.print_board1_ui()
        print(player2)
        self.print_board2_ui()

    def game_choice_ui(self):
        print("1. Multiplayer")
        print("2. Singleplayer")
        choice = input("Choose one of either multi or single player: ")
        if choice == "1" or choice.lower() == "multiplayer":
            self.multiplayer_start_ui()
        elif choice == "2" or choice.lower() == "singleplayer":
            self.singleplayer_start_ui()
        else:
            raise GameError("Please choose one of the above options!")

    def start(self):
        print("Welcome to Battleship!")
        self.game_choice_ui()
        game_continues = input("Do you want to play anymore?(YES/NO): ")
        game_continues = game_continues.lower()
        if game_continues == "no":
            print("Goodbye! You should play again soon ;)")
        else:
            self._services.clear_board()
            self.start()

    def winner_is_ui(self, counter, player1, player2):
        winner = self._services.turn(counter, player1, player2)
        if winner == "Commander von Picklestrauss":
            print("I have defeated you, useless human!")
        else:
            print(winner, "you have won this game!\nCongratulations!")

    def print_board1_ui(self):
        board = self._services.print_board1()
        print(board)

    def print_board2_ui(self):
        board = self._services.print_board2()
        print(board)

    def print_board1_for_player2_ui(self):
        print(self._services.print_board1_for_player2())

    def print_board2_for_player1_ui(self):
        print(self._services.print_board2_for_player1())

    @staticmethod
    def players_name_multiplayer():
        player1 = input("Player 1, enter your name: ")
        player2 = input("Player 2, enter your name: ")
        if player1 is None or player1 == "" or player1 == " ":
            player1 = "Player 1"
        if player2 is None or player2 == "" or player2 == " ":
            player2 = "Player 2"
        return player1, player2

    def player_turn_ui(self, counter, player1, player2):
        player_in_turn = self._services.turn(counter, player1, player2)
        if player_in_turn != "Commander von Picklestrauss":
            print(player_in_turn, "you may make your move!")
        else:
            player_in_turn += ","
            print("I,", player_in_turn, "will sink all your battleships!")

    @staticmethod
    def players_name_singleplayer():
        player1 = input("Player 1, enter your name: ")
        if player1 is None or player1 == "" or player1 == " ":
            player1 = "Player 1"
        player2 = "Commander von Picklestrauss"
        useless_variable = input("Player 2, enter your name: ")
        time.sleep(1)
        print("You cannot pick my name! Who do you think you are?!")
        return player1, player2
