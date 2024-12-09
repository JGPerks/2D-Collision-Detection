# Example file showing a basic pygame "game loop"
import pygame
import pygame.math as math
import random
import time

from CODE.particle import Particle

# pygame setup
pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Collision Detection")
clock = pygame.time.Clock()
running = True

particle = [0] * 100
# Initialize 100 particles with random (x, y) vector within the bounds of the window
for i in range(len(particle)-1):
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
    for i in range(len(particle)-1):
        particle[i].draw()  # Draws particles updated location each frame
        particle[i].detect_window()  # Each frame checks if it leaves window bounds
        start_time = time.time()
        for k in range(len(particle)-1):
            if k != i:  # Checks particle against every other particle for a collision and handles it
                particle[i].collision_detection(particle[k])
        end_time = time.time()

        elapsed_time = end_time - start_time
        print("Elapsed time: " + str(elapsed_time) + " seconds")

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
