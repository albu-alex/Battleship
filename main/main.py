"""
This module boots my game up
"""
from domain.entity import GameBoard
from repository.game_statistics import Repository
from service.services import Services
from ui.UI import UI

entity1 = GameBoard()
entity2 = GameBoard()
repository = Repository()
services = Services(repository, entity1, entity2)
ui = UI(services)
ui.start()
