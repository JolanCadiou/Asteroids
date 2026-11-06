from circleshape import CircleShape
from constants import *
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):

    def __init__(self, x: float, y:float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast1.velocity = self.velocity.rotate(rand) * 1.2
            new_ast2.velocity = self.velocity.rotate(-rand) * 1.2
