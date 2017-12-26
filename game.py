import sys,pygame
from menu import *

pygame.init()

class Game():
    def __init__(self):

        self.player_number = 1

        self.bg = pygame.image.load("images/bg.png")
        self.bgrect = self.bg.get_rect()


    def game():

        menu = GameMenu()

        menu.screen.blit(menu.bg,menu.bgrect)
        pygame.display.flip()
        print('Igra krece')