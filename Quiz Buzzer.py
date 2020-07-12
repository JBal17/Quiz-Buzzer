# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 19:17:30 2020

@author: Jack
"""

import pygame #import pygame library
import sys # import system functions
from pygame.locals import *


pygame.init() # initialize the game engine


#define colours

black = [0, 0, 0]

white = [255, 255, 255]

red = [255, 0, 0]

#input for player names (console)

player1_name = input("Enter name for Player 1: ")
player2_name = input("Enter name for Player 2: ")
player3_name = input("Enter name for Player 3: ")
player4_name = input("Enter name for Player 4: ")
 

#set height and width of screen

#size = [800, 600]

#screen = pygame.display.set_mode(size)


screen = pygame.display.set_mode((0,0), pygame.RESIZABLE) 

screen.fill(white) # fill screen white

 
# set caption
pygame.display.set_caption("Quiz Buzzer")

 
#definte font
myfont = pygame.font.SysFont("Ariel", 30)



player1= myfont.render(player1_name, 1, black)

player2 = myfont.render(player2_name, 1, black)

player3 = myfont.render(player3_name, 1, black)

player4 = myfont.render(player4_name, 1, black)

#set title

label = myfont.render("Quiz Buttons", 1, black)

#draw boxes on screen

pygame.draw.rect(screen, black, (20,200,150,150), 0)

pygame.draw.rect(screen, black, (210,200,150,150), 0)

pygame.draw.rect(screen, black, (400,200,150,150), 0)

pygame.draw.rect(screen, black, (590,200,150,150), 0)

#add title andplayernames to screeen

screen.blit(label, (10,10))

screen.blit(player1, (50,150))

screen.blit(player2, (240,150))

screen.blit(player3, (430,150))

screen.blit(player4, (620,150))

 

#show environment

pygame.display.flip()

 

lockout = False # set initial state for lockout


#keypresses and outputs

while True: #loop until quit

  if lockout == False:#when buzzers are in play

    for event in pygame.event.get():

      if event.type == pygame.QUIT:

        pygame.quit() # break out of loop

      #if event.key == pygame.K_LCTRL or K_RCTRL and K_q:
        pygame.quit()
        

      if event.type == pygame.KEYDOWN:# and lockout == False:

        if event.key == pygame.K_LEFT and lockout == False:

          print("Left Key Pressed") #print to console

          pygame.draw.rect(screen, red, (20,200,150,150) , 0)

          lockout=True

        if event.key == pygame.K_RIGHT: #and lockout == False:

          print("Right Key Pressed") #print to console

          pygame.draw.rect(screen, red, (210,200,150,150) , 0)

          lockout=1

        if event.key == pygame.K_UP:# and lockout == False:

          print("Up Key Pressed") #print to console

          pygame.draw.rect(screen, red, (400,200,150,150) , 0)

          lockout=True

        if event.key == pygame.K_DOWN:# and lockout == False:

          print("Down Key Pressed") #print to console

          pygame.draw.rect(screen, red, (590,200,150,150) , 0)

          lockout=True
          
  if lockout == True: #when buzzer has been pressed and buzzers are locked out
    
    for event in pygame.event.get():
      if event.key == pygame.K_RETURN:
        lockout=False
        pygame.draw.rect(screen, black, (20,200,150,150), 0)

        pygame.draw.rect(screen, black, (210,200,150,150), 0)

        pygame.draw.rect(screen, black, (400,200,150,150), 0)

        pygame.draw.rect(screen, black, (590,200,150,150), 0)

      pygame.display.flip()

pygame.quit() #quit game
sys.exit(0)
