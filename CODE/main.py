# Example file showing a basic pygame "game loop"
import pygame
import pygame.math as math
import random

from CODE.particle import Particle

# pygame setup
pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

particle = [0] * 100
# Initialize 100 particles with random (x, y) vector within the bounds of the window
for i in range(99):
    vector = math.Vector2(random.randint(0, width), random.randint(0, height))
    particle[i] = Particle(screen, vector)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fills the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER / Game Loop
    for i in range(99):
        particle[i].draw()
        particle[i].detect_collision()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
