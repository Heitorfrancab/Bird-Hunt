import pygame, random, sys # imports all the necessary libraries 

pygame.init() # initialize pygame
screen = pygame.display.set_mode((540, 480)) # sets the game screen
clock = pygame.time.Clock()

pygame.font.init() # initialize pygame fonts
my_font = pygame.font.SysFont('Assets/font.ttf', 40)
menu_font = pygame.font.SysFont('Assets/font.ttf', 98)

def menu(): # creates the main menu screen
    pygame.display.set_caption("Bird Hunt - Menu")
    running = True

    while running:
        menutext = menu_font.render("Bird Hunt", True, ("White"))
        menurect = menutext.get_rect(center = (270, 50))

        Bg = pygame.image.load("Assets/Background.png")
        Bgrect = Bg.get_rect(center = (270, 240))

        playbg = pygame.image.load("Assets/Button Rect.png")
        playrect = playbg.get_rect(center = (270, 200))
        playtext = menu_font.render("Play", True, (0, 0, 0))
        playtextrect = playtext.get_rect(center = (270, 200))

        quitbg = pygame.image.load("Assets/Button Rect.png")
        quitrect = quitbg.get_rect(center = (270, 350))
        quittext = menu_font.render("Quit", True, (0, 0, 0))
        quittextrect = quittext.get_rect(center = (270, 350))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if playrect.collidepoint(event.pos):
                    game()
                elif quitrect.collidepoint(event.pos):
                    running = False
    
        screen.blit(Bg, Bgrect)
        screen.blit(menutext, menurect)
        screen.blit(quitbg, quitrect)
        screen.blit(quittext, quittextrect)
        screen.blit(playbg, playrect)
        screen.blit(playtext, playtextrect)
        pygame.display.flip() # puts the current frame on the screen
        clock.tick(60)
def game(): # creates the main game screen
    pygame.display.set_caption("Bird Hunt - Play")
    running = True
    x = 0
    x1 = 540
    x2 = 0
    x3 = 0
    x4 = 0
    xexplosion = 700
    v = 6
    y = random.randrange(0,300)
    y1 = random.randrange(0,300)
    y2 = 480
    y3 = 480
    y4 = 480
    yexplosion = 0

    bg = pygame.image.load('Assets/Novo Projeto.png')

    duck1 = pygame.image.load('Assets/duck1.png')
    duck1 = duck1.convert_alpha()

    duck2 = pygame.image.load('Assets/duck2.png')
    duck2 = duck2.convert_alpha()

    duck3 = pygame.image.load('Assets/duck3.png')
    duck3 = duck3.convert_alpha()

    dead_duck1 = pygame.image.load("Assets/dead_duck.png")
    dead_duck1 = dead_duck1.convert_alpha()

    dead_duck2 = pygame.image.load("Assets/falling_duck.png")
    dead_duck2 = dead_duck2.convert_alpha()

    dynamite = pygame.image.load("Assets/dynamite.png")
    dynamite = dynamite.convert_alpha()

    explosion1 = pygame.image.load("Assets/Explosion1.png")
    explosion1 = explosion1.convert_alpha()
    pygame.transform.scale(explosion1, (256, 256))
    explosion2 = pygame.image.load("Assets/Explosion2.png")
    explosion2 = explosion2.convert_alpha()
    pygame.transform.scale(explosion2, (256, 256))
    explosion3 = pygame.image.load("Assets/Explosion3.png")
    explosion3 = explosion3.convert_alpha()
    pygame.transform.scale(explosion3, (256, 256))
    explosion4 = pygame.image.load("Assets/Explosion4.png")
    explosion4 = explosion4.convert_alpha()
    pygame.transform.scale(explosion4, (256, 256))
    explosion5 = pygame.image.load("Assets/Explosion5.png")
    explosion5 = explosion5.convert_alpha()
    pygame.transform.scale(explosion5, (256, 256))

    kills = 0

    counterduck = 0
    counterdeadduck = 0
    timerdeadduck1 = 0
    timerdeadduck2 = 0
    timerdeadduck3 = 0
    timerexplosion = 0

    enemy = duck1
    explosion = explosion1

    deadenemy = dead_duck1
    deadenemy2 = dead_duck1
    deadenemy3 = dead_duck1

    pygame.mouse.set_visible(False)
    cursor_img = pygame.image.load("Assets/Novo Projeto(1).png")
    cursor_img = cursor_img.convert_alpha()
    cursor_img_rect = cursor_img.get_rect()

    while running:
        cursor_img_rect.center = pygame.mouse.get_pos()  # update mouse position 

        text_surface = my_font.render(str(kills), False, (0, 0, 0)) # writes the pontuation down on screen

        timerdeadduck1 = timerdeadduck1 + 1 # updates the first dead duck's sprites timer
        timerdeadduck2 = timerdeadduck2 + 1 # updates the second dead duck's sprites timer
        timerdeadduck3 = timerdeadduck3 + 1 # updates the third dead duck's sprites timer
        timerexplosion = timerexplosion + 1 # updates the explosion's timer 

        counterduck = counterduck + 1 # updates the counter that "selects" the duck sprite

        x = x + v # updates the horizontal position of the alive duck

        x1 = x1 + v # updates the horizontal position of the bomb

        y2 = y2 + v # updates the horizontal position of the first dead duck

        y3 = y3 + v # updates the horizontal position of the second dead duck

        y4 = y4 + v # updates the horizontal position of the third dead duck

        if counterduck == 10: # "selects" the alive duck sprite
            if enemy == duck1:
                enemy = duck2
                counterduck = 0
            elif enemy == duck2:
                enemy = duck3
                counterduck = 0
            elif enemy == duck3:
                enemy = duck1
                counterduck = 0

        # updates the dead duck sprite
        if timerdeadduck1 == 15:
            deadenemy = dead_duck2
        if timerdeadduck2 == 15:
            deadenemy2 = dead_duck2
        if timerdeadduck3 == 15:
            deadenemy3 = dead_duck2

        # updates the explosion sprite
        if timerexplosion == 0:
            explosion = explosion1
        if timerexplosion == 5:
            explosion = explosion2
        if timerexplosion == 10:
            explosion = explosion3
        if timerexplosion == 15:
            explosion = explosion4
        if timerexplosion == 20:
            explosion = explosion5
        if timerexplosion == 25:
            xexplosion = 700
            timerexplosion = 0
        
        bomb = dynamite

        bombpos = bomb.get_rect(topleft = (x1, y1))
        enemypos = enemy.get_rect(topleft = (x, y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bombpos.collidepoint(event.pos):
                    timerexplosion = 0
                    kills = kills - 5
                    xexplosion = x1
                    yexplosion = y1
                    x1 = 700
                    y1 = random.randrange(0, 300)
                if enemypos.collidepoint(event.pos):
                    spawn_rate = random.randrange(0, 10)
                    print(spawn_rate)
                    if spawn_rate == 9:
                        x1 = 0
                        y1 = random.randrange(0, 300)
                    if counterdeadduck == 0:
                        timerdeadduck1 = 0
                        deadenemy = dead_duck1
                        y2 = y
                        x2 = x
                        counterdeadduck = counterdeadduck + 1
                    elif counterdeadduck == 1:
                        timerdeadduck2 = 0
                        deadenemy2 = dead_duck1
                        y3 = y
                        x3 = x
                        counterdeadduck = counterdeadduck + 1
                    elif counterdeadduck == 2:
                        timerdeadduck3 = 0
                        deadenemy3 = dead_duck1
                        y4 = y
                        x4 = x
                        counterdeadduck = 0
                    y = random.randrange(0,300)
                    x = 0
                    kills = kills + 1

        if enemypos.left == 540:
            y = random.randrange(0,300)
            x = 0 

        screen.blit(bg, (0, 0))
        screen.blit(deadenemy, (x2, y2))
        screen.blit(deadenemy2, (x3, y3))
        screen.blit(deadenemy3, (x4, y4))
        screen.blit(cursor_img, cursor_img_rect)
        screen.blit(enemy, (x, y)) 
        screen.blit(bomb, (x1, y1))
        screen.blit(explosion, (xexplosion, yexplosion))
        screen.blit(text_surface, (0,0))
        pygame.display.flip()
        clock.tick(60)

menu() # runs the main menu screen

pygame.quit()