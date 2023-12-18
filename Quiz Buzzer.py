import pygame #import pygame library
import sys # import system functions
import time
from pygame.locals import *

pygame.init() # initialize the game engine
pygame.mixer.init()

screen_width = 800
screen_height = 600

size = [screen_width, screen_height]

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]


font_title = pygame.font.SysFont("Ariel", 60)
myfont = pygame.font.SysFont("Ariel", 180)
name_font = pygame.font.SysFont("Ariel",400)

label = font_title.render("", 1, black)

correct_answer_sound = pygame.mixer.Sound('correct_answer.wav')

j = pygame.joystick.Joystick(0)
j.init()

p1_text_y = 200
p2_text_y = 400
p3_text_y = 600
p4_text_y = 800

player_names_x = 200
player_scores_x = 1500


def display_scores():
  pygame.draw.rect(screen, white, (player_scores_x,p1_text_y,200,800), 0)
  screen.blit(myfont.render(str(player_one.score), 1, black), (player_scores_x,p1_text_y))
  screen.blit(myfont.render(str(player_two.score), 1, black), (player_scores_x,p2_text_y))
  screen.blit(myfont.render(str(player_three.score), 1, black), (player_scores_x,p3_text_y))
  screen.blit(myfont.render(str(player_four.score), 1, black), (player_scores_x,p4_text_y))
  pygame.display.flip()


def mainscreen():
  screen.fill(white)
  screen.blit(label, (100, 10)) #add title
  #add player names
  screen.blit(player1, (player_names_x, p1_text_y))
  screen.blit(player2, (player_names_x, p2_text_y))
  screen.blit(player3, (player_names_x, p3_text_y))
  screen.blit(player4, (player_names_x, p4_text_y))

def correct(string, bg_colour, text_colour):
  screen.fill(bg_colour)
  block = name_font.render(string, True, text_colour)
  rect = block.get_rect()
  rect.center = screen.get_rect().center
  screen.blit(block, rect)
  pygame.display.flip()

class Player():
    def __init__(self, text_colour, bg_colour, buzzer_sound, player_colour_string):
        self.player_colour_string = player_colour_string
        self.text_colour = text_colour
        self.bg_colour = bg_colour
        self.player_name = self.name()
        self.buzzer_sound = pygame.mixer.Sound(buzzer_sound)
        self.score = 0

    def buzz_in(self):
       screen.fill(self.bg_colour)
       block = name_font.render(self.name, True, self.text_colour)
       rect = block.get_rect()
       rect.center = screen.get_rect().center
       screen.blit(block, rect)
       self.buzzer_sound.play()
       pygame.display.flip()

    def name(self):
        self.name =""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()# break out of loop
                if event.type == KEYDOWN:
                   if event.key == K_BACKSPACE and len(self.name) > 0:
                      self.name = self.name[:-1]
                   elif event.key == K_RETURN:
                      return self.name
                   elif event.key == K_TAB:
                      self.name = ""
                   else:
                      self.name += event.unicode
                  
                    
                # if event.type == KEYDOWN:
                #     if event.unicode:#.isalpha():
                #         self.name += event.unicode
                #     elif event.key == K_BACKSPACE:
                #         self.name = self.name[:-1]
                #     elif event.key == K_RETURN:
                #         return self.name
                      
            screen.fill(black)
            block = name_font.render(self.name, True, white)
            rect = block.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(block, rect)
            title = font_title.render(f"Enter Name of {self.player_colour_string} Player" , 1, white)
            screen.blit(title, (10, 10))
            pygame.display.flip()
    
    def increase_score(self):
       self.score += 1

    def decrease_score(self):
       self.score -= 1


screen.fill(white) # fill screen white
pygame.display.flip()        

player_one = Player(black, red, 'ding.mp3', 'Red')
player_two = Player(black, green, 'ding.mp3', 'Green')
player_three = Player(black, yellow, 'ding.mp3', 'Yellow')
player_four = Player(white, blue, 'ding.mp3', 'Blue')

player1 = myfont.render(player_one.name, 1, black)
player2 = myfont.render(player_two.name, 1, black)
player3 = myfont.render(player_three.name, 1, black)
player4 = myfont.render(player_four.name, 1, black)

def main():
# set initial state for lockout
  lockout = False
  mainscreen()
  while True: #loop until quit

    active_player = ""

    if lockout == False:#when buzzers are in play

      for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # close pygame window
        
        display_scores()

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_1:
              player_one.increase_score()

          if event.key == pygame.K_2:
              player_two.increase_score()

          if event.key == pygame.K_3:
              player_three.increase_score()

          if event.key == pygame.K_4:
              player_four.increase_score()

          if event.key == pygame.K_6:
              player_one.decrease_score()

          if event.key == pygame.K_7:
              player_two.decrease_score()

          if event.key == pygame.K_8:
              player_three.decrease_score()

          if event.key == pygame.K_9:
              player_four.decrease_score()

        if event.type == pygame.JOYBUTTONDOWN:
          print("Button Pressed")

          if j.get_button(0):
            player_one.buzz_in()
            lockout = True
            active_player = player_one
          
          if j.get_button(1):
            player_two.buzz_in()
            lockout = True
            active_player = player_two

          if j.get_button(2):
            player_three.buzz_in()
            lockout = True
            active_player = player_three
          
          if j.get_button(3):
            player_four.buzz_in()
            lockout = True
            active_player = player_four

    if lockout == True: #when buzzer has been pressed and buzzers are locked out

      for event in pygame.event.get():

        #if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):


        if j.get_button(4):
           correct('CORRECT', green, black)
           correct_answer_sound.play()
           time.sleep(2)
           lockout = False
           mainscreen()
      
        if j.get_button(5):
          lockout = False
          print("Reset")
          mainscreen()

main()