# Import of needed python modules
import sys, os
import pygame

# Import of class files used in this game
from menu import *
from player import *
from random import *


# Initialization of pygame modules
pygame.init()

# Global variables section
SIZE = width, height = 1366, 768
FS = pygame.FULLSCREEN
screentype = 'Menu'
font1 = pygame.font.Font('fonts/cartoon.ttf',20)
board_size = 4

choice = [0,0]

cards = []
card_types = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7]

card_bg = pygame.image.load('images/back.png')
card_bgrect = card_bg.get_rect()

card_bghover = pygame.image.load('images/back_hover.png')
card_bghoverrect = card_bghover.get_rect()

card_images = [pygame.image.load('images/backpack.png'),\
                pygame.image.load('images/belt.png'),\
                pygame.image.load('images/bomb.png'),\
                pygame.image.load('images/book.png'),\
                pygame.image.load('images/bronze_coin.png'),\
                pygame.image.load('images/clover.png'),\
                pygame.image.load('images/feather.png'),\
                pygame.image.load('images/ring.png')]

animation = [pygame.image.load('images/slice_01.png'),\
             pygame.image.load('images/slice_02.png'),\
             pygame.image.load('images/slice_03.png'),\
             pygame.image.load('images/slice_04.png'),\
             pygame.image.load('images/slice_05.png'),\
             pygame.image.load('images/slice_06.png'),\
             pygame.image.load('images/slice_07.png'),\
             pygame.image.load('images/slice_08.png'),\
             pygame.image.load('images/slice_09.png'),\
             pygame.image.load('images/slice_10.png'),\
             pygame.image.load('images/slice_11.png'),\
             pygame.image.load('images/slice_12.png'),\
             pygame.image.load('images/slice_13.png'),\
             pygame.image.load('images/slice_14.png'),\
             pygame.image.load('images/slice_15.png'),\
             pygame.image.load('images/slice_16.png'),\
             pygame.image.load('images/slice_17.png'),\
             pygame.image.load('images/slice_18.png'),\
             pygame.image.load('images/slice_19.png'),\
             pygame.image.load('images/slice_20.png'),\
             pygame.image.load('images/slice_21.png'),\
             pygame.image.load('images/slice_22.png'),\
             pygame.image.load('images/slice_23.png'),\
             pygame.image.load('images/slice_24.png'),\
             pygame.image.load('images/slice_25.png'),\
             pygame.image.load('images/slice_26.png'),\
             pygame.image.load('images/slice_27.png'),\
             pygame.image.load('images/slice_28.png'),\
             pygame.image.load('images/slice_29.png'),\
             pygame.image.load('images/slice_30.png'),\
             pygame.image.load('images/slice_31.png'),\
             pygame.image.load('images/slice_32.png'),\
             pygame.image.load('images/slice_33.png'),\
             pygame.image.load('images/slice_34.png'),\
             pygame.image.load('images/slice_35.png'),\
             pygame.image.load('images/slice_36.png'),\
             pygame.image.load('images/slice_37.png'),\
             pygame.image.load('images/slice_38.png'),\
             pygame.image.load('images/slice_39.png'),\
             pygame.image.load('images/slice_40.png'),\
             pygame.image.load('images/slice_41.png'),\
             pygame.image.load('images/slice_42.png'),\
             pygame.image.load('images/slice_43.png'),\
             pygame.image.load('images/slice_44.png'),\
             pygame.image.load('images/slice_45.png'),\
             pygame.image.load('images/slice_46.png'),\
             pygame.image.load('images/slice_47.png'),\
             pygame.image.load('images/slice_48.png'),\
             pygame.image.load('images/slice_49.png'),\
             pygame.image.load('images/slice_50.png'),\
             pygame.image.load('images/slice_51.png'),\
             pygame.image.load('images/slice_52.png'),\
             pygame.image.load('images/slice_53.png'),\
             pygame.image.load('images/slice_54.png'),\
             pygame.image.load('images/slice_55.png'),\
             pygame.image.load('images/slice_56.png'),\
             pygame.image.load('images/slice_57.png'),\
             pygame.image.load('images/slice_58.png'),\
             pygame.image.load('images/slice_59.png'),\
             pygame.image.load('images/slice_60.png'),\
             pygame.image.load('images/slice_61.png'),\
             pygame.image.load('images/slice_62.png'),\
             pygame.image.load('images/slice_63.png'),\
             pygame.image.load('images/slice_64.png')]

class card():   # Individual cards class that I could not throw to external file without error

    def __init__(self,c_type):

        self.c_type = c_type    # The integer number that refers card type

        self.image = card_images[c_type]    # Pass the card type to image

        self.matched = 0    # Card is already matched

    def get_c_type(self):

        return self.c_type  # Return the type of card int

    def get_image(self):
        return self.image   # Get the image of card

    def set_matched(self):
        self.matched = 1    # This sets the card to being matched

    def get_matched(self):
        return self.matched  # Returns if the card has been matched or not



# Creating a window
main_screen = pygame.display.set_mode(SIZE,FS)


# Instantiating class objects
gm = GameMenu(main_screen)
player = Player()

# Music player
pygame.mixer.music.load('music/background.mp3')
pygame.mixer.music.play(-1, 0.0)


for i in range(board_size*board_size): # Go trough all of the cards

    rand_card = card_types[randint(0,len(card_types)-1)]    # Generate a random number in specified range and use it to choose index in field


    cards.append(card(rand_card))   # Make a card and store it to card field

    card_types.remove(rand_card)    # Remove already choosed card


# Main loop that runs game mechanics
while True:

    

    mouse_x,mouse_y = pygame.mouse.get_pos()    # Gets mouse position every frame and stores it in the variables

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()    # If code passes quit event, exit the game

    # Code that draws Menu screen
    if screentype == 'Menu':    

        gm.screen.blit(gm.bg,gm.bgrect)    # Draws a background

        gm.titlerect = gm.titlex,gm.titley  # Set the position for title image
        gm.screen.blit(gm.title,gm.titlerect)  # Draw title image
            
        gm.start_buttonrect = gm.sposx,gm.sposy # Set the position for start button
        gm.screen.blit(gm.start_button, gm.start_buttonrect) # Draws start button

        gm.options_buttonrect = gm.oposx,gm.oposy  # Set the position for options button
        gm.screen.blit(gm.options_button,gm.options_buttonrect) # Draws options button

        gm.quit_buttonrect = gm.qposx,gm.qposy  # Set the position for quit button
        gm.screen.blit(gm.quit_button, gm.quit_buttonrect) # Draws quit button

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:  # If mouse is clicked...
                         
                if (mouse_x > gm.sposx) & (mouse_x < gm.sposxmax) & (mouse_y > gm.sposy) & (mouse_y < gm.sposymax): # ... and is over button, do an action
                    screentype = 'Game'
                    pygame.time.wait(2000)
                elif (mouse_x > gm.oposx) & (mouse_x < gm.oposxmax) & (mouse_y > gm.oposy) & (mouse_y < gm.oposymax):
                    screentype = 'Options'
                    pygame.time.wait(2000)
                elif (mouse_x > gm.qposx) & (mouse_x < gm.qposxmax) & (mouse_y > gm.qposy) & (mouse_y < gm.qposymax):
                    sys.exit()

        if (mouse_x > gm.sposx) & (mouse_x < gm.sposxmax) & (mouse_y > gm.sposy) & (mouse_y < gm.sposymax): # If mouse is just over button change the image that is shown
            gm.screen.blit(gm.start_hover_button,gm.start_buttonrect)
            
        if (mouse_x > gm.oposx) & (mouse_x < gm.oposxmax) & (mouse_y > gm.oposy) & (mouse_y < gm.oposymax):
            gm.screen.blit(gm.options_hover_button,gm.options_buttonrect)

        if (mouse_x > gm.qposx) & (mouse_x < gm.qposxmax) & (mouse_y > gm.qposy) & (mouse_y < gm.qposymax):
            gm.screen.blit(gm.quit_hover_button,gm.quit_buttonrect)
            
    if screentype == 'Options':
        gm.screen.blit(gm.bg,gm.bgrect)

        gm.back_buttonrect = gm.bposx, gm.bposy
        gm.screen.blit(gm.back_button, gm.back_buttonrect)
        
        if (player.player_number >= 1):
            gm.players_buttonrect = gm.pposx, gm.pposy
            gm.screen.blit(gm.players_pressed_button, gm.players_buttonrect)

        if (player.player_number >= 2):
            gm.players_buttonrect = gm.pposx + 150, gm.pposy 
            gm.screen.blit(gm.players_pressed_button, gm.players_buttonrect)
        else:
            gm.players_buttonrect = gm.pposx + 150, gm.pposy 
            gm.screen.blit(gm.players_button, gm.players_buttonrect)

        if (player.player_number >= 3):
            gm.players_buttonrect = gm.pposx + 300, gm.pposy 
            gm.screen.blit(gm.players_pressed_button, gm.players_buttonrect)
        else:
            gm.players_buttonrect = gm.pposx + 300, gm.pposy 
            gm.screen.blit(gm.players_button, gm.players_buttonrect)

        if (player.player_number >= 4):
            gm.players_buttonrect = gm.pposx + 450, gm.pposy 
            gm.screen.blit(gm.players_pressed_button, gm.players_buttonrect)
        else:
            gm.players_buttonrect = gm.pposx + 450, gm.pposy 
            gm.screen.blit(gm.players_button, gm.players_buttonrect)

        if (mouse_x > gm.bposx) & (mouse_x < gm.bposxmax) & (mouse_y > gm.bposy) & (mouse_y < gm.bposymax):
            gm.screen.blit(gm.back_hover_button,gm.back_buttonrect)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (mouse_x > gm.bposx) & (mouse_x < gm.bposxmax) & (mouse_y > gm.bposy) & (mouse_y < gm.bposymax):
                    screentype = 'Menu'
                if (mouse_x > gm.pposx) & (mouse_x < gm.pposxmax) & (mouse_y > gm.pposy) & (mouse_y < gm.pposymax):
                    player.player_number = 1
                if (mouse_x > gm.pposx + 150) & (mouse_x < gm.pposxmax + 150) & (mouse_y > gm.pposy) & (mouse_y < gm.pposymax):
                    player.player_number = 2
                if (mouse_x > gm.pposx + 300) & (mouse_x < gm.pposxmax + 300) & (mouse_y > gm.pposy) & (mouse_y < gm.pposymax):
                    player.player_number = 3
                if (mouse_x > gm.pposx + 450) & (mouse_x < gm.pposxmax + 450) & (mouse_y > gm.pposy) & (mouse_y < gm.pposymax):
                    player.player_number = 4
    if screentype == 'Chart':
        gm.screen.blit(gm.bg,gm.bgrect) # Draw background

        gm.back_buttonrect = gm.bposx, gm.bposy
        gm.screen.blit(gm.back_button, gm.back_buttonrect)

        first_place = gm.scr_width/2 - 100,200
        first_placep = gm.scr_width/2 + 140,200

        second_place = gm.scr_width/2 - 100,250
        second_placep = gm.scr_width/2 + 140,250

        third_place = gm.scr_width/2 - 100,300
        third_placep = gm.scr_width/2 + 140,300

        fourth_place = gm.scr_width/2 - 100,350
        fourth_placep = gm.scr_width/2 + 140,350
         
        if (player.player_number >= 1):  # Checks for the player number            
            p1 = font1.render('Player 1 Points:',1,(0,0,0)) # If it is not players turn render players points in black
            p1_p = font1.render(str(player.p1_points),1,(0,0,0)) # Render actual point number
            gm.screen.blit(p1,first_place)
            gm.screen.blit(p1_p,first_placep)
            
        if (player.player_number >= 2):
            p2 = font1.render('Player 2 Points:',1,(0,0,0))
            p2_p = font1.render(str(player.p2_points),1,(0,0,0))
            gm.screen.blit(p2,second_place)
            gm.screen.blit(p2_p,second_placep)
           
        if (player.player_number >= 3):
            p3 = font1.render('Player 3 Points:',1,(0,0,0))
            p3_p = font1.render(str(player.p3_points),1,(0,0,0))
            gm.screen.blit(p3,third_place)
            gm.screen.blit(p3_p,third_placep)
            
        if (player.player_number >= 4):
            p4 = font1.render('Player 4 Points:',1,(0,0,0))
            p4_p = font1.render(str(player.p4_points),1,(0,0,0))
            gm.screen.blit(p4,fourth_place)
            gm.screen.blit(p4_p,fourth_placep)

        if (mouse_x > gm.bposx) & (mouse_x < gm.bposxmax) & (mouse_y > gm.bposy) & (mouse_y < gm.bposymax):
            gm.screen.blit(gm.back_hover_button,gm.back_buttonrect)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (mouse_x > gm.bposx) & (mouse_x < gm.bposxmax) & (mouse_y > gm.bposy) & (mouse_y < gm.bposymax):
                    screentype = 'Menu'
                    player.p1_points = 0
                    player.p2_points = 0
                    player.p3_points = 0
                    player.p4_points = 0

    # Code that draws Game screen
    if screentype == 'Game':

        

        gm.screen.blit(gm.bg,gm.bgrect) # Draw background
        
        if (player.player_number >= 1):  # Checks for the player number
            if player.player_turn == 1:   # Checks for player turn
                p1 = font1.render('Player 1 Points:',1,(255,255,255)) # If it is players turn than render Player points in white  
            else: 
                p1 = font1.render('Player 1 Points:',1,(0,0,0)) # If it is not players turn render players points in black
            p1_p = font1.render(str(player.p1_points),1,(0,0,0)) # Render actual point number
            gm.screen.blit(p1,(gm.scr_width/2 - 100,720))   # Position and draw Players points text
            gm.screen.blit(p1_p,(gm.scr_width/2 + 140,720)) # Postion and draw Players points number

        if (player.player_number >= 2):
            if player.player_turn == 2:
                p2 = font1.render('Player 2 Points:',1,(255,255,255)) 
            else:
                p2 = font1.render('Player 2 Points:',1,(0,0,0))
            p2_p = font1.render(str(player.p2_points),1,(0,0,0))
            p2 = pygame.transform.rotate(p2,-90)
            p2_p = pygame.transform.rotate(p2_p,-90)
            gm.screen.blit(p2,(1315,gm.scr_height/2 - 100))
            gm.screen.blit(p2_p,(1315,gm.scr_height/2 + 140))

        if (player.player_number >= 3):
            if player.player_turn == 3:
                p3 = font1.render('Player 3 Points:',1,(255,255,255))  
            else:
                p3 = font1.render('Player 3 Points:',1,(0,0,0))
            p3_p = font1.render(str(player.p3_points),1,(0,0,0))
            gm.screen.blit(p3,(gm.scr_width/2 - 100,50))
            gm.screen.blit(p3_p,(gm.scr_width/2 + 140,50))

        if (player.player_number >= 4):
            if player.player_turn == 4:
                p4 = font1.render('Player 4 Points:',1,(255,255,255))  
            else:
                p4 = font1.render('Player 4 Points:',1,(0,0,0))
            p4_p = font1.render(str(player.p4_points),1,(0,0,0))
            p4 = pygame.transform.rotate(p4,90)
            p4_p = pygame.transform.rotate(p4_p,90)
            gm.screen.blit(p4,(50,gm.scr_height/2 - 100))
            gm.screen.blit(p4_p,(50,gm.scr_height/2 - 125))

        
        for x in range(board_size):      # Loop that goes trough every card
            for y in range(board_size):
                if cards[x+y*board_size].get_matched() == 0: # If the card with specific index has not yet been matched
                    

                    gm.screen.blit(card_bg,((gm.scr_width/2 - 276)+x*138,98 + y*138,128,128)) # Draws the background tile

                    if 392 + x*138 < mouse_x < 392+ x*138 + 138 and 98 + y*138 < mouse_y < 98+ y*138 +138: # If mouse is hovering a tile
                        
                        
                        gm.screen.blit(card_bghover,((gm.scr_width/2 - 276)+x*138,98 + y*138,128,128)) # Draw the hover tile 
        
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN: # If mouse button is pressed down

                                if choice[0] == 0:  # If this is your first choice
                                    choice[0] = cards[x+y*board_size]  # Join the card field index to the first choice 

                                if choice[1] == 0 and choice[0] != cards[x+y*board_size]: # If you already choosed one card, this is your second choice
                                    choice[1] = cards[x+y*board_size]  # Join the card field index to the second choice

                    else:
                        gm.screen.blit(card_bg,((gm.scr_width/2 - 276)+(x*138),98 + y*138,128,128)) # If mouse is not hovering a tile, draw background tile

                    
                    
                    if choice[0] == cards[x+y*board_size]:   # If card have been picked, draw the image on the selected tile
                        gm.screen.blit(choice[0].get_image(),((gm.scr_width/2 - 276)+x*138,98 + y*138,128,128))
                        anim_position = (gm.scr_width/2 - 276)+(x*138),98 + y*138
                   

                    if choice[1] == cards[x+y*board_size]:   # If card have been picked, draw the image on the selected tile
                        gm.screen.blit(choice[1].get_image(),((gm.scr_width/2 - 276)+x*138,98 + y*138,128,128))
                        anim_position2 = (gm.scr_width/2 - 276)+(x*138),98 + y*138
                    
            
        if choice[0] != 0 and choice[1] != 0:   # If two cards have been picked
            
            pygame.display.flip()   # Draw everything 
            pygame.time.wait(300)   # Time delay beetwen erasing fliped images
            
            

            if choice[0].get_c_type() == choice[1].get_c_type():    # If cards are the same type

                if player.player_turn == 1:    # If it is player1's turn then give them a point
                    player.p1_points += 1

                elif player.player_turn == 2:  # If it is player2's turn give them a point
                    player.p2_points += 1

                elif player.player_turn == 3:  # If it is player3's turn give them a point
                    player.p3_points += 1

                elif player.player_turn == 4:  # If it is player4's turn give them a point
                    player.p4_points += 1

                choice[0].set_matched()  # Flag the card that it has been matched already
                choice[1].set_matched()
                for k in range(63):
                    gm.screen.blit(animation[k], anim_position)
                    gm.screen.blit(animation[k], anim_position2)
                    pygame.time.wait(20)
                    pygame.display.flip()


            if player.player_turn == 1:    # Checks which players turn is
                if player.player_number > 1: # Checks the number of players
                    player.player_turn = 2  # Sets next turn player
                else:
                    player.player_turn = 1

            elif player.player_turn == 2:   
                if player.player_number > 2:
                    player.player_turn = 3
                else:
                    player.player_turn = 1
            
            elif player.player_turn == 3:   
                if player.player_number > 3:
                    player.player_turn = 4
                else:
                    player.player_turn = 1
            
            elif player.player_turn == 4: 
                player.player_turn = 1

            
            choice = [0,0]  # Reset the chosen cards

        if player.p1_points+player.p2_points+player.p3_points+player.p4_points == 8:   # If all matches are made, show chart screen
           screentype = 'Chart'

        
    pygame.display.flip()   # General display drawing

quit()