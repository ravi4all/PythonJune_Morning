import pygame

pygame.init()

screen = pygame.display.set_mode((800,500))

red = 255,0,0
x = 0
y = 0
move_x = 0
move_y = 0

img = pygame.image.load("ball.jpg")

clock = pygame.time.Clock()
FPS = 40

while True:

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = +5
            elif event.key == pygame.K_DOWN:
                move_y = +5
            if event.key == pygame.K_LEFT:
                move_x = -5
            elif event.key == pygame.K_UP:
                move_y = -5



    screen.fill((255,255,255))
    pygame.draw.rect(screen,red,[x,y,50,50])
    screen.blit(img,(10,10))

    x += move_x
    y += move_y

    pygame.display.update()
    clock.tick(FPS)

quit()
