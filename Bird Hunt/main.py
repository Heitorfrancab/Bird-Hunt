from codecs import BOM_BE
import pygame, random, sys


pygame.init()
screen = pygame.display.set_mode((540, 480)) # configura janela do jogo
clock = pygame.time.Clock()

pygame.font.init()
my_font = pygame.font.SysFont('Assets/font.ttf', 40)
menu_font = pygame.font.SysFont('Assets/font.ttf', 98)

def menu():
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
        pygame.display.flip() # Desenha o quadro atual na tela
        clock.tick(60)
def game():
    for num in range(1, 50):
        if num % 10 == 0:
            bombexplosion = pygame.image.load(f"Assets/Explosion{int(num/10)}.png")
        if num == 50:
            xexplosion = 700

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

    kills = 0

    counterduck = 0
    counterdeadduck = 0
    timerdeadduck1 = 0
    timerdeadduck2 = 0
    timerdeadduck3 = 0

    enemy = duck1

    deadenemy = dead_duck1
    deadenemy2 = dead_duck1
    deadenemy3 = dead_duck1

    pygame.mouse.set_visible(False)
    cursor_img = pygame.image.load("Assets/Novo Projeto(1).png")
    cursor_img = cursor_img.convert_alpha()
    cursor_img_rect = cursor_img.get_rect()

    while running:
        cursor_img_rect.center = pygame.mouse.get_pos()  # update position 

        text_surface = my_font.render(str(kills), False, (0, 0, 0))

        timerdeadduck1 = timerdeadduck1 + 1
        timerdeadduck2 = timerdeadduck2 + 1
        timerdeadduck3 = timerdeadduck3 + 1

        counterduck = counterduck + 1

        x = x + v

        x1 = x1 + v

        y2 = y2 + v

        y3 = y3 + v

        y4 = y4 + v

        if counterduck == 10:
            if enemy == duck1:
                enemy = duck2
                counterduck = 0
            elif enemy == duck2:
                enemy = duck3
                counterduck = 0
            elif enemy == duck3:
                enemy = duck1
                counterduck = 0

        if timerdeadduck1 == 15:
            deadenemy = dead_duck2
        if timerdeadduck2 == 15:
            deadenemy2 = dead_duck2
        if timerdeadduck3 == 15:
            deadenemy3 = dead_duck2

        bomb = dynamite

        bombpos = bomb.get_rect(topleft = (x1, y1))
        enemypos = enemy.get_rect(topleft = (x, y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bombpos.collidepoint(event.pos):
                    kills = kills - 5
                    xexplosion = x1
                    yexplosion = y1
                    x1 = 700
                    y1 = random.randrange(0, 300)
                    for num in range(1, 50):
                        if num % 10 == 0:
                            bombexplosion = pygame.image.load(f"Assets/Explosion{int(num/10)}.png")
                        if num == 50:
                            xexplosion = 700

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
        screen.blit(cursor_img, cursor_img_rect) # draw the cursor
        screen.blit(enemy, (x, y)) # desenha figura sobre o quadro atual nas coordenadas indicadas
        screen.blit(bomb, (x1, y1))
        screen.blit(bombexplosion, (xexplosion, yexplosion))
        screen.blit(text_surface, (0,0))
        pygame.display.flip() # Desenha o quadro atual na tela
        clock.tick(60)

menu()

pygame.quit()