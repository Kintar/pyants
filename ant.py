import pygame.draw
from pygame.math import Vector2


green = pygame.Color(0, 255, 0, 255)


class Ant:
    def __init__(self):
        self.position = Vector2(0, 0)
        self.direction = Vector2(1, 0)
        self.rotation = 0.0
        self.speed = 0.0

    def on_update(self, delta):
        target_dir = self.direction
        target_dir.rotate(self.rotation)
        self.direction = self.direction.slerp(target_dir, delta)
        target_pos = self.position
        target_pos += self.direction * self.speed
        self.position = self.position.lerp(target_pos, delta)
        print(F"pos: {self.position}, heading: {self.direction}, speed: {self.speed}")

    def on_render(self, surface):
        pygame.draw.circle(surface, green, self.position, 5, 1)
        pygame.draw.line(surface, green, self.position, self.position + self.direction * 10, 1)
