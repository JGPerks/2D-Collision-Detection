# Example file showing a basic pygame "game loop"
import pygame
import pygame.math as math
import random
import time

from CODE.particle import Particle
from CODE.quadtree import *


def draw_quadtree(screen, quadtree):
    """Draw the quadtree and its points. Only draw boundaries if subdivided."""
    if quadtree.divided:
        pygame.draw.rect(screen, "white",
                         (quadtree.boundary.x, quadtree.boundary.y, quadtree.boundary.width, quadtree.boundary.height),
                         1)
        draw_quadtree(screen, quadtree.northeast)
        draw_quadtree(screen, quadtree.northwest)
        draw_quadtree(screen, quadtree.southeast)
        draw_quadtree(screen, quadtree.southwest)
    else:
        for point in quadtree.points:
            pygame.draw.circle(screen, "red", (int(point.pos.x), int(point.pos.y)), int(point.radius), 0)


def main():
    # pygame setup
    pygame.init()

    width = 1280
    height = 720
    boundary = Rectangle(0, 0, width, height)
    qt = Quadtree(boundary, 10)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Collision Detection")
    clock = pygame.time.Clock()
    running = True

    particles = []
    # Initialize 100 particles with random (x, y) vector within the bounds of the window
    for i in range(50):
        vector = math.Vector2(i * 100 % width, (i * 150 % height))  # Using % to equally space particles upon creation
        particles.append(Particle(screen, vector))

    while running:
        # fills the screen with a color to wipe away anything from last frame
        screen.fill("black")

        for particle in particles:
            qt.insert(particle)
            particle.detect_window()
            particle.draw()

        draw_quadtree(screen, qt)

        # Game Loop / collision detection post-quadtree implementation
        for particle in particles:
            query_range = Rectangle(particle.pos.x - 50, particle.pos.y - 50, 100, 100)
            nearby_particles = qt.query(query_range)
            for other in nearby_particles:
                if particle != other:
                    particle.collision_detection(other)
        # Game Loop / collision detection pre-quadtree implementation
        """for i in query_range(len(particle)):
            particle[i].draw()  # Draws particles updated location each frame
            particle[i].detect_window()  # Each frame checks if it leaves window bounds
            start_time = time.time()
            for k in query_range(len(particle)):
                if k != i:  # Checks particle against every other particle for a collision and handles it
                    particle[i].collision_detection(particle[k])
            end_time = time.time()
    
            elapsed_time = end_time - start_time
            print("Elapsed time: " + str(elapsed_time) + " seconds")"""

        # pygame.QUIT event means the user clicked X to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # flip() the display to put your work on screen
        pygame.display.flip()

        # Prune empty regions of the quadtree to keep it balanced
        qt.prune()
        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    main()
