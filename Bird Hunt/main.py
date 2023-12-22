import pygame
import random

pygame.init()
screen = pygame.display.set_mode((540, 480)) # configura janela do jogo
clock = pygame.time.Clock()
running = True
x = 0
x2 = 0
x3 = 0
x4 = 0
v = 6
y = random.randrange(0,300)
y2 = 480
y3 = 480
y4 = 480

bg = pygame.image.load('Novo Projeto.png')

duck1 = pygame.image.load('duck1.png')
duck1 = duck1.convert_alpha()

duck2 = pygame.image.load('duck2.png')
duck2 = duck2.convert_alpha()

duck3 = pygame.image.load('duck3.png')
duck3 = duck3.convert_alpha()

dead_duck1 = pygame.image.load("dead_duck.png")
dead_duck1 = dead_duck1.convert_alpha()

dead_duck2 = pygame.image.load("falling_duck.png")
dead_duck2 = dead_duck2.convert_alpha()

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
cursor_img = pygame.image.load("Novo Projeto(1).png")
cursor_img = cursor_img.convert_alpha()
cursor_img_rect = cursor_img.get_rect()

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

while running:
    cursor_img_rect.center = pygame.mouse.get_pos()  # update position 

    text_surface = my_font.render(str(kills), False, (0, 0, 0))

    timerdeadduck1 = timerdeadduck1 + 1
    timerdeadduck2 = timerdeadduck2 + 1
    timerdeadduck3 = timerdeadduck3 + 1

    counterduck = counterduck + 1

    x = x + v

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

    enemypos = enemy.get_rect(topleft = (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if enemypos.collidepoint(event.pos):
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
    screen.blit(text_surface, (0,0))
    pygame.display.flip() # Desenha o quadro atual na tela
    clock.tick(60)

pygame.quit()