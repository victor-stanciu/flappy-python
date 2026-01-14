import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Movement")


player_x = 400
player_y = 300
player_speed = 0.5
crap_count = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if pygame.key.get_pressed()[pygame.K_f]:
        screen.fill((130, 30, 130))
        crap_count += 1
        print("crap count: ",crap_count)
    else:
        crap_count = 0


    if keys[pygame.K_a] or keys[pygame.K_LEFT] :
        player_x -= player_speed
        print(f"X: {player_x}, Y: {player_y}")
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed
        print(f"X: {player_x}, Y: {player_y}")
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= player_speed
        print(f"X: {player_x}, Y: {player_y}")
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += player_speed
        print(f"X: {player_x}, Y: {player_y}")

    screen.fill((30, 130, 130))
    pygame.draw.rect(screen, "Red", (player_x, player_y, 50, 50))
    pygame.display.flip()


pygame.quit()

