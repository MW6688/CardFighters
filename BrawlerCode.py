#########################################
# File Name: AnimatedCharacter.py
# Description: Demonstrates how to animate a character 
#########################################
# sample change
import pygame
pygame.init()
HEIGHT = 400
WIDTH  = 640
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = ( 255, 255, 255)

#---------------------------------------#
#   functions                           #
#---------------------------------------#
def redrawGameWindow():
    gameWindow.fill(WHITE)
    gameWindow.blit(marioPic[marioPicNum], (marioX, marioY))
    pygame.display.update()  

#---------------------------------------#
#   main program                        #
#---------------------------------------# 
GROUND_LEVEL = 300
RUN_SPEED = 10
JUMP_SPEED = -30
GRAVITY = 2

mario = pygame.image.load("images/mario1.png")
marioH = 63
marioW = 33
marioX = WIDTH/2
marioY = GROUND_LEVEL
marioVx = 0
marioVy = 0
marioPicNum = 1                         # current picture of mario
marioDir = "left"                       # direction in which mario is facing
marioPic =[0]*12                        # 12 pictures represent all animated views of mario
for i in range(12):                     # these pictures must be in the same folder
    marioPic[i] = pygame.image.load("images/mario" + str(i) + ".png")

nextLeftPic  = [1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]
nextRightPic = [4, 4, 4, 4, 5, 6, 7, 5, 4, 4, 4, 4]

print("Hit ESC to end the program.")
clock = pygame.time.Clock()
FPS = 30

#---------------------------------------#
inPlay = True
while inPlay:              
    redrawGameWindow()
    clock.tick(FPS)
    
    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False

# set direction and select picture depending on the arrow keys
    if keys[pygame.K_LEFT]:
        marioVx = -RUN_SPEED
        marioDir = "left"
        if marioY == GROUND_LEVEL:
            marioPicNum = nextLeftPic[marioPicNum]
    elif keys[pygame.K_RIGHT]:
        marioVx = RUN_SPEED
        marioDir = "right"
        if marioY == GROUND_LEVEL:
            marioPicNum = nextRightPic[marioPicNum]
    else:                               # if neither left nor right arrow is pressed
        marioVx = 0                     # mario is in standing still position
        if marioDir == "left":          # when standing,
            marioPicNum = 0             # the animation view is either 1 or 5,
        elif marioDir == "right":       # depending on the direction in which
            marioPicNum = 4             # mario is facing
            
    if keys[pygame.K_UP] and marioY == GROUND_LEVEL:
        marioVy = JUMP_SPEED
        if marioDir == "left":          # when jumping,
            marioPicNum = 8             # the animation view is either 9 or 10,
        elif marioDir == "right":       # depending on the direction in which
            marioPicNum = 9             # mario is facing
    elif keys[pygame.K_DOWN] and marioY == GROUND_LEVEL:
        marioVx = 0
        if marioDir == "left":          # when squatting,
            marioPicNum = 10            # the animation view is either 11 or 12,
        elif marioDir == "right":       # depending on the direction in which
            marioPicNum = 11            # mario is facing

# move Mario in horizontal direction
    marioX = marioX + marioVx
# update Mario's vertical velocity
    marioVy = marioVy + GRAVITY
# move Mario in vertical direction
    marioY = marioY + marioVy
    if marioY > GROUND_LEVEL:
        marioY = GROUND_LEVEL
        marioVy = 0
        
#---------------------------------------# 
pygame.quit()
