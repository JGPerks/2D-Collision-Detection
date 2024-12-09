import pygame
import pygame.math as math
import random


class Particle:

    def __init__(self, surface, pos):
        self.surface = surface
        self.pos = pos
        self.velocity = math.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))  # Temporary
        self.acceleration = (0.01, 0.01)
        self.radius = 5

    def draw(self):
        self.pos += self.velocity
        self.pos += self.acceleration
        pygame.draw.circle(self.surface, "white", (self.pos.x, self.pos.y), self.radius, 0)

    def detect_window(self):
        """Keeps particles in bounds of window"""
        if self.pos.x > 1280 or self.pos.x < 0:
            self.velocity.x *= -1
        if self.pos.y > 720 or self.pos.y < 0:
            self.velocity.y *= -1

    def collision_detection(self, other):
        """Checks if a particle is colliding with another. If so it is handled so it no longer collides."""
        distance = (pow((self.pos.x - other.pos.x), 2) + pow(self.pos.y - other.pos.y, 2))**0.5

        if distance < self.radius + other.radius:  # There are better ways to handle this, but will update later
            self.velocity *= -1
            other.velocity *= -1
