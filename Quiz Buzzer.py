# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 19:17:30 2020

@author: Jack
"""

import pygame #import pygame library
import sys # import system functions
from pygame.locals import *


pygame.init() # initialize the game engine
pygame.mixer.init()

#define sounds

player1_buzzer = pygame.mixer.Sound('buzzer1.wav')
player2_buzzer = pygame.mixer.Sound('buzzer2.wav')

#define colours

black = [0, 0, 0]

white = [255, 255, 255]

red = [255, 0, 0]

green = [0, 255, 0]

#input for player names (console)

player1_name = input("Enter name for Player 1: ")
player2_name = input("Enter name for Player 2: ")
player3_name = input("Enter name for Player 3: ")
player4_name = input("Enter name for Player 4: ")

#p1_key =

#initial state for player scores

p1_score=0
p2_score=0
p3_score=0
p4_score=0
 

#set height and width of screen

size = [800, 600]

screen = pygame.display.set_mode(size)
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

#function for black squares

def black_sq():
  pygame.draw.rect(screen, black, (20,200,150,150), 0)

  pygame.draw.rect(screen, black, (210,200,150,150), 0)

  pygame.draw.rect(screen, black, (400,200,150,150), 0)

  pygame.draw.rect(screen, black, (590,200,150,150), 0)

#add title and player names to screeen

screen.blit(label, (10,10))

screen.blit(player1, (50,150))

screen.blit(player2, (240,150))

screen.blit(player3, (430,150))

screen.blit(player4, (620,150))

#draw black squares
black_sq()

#show environment

pygame.display.flip()

 

lockout = False # set initial state for lockout


#keypresses and outputs

while True: #loop until quit

  if lockout == False:#when buzzers are in play

    for event in pygame.event.get():

      if event.type == pygame.QUIT:

        pygame.quit()
        sys.exit()# break out of loop

      #if event.key == pygame.K_LCTRL or K_RCTRL and K_q:
        #pygame.quit()


      if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_LEFT and lockout == False:

          print("Left Key Pressed") #print to console

          pygame.draw.rect(screen, red, (20,200,150,150) , 0)
          player1_buzzer.play()
          lockout=True

        if event.key == pygame.K_RIGHT: #and lockout == False:

          print("Right Key Pressed") #print to console

          pygame.draw.rect(screen, red, (210,200,150,150) , 0)
          player2_buzzer.play()
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

    #reset buzzers and make all squares black
    for event in pygame.event.get():
      if event.key == pygame.K_RETURN:
        lockout=False
        black_sq()

      pygame.display.flip()

