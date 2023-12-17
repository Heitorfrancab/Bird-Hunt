import pygame
import random

pygame.init()
screen = pygame.display.set_mode((540, 480)) # configura janela do jogo
clock = pygame.time.Clock()
running = True
x = 0
v = 6
y = random.randrange(0,300)

bg = pygame.image.load('Novo Projeto.png')

duck1 = pygame.image.load('duck1.png')
duck1 = duck1.convert_alpha()

duck2 = pygame.image.load('duck2.png')
duck2 = duck2.convert_alpha()

duck3 = pygame.image.load('duck3.png')
duck3 = duck3.convert_alpha()

kills = 0

contadorduck = 0

inimigo = duck1

while running:

    contadorduck = contadorduck + 1

    x = x + v

    if contadorduck == 10:
        if inimigo == duck1:
            inimigo = duck2
            contadorduck = 0
        elif inimigo == duck2:
            inimigo = duck3
            contadorduck = 0
        elif inimigo == duck3:
            inimigo = duck1
            contadorduck = 0

    inimigopos = inimigo.get_rect(topleft = (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if inimigopos.collidepoint(event.pos):
                print('colis')
                y = random.randrange(0,300)
                x = 0
                kills = kills + 1

    if inimigopos.left == 540:
        y = random.randrange(0,300)
        x = 0 

    screen.blit(bg, (0, 0))
    screen.blit(inimigo, (x, y)) # desenha figura sobre o quadro atual nas coordenadas indicadas
    pygame.display.flip() # Desenha o quadro atual na tela
    clock.tick(60)

pygame.quit()
