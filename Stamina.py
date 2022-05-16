import pygame
import time

PERIOD = 3
referenceTime = time.time()
elapsed = 0
triggered = False
print("Press the space bar to emulate a move cooldown")
clock = pygame.time.Clock()
FPS = 24
loadtimer = True
while loadtimer:
    pygame.event.clear()    
    clock.tick(FPS)
     
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        triggered = True
        referenceTime = time.time() 
    if triggered:
        print(elapsed)
        elapsed = round(time.time() - referenceTime, 1)
        if elapsed > PERIOD:
            print("Cooldown Over")
            loadtimer = False