import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Movement")


player_x = 400
player_y = 300
vel_x = 0
vel_y = 0
accel_speed = 5 # Acceleration
friction = 0.8
player_size = 50
crap_count = 0

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if pygame.key.get_pressed()[pygame.K_f]:
        screen.fill((130, 30, 130))
        crap_count += 1
        print("press frames: ",crap_count)
    else:
        crap_count = 0


    if keys[pygame.K_a] or keys[pygame.K_LEFT] :
        vel_x -= accel_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        vel_x += accel_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        vel_y -= accel_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        vel_y += accel_speed


    # Apply friction (slows down over time)
    vel_x *= friction
    vel_y *= friction

    player_x += vel_x
    player_y += vel_y

    # Prevent going off screen
    player_x = max(0, min(player_x, 800 - player_size))
    player_y = max(0, min(player_y, 600 - player_size))

    
    print(f'X: {int(player_x)}, Y: {int(player_y)}')



    screen.fill((30, 130, 130))
    pygame.draw.rect(screen, "Green", (player_x, player_y, player_size, player_size))
    pygame.display.flip()


pygame.quit()

