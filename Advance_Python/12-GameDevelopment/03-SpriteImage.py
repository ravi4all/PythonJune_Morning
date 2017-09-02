# Pygame template - skeleton for a new pygame project
import pygame
import random
import os

WIDTH = 800
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

game_folder = os.path.dirname(__file__)
# print(game_folder)
img_folder = os.path.join(game_folder,'assets')
# print(img_folder)
# use convert(), which will speed up Pygame’s drawing by converting the image into a format that will be faster to draw on the screen.
player_img = pygame.image.load(os.path.join(img_folder,'image_1.png')).convert()

# player_img = pygame.image.load("assets/image_1.png")

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

    def update(self):
        self.rect.x += 5

        if self.rect.x > WIDTH:
            self.rect.right = 0

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
