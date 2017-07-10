import pygame

pygame.init()

screen = pygame.display.set_mode((800,500))

red = 255,0,0
x = 0
y = 0
move_x = 0
move_y = 0

img = pygame.image.load("car_1.png")

clock = pygame.time.Clock()
FPS = 40

rotate = False

rotation = 0

clock = pygame.time.Clock()
FPS = 12


def rotateCar():
    if rotate == True:
        r = pygame.transform.rotate(img, rotation)
    else:
        r = pygame.transform.rotate(img, 0)

    screen.blit(r,(100,100))

while True:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            rotation += 10
            rotate = True
        # if event.type == pygame.KEYUP:
        #     rotation = 0

    screen.fill((255,255,255))

    x += move_x
    y += move_y

    rotateCar()

    pygame.display.update()
    clock.tick(FPS)

quit()
