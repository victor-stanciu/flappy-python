import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("First game")

player = pygame.Rect((300, 250, 50, 50))
running = True


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 130, 130))

    pygame.display.flip()

pygame.quit()

