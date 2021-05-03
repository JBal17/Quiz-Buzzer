# -*- coding: utf-8 -*-
"""
Lockout Quiz Buzzer using pygame
"""

import pygame #import pygame library
import sys # import system functions
from pygame.locals import *


pygame.init() # initialize the game engine
pygame.mixer.init()

#define sounds

player1_buzzer = pygame.mixer.Sound('buzzer1.wav')
player2_buzzer = pygame.mixer.Sound('buzzer2.wav')
player3_buzzer = pygame.mixer.Sound('buzzer3.wav')
player4_buzzer = pygame.mixer.Sound('buzzer4.wav')

#define colours

black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]

#set height and width of screen
screen_width = 800
screen_height = 600

size = [screen_width, screen_height]

screen = pygame.display.set_mode(size)

# set caption
pygame.display.set_caption("Lockout Quiz Buzzer")

#definte fonts
font_title = pygame.font.SysFont("Ariel", 60)
myfont = pygame.font.SysFont("Ariel", 90)
name_font = pygame.font.SysFont("Ariel", 170)

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
    title = font_title.render("Enter Name of Player " + str(p_number), 1, white)
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

label = font_title.render("Quiz Buzzer", 1, black)

# initialise joystick buttons

j = pygame.joystick.Joystick(0)
j.init()

#function for black squares

def black_sq():
  pygame.draw.rect(screen, black, (20,200,150,150), 0)
  pygame.draw.rect(screen, black, (210,200,150,150), 0)
  pygame.draw.rect(screen, black, (400,200,150,150), 0)
  pygame.draw.rect(screen, black, (590,200,150,150), 0)

#add title player names and scores to screeen

def display_scores():
  pygame.draw.rect(screen, white, (600,110,200,480), 0)
  screen.blit(myfont.render(str(p1_score), 1, black), (600,110))
  screen.blit(myfont.render(str(p2_score), 1, black), (600,240))
  screen.blit(myfont.render(str(p3_score), 1, black), (600,370))
  screen.blit(myfont.render(str(p4_score), 1, black), (600,500))
  pygame.display.flip()

#display name of player who buzzed

def buzz(name, bg_colour, text_colour):
  screen.fill(bg_colour)
  block = name_font.render(name, True, text_colour)
  rect = block.get_rect()
  rect.center = screen.get_rect().center
  screen.blit(block, rect)
  pygame.display.flip()

#default screen view
def mainscreen():
  screen.fill(white)
  screen.blit(label, (100, 10)) #add title
  #add player names
  screen.blit(player1, (100, 110))
  screen.blit(player2, (100, 240))
  screen.blit(player3, (100, 370))
  screen.blit(player4, (100, 500))

  display_scores()
  pygame.display.flip() #show environment

# set initial state for lockout


  #keypresses and outputs
def main():

  lockout = False
  mainscreen()
  while True: #loop until quit

    active_player = ""

    if lockout == False:#when buzzers are in play

      for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # close pygame window

        if event.type == pygame.KEYDOWN:
          global p1_score
          global p2_score
          global p3_score
          global p4_score

          if event.key == pygame.K_1:
              p1_score += 1
              print('P1 score +1!')

          if event.key == pygame.K_2:
              p2_score += 1
              print('P2 score +1!')

          if event.key == pygame.K_3:
              p3_score += 1
              print('P3 score +1!')

          if event.key == pygame.K_4:
              p4_score += 1
              print('P4 score +1!')

          if event.key == pygame.K_F1:
              p1_score -= 1
              print('P1 score -1!')

          if event.key == pygame.K_F2:
              p2_score -= 1
              print('P2 score -1!')

          if event.key == pygame.K_F3:
              p3_score -= 1
              print('P3 score -1!')

          if event.key == pygame.K_F4:
              p4_score -= 1
              print('P4 score -1!')

        display_scores()

        if event.type == pygame.JOYBUTTONDOWN:
          print("Button Pressed")

          if j.get_button(0):
            print("BUTTON 0")
            buzz(player1_name, red, black)
            player1_buzzer.play()
            lockout = True

          if j.get_button(1):
            print("BUTTON 1")
            buzz(player2_name, green, black)
            player2_buzzer.play()
            lockout = True

          if j.get_button(2):
            print("BUTTON 2")
            buzz(player3_name, yellow, black)
            player3_buzzer.play()
            lockout = True

          if j.get_button(3):
            print("BUTTON 3")
            buzz(player4_name, blue, white)
            player4_buzzer.play()
            lockout = True

    if lockout == True: #when buzzer has been pressed and buzzers are locked out

      for event in pygame.event.get():

        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
          lockout = False
          print("Reset")
          mainscreen()


main()