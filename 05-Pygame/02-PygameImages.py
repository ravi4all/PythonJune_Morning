import pygame

pygame.init()

width = 1000
height = 600

screen = pygame.display.set_mode((width,height))

red = 255,0,0
x = 0
y = 0
move_x = 10
move_y = 10

img = pygame.image.load("ball.jpg")

clock = pygame.time.Clock()
FPS = 40

while True:

    for event in pygame.event.get():
        pass
        #print(event)
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         move_x = +5
        #     elif event.key == pygame.K_DOWN:
        #         move_y = +5
        #     if event.key == pygame.K_LEFT:
        #         move_x = -5
        #     elif event.key == pygame.K_UP:
        #         move_y = -5

    screen.fill((255,255,255))
    screen.blit(img,(x,y))

    x += move_x
    y += move_y

    if x > width - img.get_width():
        move_x = -10
    elif x < 0:
        move_x = +10
    elif y > height - img.get_height():
        move_y = -10
    elif y < 0:
        move_y = +10

    pygame.display.update()
    clock.tick(FPS)

quit()
