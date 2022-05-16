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
Char1Col = (255, 0, 0)
Char2Col = (0, 255, 0)
Char3Col = (0, 0, 255)
Char4Col = (255, 234, 0)
elapsed = 0
triggered = False
PERIOD = 3
FPS = 24
# sample change 2
###Loading and Defining Variables (loading)###
pygame.display.set_caption("CardFighters")
pygame.font.init()
font = pygame.font.SysFont("comicsans", 60)
loadinggraphics = font.render("Loading...", 1, WHITE)

gameWindow = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()
ground = gameWindow.get_height() * 3 // 4


def startloadMusic():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.mixer.music.load("Capyvibe.mp3")
    pygame.mixer.music.play(-1)


def startMenuMusic():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.mixer.music.load("Smash.mp3")
    pygame.mixer.music.play(-1)


def stopMusic():
    pygame.mixer.stop()


# Title Code
Titlefont = pygame.font.SysFont("Times New Roman", 30)
Titlegraphics = Titlefont.render("X x Left Click To Start x X", 1, TitleColor)

#GameTitlePNG#
GameTitle = pygame.image.load('CardFighters Title.png')

# Menubackground
Menubackground = pygame.image.load("MenuBackground.png")


GameStatus = "Menu"


def PrintStatus():
    print("Now in "+GameStatus + " Stage")


while GameStatus == "Menu":
    gameWindow.blit(Menubackground, (0, 0))
    gameWindow.blit(GameTitle, (60, -100))
    gameWindow.blit(Titlegraphics, (115, 280))
    startMenuMusic
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

while GameStatus == "Loading":
    startloadMusic()
    clock.tick(20)
    all_sprites.update()

    gameWindow.fill((255, 134, 69), (0, 0, gameWindow.get_width(), ground))
    gameWindow.fill((255, 127, 64),
                    (0, ground, gameWindow.get_width(), gameWindow.get_height() - ground))
    all_sprites.draw(gameWindow)
    pygame.display.flip()

    gameWindow.blit(loadinggraphics, (180, 100))
    print(elapsed)
    pygame.event.clear()

    pygame.display.update()


while GameStatus == "Character Select":
    print(pygame.mouse.get_pos())
    mouseX, mouseY = pygame.mouse.get_pos()
    pygame.event.clear()
    pygame.draw.rect(gameWindow, Char1Col, pygame.Rect(
        0, 0, 200, 600),  0)  # CharlSel1
    pygame.draw.rect(gameWindow, Char2Col, pygame.Rect(150, 0, 200, 600),  0)
# CharSel2
    pygame.draw.rect(gameWindow, Char3Col, pygame.Rect(300, 0, 200, 600),  0)
# CharSel3
    pygame.draw.rect(gameWindow, Char4Col, pygame.Rect(450, 0, 200, 600),  0)
# CharSel4
    if mouseX < 150 and mouseY < 600 and mouseX > 5:
        print("Red Zone")
        Char1Col = (255, 81, 83)
        Char2Col = (0, 255, 0)
        Char3Col = (0, 0, 255)
        Char4Col = (255, 234, 0)
    if mouseX < 300 and mouseX > 150 and mouseY < 600:
        print("Green Zone")
        Char1Col = (255, 0, 0)
        Char2Col = (129, 250, 127)
        Char3Col = (0, 0, 255)
        Char4Col = (255, 234, 0)
    if mouseX < 450 and mouseX > 300 and mouseY < 600:
        print("Blue Zone")
        Char1Col = (255, 0, 0)
        Char2Col = (0, 255, 0)
        Char3Col = (96, 108, 250)
        Char4Col = (255, 234, 0)
    if mouseX < 600 and mouseX > 450 and mouseY < 600:
        print("Yellow Zone")
        Char1Col = (255, 0, 0)
        Char2Col = (0, 255, 0)
        Char3Col = (0, 0, 255)
        Char4Col = (255, 254, 76)
    pygame.display.update()
    pygame.time.delay(80)


print("here")
pygame.quit()
exit()
