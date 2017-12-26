import sys, pygame

pygame.init()

class GameMenu():
    def __init__(self,screen):
        
        # Button Setup
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height 

        self.clock = pygame.time.Clock()

        self.bg = pygame.image.load("images/bg.png")
        self.bgrect = self.bg.get_rect()

        self.title = pygame.image.load("images/title.png")
        self.titlerect = self.title.get_rect()
        self.titlex = self.scr_width/2 - self.titlerect.width/2
        self.titley = 50

        self.start_button = pygame.image.load("images/play_normal.png")
        self.start_hover_button = pygame.image.load("images/play_hover.png")
        self.start_buttonrect = self.start_button.get_rect()

        self.sposx = (self.scr_width / 2) - (self.start_buttonrect.width/2)    
        self.sposy = (self.scr_height / 2 - 100)
        self.sposxmax = self.sposx + self.start_buttonrect.width
        self.sposymax = self.sposy + (self.start_buttonrect.height)   

        self.options_button = pygame.image.load("images/options_normal.png")
        self.options_hover_button = pygame.image.load("images/options_hover.png")
        self.options_buttonrect = self.options_button.get_rect()

        self.oposx = (self.scr_width / 2) - (self.options_buttonrect.width/2)    
        self.oposy = (self.scr_height / 2) + 60
        self.oposxmax = self.oposx + self.options_buttonrect.width
        self.oposymax = self.oposy + (self.options_buttonrect.height)

        self.quit_button = pygame.image.load("images/quit_normal.png")
        self.quit_hover_button = pygame.image.load("images/quit_hover.png")
        self.quit_buttonrect = self.quit_button.get_rect()

        self.qposx = (self.scr_width / 2) - (self.quit_buttonrect.width/2)    
        self.qposy = (self.scr_height / 2) + (self.start_buttonrect.height + 30)
        self.qposxmax = self.qposx + self.quit_buttonrect.width
        self.qposymax = self.qposy + self.quit_buttonrect.height

        self.back_button = pygame.image.load("images/back_normal.png")
        self.back_hover_button = pygame.image.load("images/back_hovered.png")
        self.back_buttonrect = self.back_button.get_rect()

        self.bposx = 50    
        self.bposy = 50
        self.bposxmax = self.bposx + self.back_buttonrect.width
        self.bposymax = self.bposy + self.back_buttonrect.height  

        self.players_button = pygame.image.load("images/players.png")
        self.players_pressed_button = pygame.image.load("images/players_pressed.png")
        self.players_buttonrect = self.players_button.get_rect()

        self.pposx = (self.scr_width /2) - (2 * self.players_buttonrect.width)    
        self.pposy = (self.scr_height /2)
        self.pposxmax = self.pposx + self.players_buttonrect.width
        self.pposymax = self.pposy + self.players_buttonrect.height                          