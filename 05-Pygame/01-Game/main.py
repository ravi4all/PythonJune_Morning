import pygame
import random

pygame.init()

height = 600
width = 800
white = 255,255,255
green = 0,255,0
brown = 139,69,19

screen = pygame.display.set_mode((width,height))

my_car = pygame.image.load("assets/my_car.png")
opp_1 = pygame.image.load("assets/car_1.png")
opp_2 = pygame.image.load("assets/car_2.png")
opp_3 = pygame.image.load("assets/car_3.png")
bg_1 = pygame.image.load("assets/road.png")
bg_2 = pygame.image.load("assets/road.png")

clock = pygame.time.Clock()
FPS = 20

bg_y = 0
move_bg = 20

car_x = (width/2)-38
car_y = height-150
move_car = 0

opp_x = random.randint((width/2)-200,width-100)
opp_y = -120;
move_opp_y = 25

bg2_y = -height

mainLoop = True
while mainLoop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_bg += 5
            elif event.key == pygame.K_LEFT:
                move_car -= 10
            elif event.key == pygame.K_RIGHT:
                move_car += 10
        if event.type == pygame.KEYUP:
            move_car = 0

    screen.fill(white)
    screen.blit(bg_1, [(width/2)-200, bg_y])
    screen.blit(bg_2, [(width/2)-200, bg2_y])

    pygame.draw.rect(screen, green, [0,0,130,height])
    pygame.draw.rect(screen, green, [width-130,0,130,height])

    pygame.draw.rect(screen,brown, [130,0,50,height])
    pygame.draw.rect(screen,brown, [width-180,0,50,height])

    screen.blit(my_car, [car_x, car_y])
    screen.blit(opp_1, [opp_x,opp_y])

    opp_rect = pygame.Rect(opp_x, opp_y, opp_1.get_width(), opp_1.get_height())
    my_rect = pygame.Rect(car_x, car_y, my_car.get_width(), my_car.get_height())

    if opp_rect.colliderect(my_rect):
        opp_x = random.randint((width/2)-200,400)
        opp_y = -120;

    bg_y += move_bg
    bg2_y += move_bg

    car_x += move_car

    opp_y += move_opp_y

    if bg_y > height:
        bg_y = -height
    elif bg2_y > height:
        bg2_y = -height
    elif opp_y > height:
        opp_x = random.randint((width/2)-200,400)
        opp_y = -120;

    pygame.display.update()
    clock.tick(FPS)