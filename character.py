import pygame
import constants
import math


class CharacterClass:
    def __init__(self, x, y, animation_list) -> None:
        self.flip = False
        self.animation_list = animation_list
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animation_list[self.frame_index]
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    def move(self, dx, dy):
        if dx < 0:
            self.flip = True
        if dx > 0:
            self.flip = False
        # control diagonal speed
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2) / 2)
            dy = dy * (math.sqrt(2) / 2)

        self.rect.x += dx
        self.rect.y += dy

    def update(self):
        animation_cooldown = 70
        # handle animation
        # updated image
        self.image = self.animation_list[self.frame_index]
        # check if enought time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        # check if animation has finished
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def draw(self, surface):
        fipped_image = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(fipped_image, self.rect)
        pygame.draw.rect(surface, constants.RED, self.rect, 1)