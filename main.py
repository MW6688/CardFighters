import time
from PIL import Image, ImageSequence
import pygame
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
TitleColor = (255, 198, 0)
Char1Col = (255, 222, 94)
Char2Col = (224, 95, 0)
Char3Col = (231, 22, 8)
Char4Col = (247, 180, 67)
DispCol = (111, 143, 175)
ConfButtCol = (181, 43, 38)
elapsed = 0
triggered = False
PERIOD = 3
FPS = 24
p1choicedisp = (-1000, -2000)
p2choicedisp = (-1000, -2000)
# sample change 2
###Loading and Defining Variables (loading)###
pygame.display.set_caption("CardFighters")
pygame.font.init()
font = pygame.font.SysFont("comicsans", 60)
loadinggraphics = font.render("Loading...", 1, WHITE)

gameWindow = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()
ground = gameWindow.get_height() * 3 // 4
p1choice = 0
p2choice = 0
p1conf = False
p2conf = False



def startloadMusic():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.mixer.music.load("Capyvibe.mp3")
    pygame.mixer.music.play(loops = -1)


def startMenuMusic():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.mixer.music.load("MENUMUS.mp3")
    pygame.mixer.music.play(-1)


def stopMusic():
    pygame.mixer.music.stop()


# Title Code
Titlefont = pygame.font.Font("Bungee-Regular.ttf", 30)
Titlegraphics = Titlefont.render("Left Click To Start", 1, (225,225,225))

#GameTitlePNG#
GameTitle = pygame.image.load('CardFighters Title.png')

# Menubackground
Menubackground = pygame.image.load("MenuBackground.png")

#Player1ChoiceClearText
Choicefont = pygame.font.Font("Bungee-Regular.ttf", 30)
P1Choicegraphics = Choicefont.render("Player 1 Chose:", 1, BLACK)

#Player2ChoiceClearText
Choicefont2 = pygame.font.Font("Bungee-Regular.ttf", 30)
P2Choicegraphics = Choicefont.render("Player 2 Chose:", 1, BLACK)

#DisplayChoice#
DChofont = pygame.font.Font("Bungee-Regular.ttf", 30)
Choicegraphics = DChofont.render("Click Here to Reset Your Choices", 1, BLACK)

#CharacterConfirmButtonText#
CharConf = pygame.font.Font("Bungee-Regular.ttf", 30)
ConfButGraphics = CharConf.render("CONFIRM CHOICES", 1, WHITE)

#CharChoiceLogoP1#
LogoP1 = pygame.image.load('p1_cho.png')
#CharChoiceLogoP2#
LogoP2 = pygame.image.load('p2_cho.png')

GameStatus = "Menu"


def PrintStatus():
    print("Now in "+GameStatus + " Stage")

if GameStatus == "Menu":
    pygame.mixer.init()
    pygame.mixer.music.load("MENUMUS.mp3")
    pygame.mixer.music.play(-1)
    print("menumusic")
    #sample change
while GameStatus == "Menu":
    gameWindow.blit(Menubackground, (0, 0))
    gameWindow.blit(GameTitle, (60, -100))
    gameWindow.blit(Titlegraphics, (130, 285))
    pygame.event.clear()
    pygame.display.update()
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Click Detected, starting game...")
            GameStatus = "Loading"
            PrintStatus()



def loadGIF(filename):  # Converting the capybara gif into sprite frames#
    pilImage = Image.open(filename)
    frames = []
    for frame in ImageSequence.Iterator(pilImage):
        frame = frame.convert('RGBA')
        pygameImage = pygame.image.fromstring(frame.tobytes(), frame.size,
                                              frame.mode).convert_alpha()
        frames.append(pygameImage)
    return frames


class AnimatedSpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, bottom, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=(x, bottom+180))
        self.image_index = 0

    def update(self):  # Animation Frames#
        self.image_index += 1
        self.image = self.images[self.image_index % len(self.images)]
        self.rect.x -= 15
        if self.rect.right < 0:
            self.rect.left = pygame.display.get_surface().get_width()


pygame.init()

gifFrameList = loadGIF('CapyBaraMyLove.gif')
animated_sprite = AnimatedSpriteObject(gameWindow.get_width() // 2, ground,
                                       gifFrameList)
all_sprites = pygame.sprite.Group(animated_sprite)

pygame.time.set_timer(pygame.USEREVENT+1, 3000)

def spriterefresh():
    clock.tick(20)
    all_sprites.update()
    all_sprites.draw(gameWindow)
    pygame.display.flip()
    pygame.event.clear()
    pygame.display.update()

tmptime = time.time()


if GameStatus == "Loading":
    print("startmusic")
    pygame.mixer.music.load("Capyvibe.mp3")
    pygame.mixer.music.play(loops = -1)

while GameStatus == "Loading":
    triggered = True
    
    #startloadMusic()
    gameWindow.fill((255, 134, 69), (0, 0, gameWindow.get_width(), ground))
    gameWindow.fill((255, 127, 64),
                    (0, ground, gameWindow.get_width(), gameWindow.get_height() - ground))
    gameWindow.blit(loadinggraphics, (180, 100))
    spriterefresh()
    if time.time()-tmptime > 1: #CHANGE THIS TO 10 WHEN PLAYTESTING#
        break
        
GameStatus = "Character Select"

# Character Select

#Player1ChoiceText
Choicefont = pygame.font.Font("Bungee-Regular.ttf", 20)
P1Choicegraphics = Choicefont.render("Player 1 Chose:", 1, BLACK)

#Player2ChoiceText
Choicefont2 = pygame.font.Font("Bungee-Regular.ttf", 20)
P2Choicegraphics = Choicefont.render("Player 2 Chose:", 1, BLACK)
mframe = 6; ####MONK ANIMIMATION FRAME COUNT#####
dframe = 4; ####DO ANIMIMATION FRAME COUNT#####
sframe = 8; ####SALAH ANIMIMATION FRAME COUNT#####
nframe = 4; ####SUNNY ANIMIMATION FRAME COUNT#####
while GameStatus == "Character Select":
    stopMusic()
    gameWindow.fill(BLACK)
    #print(pygame.mouse.get_pos())
    mouseX, mouseY = pygame.mouse.get_pos()
    keys = pygame.mouse.get_pressed()
    pygame.event.clear()
    pygame.draw.rect(gameWindow, Char1Col, pygame.Rect(
        0, 0, 200, 800),  0)  # CharlSel1
    pygame.draw.rect(gameWindow, Char2Col, pygame.Rect(150, 0, 200, 800),  0)
# CharSel2
    pygame.draw.rect(gameWindow, Char3Col, pygame.Rect(300, 0, 200, 800),  0)
# CharSel3
    pygame.draw.rect(gameWindow, Char4Col, pygame.Rect(450, 0, 200, 800),  0)
    pygame.draw.rect(gameWindow, WHITE, pygame.Rect(0, 0, 600, 50),  0)
    gameWindow.blit(Choicegraphics, (5, 5))
    pygame.draw.rect(gameWindow, DispCol, pygame.Rect(0, 800, 100, 100),  0)
    pygame.draw.rect(gameWindow, ConfButtCol, pygame.Rect(0, 650, 600, 150),  0)
    gameWindow.blit(ConfButGraphics, (150, 710))
    gameWindow.blit(LogoP1, p1choicedisp)
    gameWindow.blit(LogoP2, p2choicedisp)
   #MONK IDLE CODE#
    mframe += 1
    if mframe > 6:
        mframe = 1
    Monk = pygame.image.load(f"Marcus Sprites/png/idle/Midle_{mframe}.png")
    Monk = pygame.transform.scale(Monk, (1200,550))
    gameWindow.blit(Monk, (-375, -100))

    #DO IDLE CODE#
    dframe += 1
    if dframe > 4:
        dframe = 1
    Do = pygame.image.load(f"Do_Idle_Frames/Didle{dframe}.png")
    Do = pygame.transform.scale(Do, (800,580))
    gameWindow.blit(Do, (-20, 55))

    #SALAH IDLE CODE#
    sframe += 1
    if sframe > 8:
        sframe = 1
    Salah = pygame.image.load(f"Salah/PNG/idle/idle_{sframe}.png")
    Salah = pygame.transform.scale(Salah, (1000,580))
    gameWindow.blit(Salah, (-430, -150))

    #SUNNY IDLE CODE#
    nframe += 1
    if nframe > 4:
        nframe = 1
    SunK = pygame.image.load(f"SunIdle/nidle{nframe}.png")
    SunK = pygame.transform.scale(SunK, (170,190))
    gameWindow.blit(SunK, (440, 250))
    if mouseY < 50:
        if keys[0]:
            print("Player Choices Reset")
            p1choice = 0
            p2choice = 0
            p1conf = False
            p2conf = False
            p1choicedisp = (-1000, -2000)
            p2choicedisp = (-1000, -2000)
    
    if mouseX < 150 and mouseY < 800 and mouseX > 5 and mouseY>50 and mouseY < 650:
        if keys[0]:
            print("SAL Zone Clicked")
            if p1conf == True:
                print("player 2 choice confirmed, SAL")
                p2conf = True
                p2choice = "Salah"
                p2choicedisp = (-180, 300)
            if p1conf == False:
                print("player 1 choice confirmed, SAL")
                p1conf = True
                p1choice = "Salah"
                p1choicedisp = (-180, 230)
    if mouseX < 300 and mouseX > 150 and mouseY < 800 and mouseY>50:
        #print("Green Zone")
        if keys[0]:
            print("MAR Zone Clicked")
            if p1conf == True:
                print("player 2 choice confirmed, MAR")
                p2conf = True
                p2choice = "Marcus"
                p2choicedisp = (-20, 300)
            if p1conf == False:
                print("player 1 choice confirmed, MAR")
                p1conf = True
                p1choice = "Marcus"
                p1choicedisp = (-20, 230)
    if mouseX < 450 and mouseX > 300 and mouseY < 800 and mouseY>50:
        if keys[0]:
            print("DO Zone Clicked")
            if p1conf == True:
                print("player 2 choice confirmed, DO")
                p2conf = True
                p2choice = "Mr Do"
                p2choicedisp = (125, 300)
            if p1conf == False:
                print("player 1 choice confirmed, DO")
                p1conf = True
                p1choice = "Mr Do"
                p1choicedisp = (125, 230)

    if mouseX < 600 and mouseX > 450 and mouseY < 800 and mouseY>50 and mouseY < 650:
        if keys[0]:
            print("SUN Zone Clicked")
            if p1conf == True:
                print("player 2 choice confirmed, SUN")
                p2conf = True
                p2choice = "Sunny"
                p2choicedisp = (280, 300)
            if p1conf == False:
                print("player 1 choice confirmed, SUN")
                p1conf = True
                p1choice = "Sunny"
                p1choicedisp = (280, 230)

    if p1conf == True and p2conf == True:
        ConfButtCol = (235, 55, 49)
        if mouseY > 650:
            if keys[0]:
                ConfButtCol = (0,0,0)
                GameStatus = "Select Stage"
    pygame.display.update()
    pygame.time.delay(80)

plystgc = 0
bplyconf = False

#Stage 1 Code#
stg1 = pygame.image.load("stg1.png")

#Stage 2 Code#
stg2 = pygame.image.load("plc.png")

#Stage 3 Code#
stg3 = pygame.image.load("plc.png")

#PlayerChoiceClearText
pygame.font.init()
Choicefont = pygame.font.SysFont("Bungee-Regular.ttf", 30)
Choicegraphics = Choicefont.render("Click Here to Confirm Your Stage", 1, (0,0,0))

while GameStatus == "Select Stage":
   mouseX, mouseY = pygame.mouse.get_pos()
   #print(pygame.mouse.get_pos())
   keys = pygame.mouse.get_pressed()
   pygame.event.clear()
   gameWindow.fill ((0,0,0))
   mouseX, mouseY = pygame.mouse.get_pos()
   gameWindow.blit(stg1, (0, 0,))
   gameWindow.blit(stg2, (0, 200,))
   gameWindow.blit(stg3, (0, 400,))
   pygame.draw.rect(gameWindow, (235, 189, 91), pygame.Rect(0, 600, 600, 200),  0)  
   gameWindow.blit(Choicegraphics, (60, 650))
   pygame.display.update()
   pygame.time.delay(50)
   if mouseY < 200:
      if keys[0]:
        print("stg1 Clicked")
        plystgc = 1
   if mouseY > 200 and mouseY < 400:
      if keys[0]:
        print("stg2 Clicked")
        plystgc = 2
   if mouseY > 400 and mouseY < 600:
      if keys[0]:
        print("stg3 Clicked")
        plystgc = 3
   if mouseY >600:
      if keys[0]:
          if plystgc == 0:
            print("please select a stage first")
          else:
            print("Confirmed")
            bplyconf = True
    
   pygame.display.update()
   pygame.time.delay(80)

print("here")
pygame.quit()
exit()
