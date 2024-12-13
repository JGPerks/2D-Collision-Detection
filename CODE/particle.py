import pygame
import pygame.math as math
import random


class Particle:

    def __init__(self, surface, pos):
        self.surface = surface
        self.pos = math.Vector2(pos)
        self.velocity = math.Vector2(random.randint(-3, 3), random.uniform(-3, 3))
        self.acceleration = math.Vector2(0, 0)
        self.mass = random.uniform(2.3, 3)
        self.radius = (self.mass**2)

    def draw(self):
        self.velocity += self.acceleration
        self.pos += self.velocity
        self.acceleration * 0
        pygame.draw.circle(self.surface, "white", (self.pos.x, self.pos.y), self.radius, 0)

    def detect_window(self):
        """Keeps particles in bounds of window"""
        if self.pos.x > 1280 or self.pos.x < 0:
            self.velocity.x *= -1
        if self.pos.y > 720 or self.pos.y < 0:
            self.velocity.y *= -1

    def collision_detection(self, other):
        """Checks if a particle is colliding with another. If so it is handled so it no longer collides."""
        impact_vector = math.Vector2.__sub__(other.pos, self.pos)
        distance = impact_vector.magnitude()

        if distance < self.radius + other.radius:
            # Math for collision handling w/ elastic collisions
            overlap = distance - (self.radius + other.radius)
            direction = impact_vector.copy() * (overlap * 0.5)
            self.pos += direction
            other.pos -= direction
            # The math is wonky which is why you can see particles suddenly pop after colliding, but it'll do
            distance = self.radius + other.radius

            mass_sum = self.mass + other.mass
            velDiff = other.velocity - self.velocity
            # Self Particle math
            num = velDiff.dot(impact_vector)
            den = mass_sum * distance * distance
            deltaVA = impact_vector.copy()
            deltaVA *= (2 * other.mass * num / den)
            self.velocity += deltaVA
            # Other Particle math
            deltaVB = impact_vector.copy()
            deltaVB *= (-2 * self.mass * num / den)
            other.velocity += deltaVB
