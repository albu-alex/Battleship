import pygame

pygame.init()

display_width = 1920
display_height = 1080

pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Welcome to Battleship!")


class MainMenu:
    """
    This class is the main menu before entering the actual battleship game
    This will be used for changing settings before entering the game(difficulty and such)
    """
    def __init__(self, settings):
        self.settings = settings

