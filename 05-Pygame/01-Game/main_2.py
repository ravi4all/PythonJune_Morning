import pygame
import random

pygame.init()
pygame.mixer.init()

height = 600
width = 800
white = 255,255,255
green = 0,255,0
brown = 139,69,19
red = 255,0,0

screen = pygame.display.set_mode((width,height))

my_car = pygame.image.load("assets/my_car.png")
opp_1 = pygame.image.load("assets/car_1.png")
opp_2 = pygame.image.load("assets/car_2.png")
cop_car = pygame.image.load("assets/car_3.png")
bg_1 = pygame.image.load("assets/road.png")
bg_2 = pygame.image.load("assets/road.png")
busted_image = pygame.image.load("assets/busted.png")
home_bg = pygame.image.load("assets/home_bg_image.jpg")

bg_music = pygame.mixer.Sound("assets/audio_gt.wav")
police_music = pygame.mixer.Sound("assets/police_horn.wav")

bg_music.play(-1)
police_music.play(-1)

clock = pygame.time.Clock()
FPS = 20

def gameIntro():
    font_1 = pygame.font.SysFont("Arcade",100)
    text_1 = font_1.render("Police Chase",True,red)
    font_2 = pygame.font.SysFont("None",50)
    text_2 = font_2.render("Press S to start or Q to quit", True, red)
    gameIntro = False
    while not gameIntro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    main()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        screen.fill(white)
        screen.blit(home_bg, (0,100))
        screen.blit(text_1,(250,0))
        screen.blit(text_2, (200, 130))

        pygame.display.update()

def gameOver():
    font_1 = pygame.font.SysFont("Arcade",100)
    text_1 = font_1.render("Game Over",True,red)
    font_2 = pygame.font.SysFont("None",50)
    text_2 = font_2.render("Press C to continue or B to go back", True, red)
    gameOver = False
    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    main()
                elif event.key == pygame.K_b:
                    gameIntro()

        screen.blit(text_1,(250,0))
        screen.blit(text_2, (200, 130))

        pygame.display.update()


def car(car_x, car_y):

    if car_hit == True:
        car_direction = pygame.transform.rotate(my_car,-60)
    else:
        car_direction = pygame.transform.rotate(my_car,0)

    screen.blit(car_direction, [car_x, car_y])

def cops(cop_x,cop_y):

    screen.blit(cop_car, [cop_x,cop_y])

def busted():

    screen.blit(busted_image, (250,250))
    pygame.display.update()

def counter(c):
    font = pygame.font.SysFont("Arcade",40)
    text = font.render("Car Passed : "+ str(c),True,red)
    screen.blit(text, (50,10))

def main():

    count = 0

    bg_y = 0
    move_bg = 20

    car_x = (width/2)-38
    car_y = height-150
    move_car = 0
    global car_hit
    car_hit = False

    cop_x = random.randint((width/2)-200,width-200)
    cop_y = -height
    move_cop_y = 18

    opp_x = random.randint((width/2)-200,width-200)
    opp_y = -120
    move_opp_y = 18

    bg2_y = -height

    mainLoop = False
    while not mainLoop:

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

        screen.blit(opp_1, [opp_x,opp_y])

        opp_rect = pygame.Rect(opp_x, opp_y, opp_1.get_width(), opp_1.get_height())
        cop_rect = pygame.Rect(cop_x, cop_y, cop_car.get_width(), cop_car.get_height())
        my_rect = pygame.Rect(car_x, car_y, my_car.get_width(), my_car.get_height())

        bg_y += move_bg
        bg2_y += move_bg

        car_x += move_car

        opp_y += move_opp_y

        cop_y += move_cop_y

        car(car_x,car_y)
        cops(cop_x,cop_y)
        counter(count)

        if bg_y > height:
            bg_y = -height
        elif bg2_y > height:
            bg2_y = -height
        elif opp_y > height:
            opp_x = random.randint((width/2)-200,400)
            opp_y = -120
            count += 1
        elif cop_y > height:
            cop_x = random.randint((width/2)-200,width-200)
            cop_y = -height


        if opp_rect.colliderect(my_rect):
            gameOver()

        if cop_rect.colliderect(my_rect):
            car_hit = True
            move_car = +10
            busted()
            gameOver()
        elif car_x > width-220:
            move_car = 0
            gameOver()

        pygame.display.update()
        clock.tick(FPS)

gameIntro()