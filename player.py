import sys, pygame

pygame.init()

class Player():
    def __init__(self):

        self.p1_points = 0
        self.p2_points = 0
        self.p3_points = 0
        self.p4_points = 0

        self.player_turn = 1

        self.player_number = 3

