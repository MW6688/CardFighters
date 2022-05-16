import pygame
pygame.init()
import time
clock = pygame.time.Clock()
#Colors:
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 234, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
Char1Col = (255, 0, 0)
Char2Col = (0,255,0)
Char3Col= (0,0,255)
Char4Col= (255, 234, 0)


display_width = 800
display_height = 600

gameWindow = pygame.display.set_mode((600, 800))
pygame.font.init()
pygame.display.set_caption("Selection Menu Test")

##Copy and Paste from Here#


while display_width == 800:
  print(pygame.mouse.get_pos())
  mouseX,mouseY = pygame.mouse.get_pos()
  pygame.event.clear()
  pygame.draw.rect(gameWindow, Char1Col, pygame.Rect(0, 0, 200, 600),  0) #CharlSel1
  pygame.draw.rect(gameWindow, Char2Col, pygame.Rect(150, 0, 200, 600),  0)
#CharSel2
  pygame.draw.rect(gameWindow, Char3Col, pygame.Rect(300, 0, 200, 600),  0)
#CharSel3
  pygame.draw.rect(gameWindow, Char4Col, pygame.Rect(450, 0, 200, 600),  0)
#CharSel4
  if mouseX < 150 and mouseY <600 and mouseX > 5:
    print("Red Zone")
    Char1Col = (255, 81, 83)
    Char2Col = (0,255,0)
    Char3Col= (0,0,255)
    Char4Col= (255, 234, 0)
  if mouseX < 300 and mouseX > 150 and mouseY <600:
    print("Green Zone")
    Char1Col =(255, 0, 0) 
    Char2Col = (129, 250, 127)
    Char3Col= (0,0,255)
    Char4Col= (255, 234, 0)
  if mouseX < 450 and mouseX > 300 and mouseY <600:
    print("Blue Zone")
    Char1Col = (255, 0, 0)
    Char2Col = (0,255,0)
    Char3Col= (96, 108, 250)
    Char4Col= (255, 234, 0)
  if mouseX < 600 and mouseX > 450 and mouseY <600:
    print("Yellow Zone")
    Char1Col = (255, 0, 0)
    Char2Col = (0,255,0)
    Char3Col= (0,0,255)
    Char4Col= (255, 254, 76)
  pygame.display.update()
  pygame.time.delay(80)


