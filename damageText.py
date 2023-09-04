import pygame


# DAMAGE TEXT CLASS
class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, color, font) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(str(damage), True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        # DAMAGE TEXT ANIMATION
        self.rect.y -= 1
        # DELETE COUNTER AFTER #s
        self.counter += 1
        if self.counter > 30:
            self.kill()
