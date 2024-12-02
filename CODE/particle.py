import pygame
import random


class Particle:

    def __init__(self, surface, pos):
        self.surface = surface
        self.pos = pos
        self.velocity = random.uniform(1, 2)  # Temporary until I add cartesian coordinates
        self.acceleration = 1

    def draw(self):
        self.pos.x += self.velocity
        self.pos.y += self.velocity
        pygame.draw.circle(self.surface, "white", (self.pos.x, self.pos.y), 3, 0)

    def detect_collision(self):
        """Keeps particles in bounds of window"""
        if self.pos.x > 1280:
            self.pos.x = self.pos.x - self.pos.x
        if self.pos.x < 0:
            self.pos.x = self.pos.x + 1280

        if self.pos.y > 720 or self.pos.y < 0:
            self.pos.y = self.pos.y - self.pos.y
        if self.pos.y < 0:
            self.pos.y = self.pos.y + 720
