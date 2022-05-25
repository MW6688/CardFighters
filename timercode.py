#############TIMERCODE###########
PERIOD = 3
referenceTime = time.time()
elapsed = 0
triggered = False
print("Press the space bar if you dare!")
clock = pygame.time.Clock()
FPS = 24
loadtimer = True
while loadtimer:
    pygame.event.clear()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            triggered = True
            referenceTime = time.time()     # set reference time when the period is triggered

    if triggered:
        print(elapsed)
        elapsed = round(time.time() - referenceTime, 1)
        if elapsed > PERIOD:
            print("KABOOM!!")
            loadtimer = False
            break

###########TIMERCODE################