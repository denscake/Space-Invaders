import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship, angle=0):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        self.horizontal_speed_factor = ai_settings.bullet_horizontal_speed_factor * angle
        self.old_x = self.x
        self.old_y = self.y
        self.width = ai_settings.bullet_width

    def update(self):
        self.old_x = self.x
        self.old_y = self.y

        self.y -= self.speed_factor
        self.rect.y = self.y
        self.x -= self.horizontal_speed_factor
        self.rect.x = self.x

        self.draw_x = self.x + (self.x - self.old_x) * 2
        self.draw_y = self.y + (self.y - self.old_y) * 2

    def draw_bullet(self):
        try:
            pygame.draw.line(self.screen, self.color, (self.x, self.y), (self.draw_x, self.draw_y), self.width)
        except AttributeError:
            pass
