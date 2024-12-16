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
        self.radius = self.mass * 2  # Radius proportional to the mass

    def draw(self):
        self.velocity += self.acceleration
        self.pos += self.velocity
        self.acceleration *= 0  # Reset acceleration after each frame
        pygame.draw.circle(self.surface, "white", (int(self.pos.x), int(self.pos.y)), int(self.radius))

    def detect_window(self):
        """Keeps particles in bounds of window."""
        if self.pos.x > 1280 or self.pos.x < 0:
            self.velocity.x *= -1
        if self.pos.y > 720 or self.pos.y < 0:
            self.velocity.y *= -1

    def collision_detection(self, other):
        """Checks if a particle is colliding with another. If so it is handled so it no longer collides."""
        impact_vector = other.pos - self.pos
        distance = impact_vector.magnitude()

        if distance < self.radius + other.radius:
            overlap = distance - (self.radius + other.radius)
            direction = impact_vector.copy() * (overlap * 0.5)
            self.pos += direction
            other.pos -= direction

            mass_sum = self.mass + other.mass
            velDiff = other.velocity - self.velocity
            num = velDiff.dot(impact_vector)
            den = mass_sum * distance ** 2
            deltaVA = impact_vector.copy() * (2 * other.mass * num / den)
            self.velocity += deltaVA
            deltaVB = impact_vector.copy() * (-2 * self.mass * num / den)
            other.velocity += deltaVB