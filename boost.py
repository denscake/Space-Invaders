import pygame
from pygame.sprite import Sprite
import random


class Boost(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen

        self.picture = pygame.image.load("images/boost.png").convert_alpha()
        self.rect = self.picture.get_rect()
        self.image = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA, 32)
        self.image.blit(self.picture, (0, 0))

        self.x = random.randrange(0, ai_settings.screen_width - self.rect.width)
        self.y = -self.rect.height

        self.speed_factor = ai_settings.boost_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.speed_factor
        self.rect.y = self.y
        self.rect.x = self.x
