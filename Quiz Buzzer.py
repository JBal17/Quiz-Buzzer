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

#set height and width of screen

size = [800, 600]

screen = pygame.display.set_mode(size)
screen.fill(white) # fill screen white

# set caption
pygame.display.set_caption("Lockout Quiz Buzzer")

#definte font
myfont = pygame.font.SysFont("Ariel", 30)
name_font = pygame.font.SysFont("Ariel", 120)

#define function for entering player name
def name(p_number):

  name =""
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()# break out of loop
      if event.type == KEYDOWN:
        if event.unicode.isalpha():
          name += event.unicode
        elif event.key == K_BACKSPACE:
          name = name[:-1]
        elif event.key == K_RETURN:
          return name
    screen.fill(black)
    block = name_font.render(name, True, white)
    rect = block.get_rect()
    rect.center = screen.get_rect().center
    screen.blit(block, rect)
    title = myfont.render("Enter Name of Player " + str(p_number), 1, white)
    screen.blit(title, (10, 10))
    pygame.display.flip()


#call player input name function

player1_name = name(1)
player2_name = name(2)
player3_name = name(3)
player4_name = name(4)

screen.fill(white) # fill screen white
pygame.display.flip()

#initial state for player scores

p1_score= 0
p2_score= 0
p3_score= 0
p4_score= 0


#set player name styles

player1 = myfont.render(player1_name, 1, black)
player2 = myfont.render(player2_name, 1, black)
player3 = myfont.render(player3_name, 1, black)
player4 = myfont.render(player4_name, 1, black)

#set score styles

score1 = myfont.render(str(p1_score), 1, black)
score2 = myfont.render(str(p2_score), 1, black)
score3 = myfont.render(str(p3_score), 1, black)
score4 = myfont.render(str(p4_score), 1, black)

#set title

label = myfont.render("Quiz Buzzer", 1, black)

#function for black squares

def black_sq():
  pygame.draw.rect(screen, black, (20,200,150,150), 0)
  pygame.draw.rect(screen, black, (210,200,150,150), 0)
  pygame.draw.rect(screen, black, (400,200,150,150), 0)
  pygame.draw.rect(screen, black, (590,200,150,150), 0)

#add title player names and scores to screeen

screen.blit(label, (10,10))

screen.blit(player1, (75,150))
screen.blit(player2, (265,150))
screen.blit(player3, (455,150))
screen.blit(player4, (645,150))

def display_scores():
  pygame.draw.rect(screen, white, (50,380,700,60), 0)
  screen.blit(myfont.render(str(p1_score), 1, black), (95,400))
  screen.blit(myfont.render(str(p2_score), 1, black), (285,400))
  screen.blit(myfont.render(str(p3_score), 1, black), (475,400))
  screen.blit(myfont.render(str(p4_score), 1, black), (665,400))
  pygame.display.flip()

display_scores()

#draw black squares
black_sq()

#show environment
pygame.display.flip()

# set initial state for lockout
lockout = False


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

        if event.key == pygame.K_LEFT:
          print("Left Key Pressed") #print to console
          pygame.draw.rect(screen, red, (20,200,150,150), 0)
          player1_buzzer.play()
          lockout = True

        if event.key == pygame.K_RIGHT:
          print("Right Key Pressed") #print to console
          pygame.draw.rect(screen, red, (210,200,150,150), 0)
          player2_buzzer.play()
          lockout = True

        if event.key == pygame.K_UP:
          print("Up Key Pressed") #print to console
          pygame.draw.rect(screen, red, (400,200,150,150), 0)
          lockout = True

        if event.key == pygame.K_DOWN:
          print("Down Key Pressed") #print to console
          pygame.draw.rect(screen, red, (590,200,150,150), 0)
          lockout = True

        if event.key == pygame.K_1:
          p1_score += 1

        if event.key == pygame.K_2:
          p2_score += 1

        if event.key == pygame.K_3:
          p3_score += 1

        if event.key == pygame.K_4:
          p4_score += 1

        if event.key == pygame.K_F1:
          p1_score -= 1

        if event.key == pygame.K_F2:
          p2_score -= 1

        if event.key == pygame.K_F3:
          p3_score -= 1

        if event.key == pygame.K_F4:
          p4_score -= 1

        display_scores()

          
  if lockout == True: #when buzzer has been pressed and buzzers are locked out

    #reset buzzers and make all squares black
    for event in pygame.event.get():
      if event.key == pygame.K_RETURN:
        lockout = False
        print("Reset")
        black_sq()
      pygame.display.flip()