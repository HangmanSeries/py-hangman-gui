from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame.image import load
import pygame

class Ground(Sprite):
    def __init__(self):
        super(Ground, self).__init__()
        self.surf = Surface((550, 100))
        self.surf.fill((200, 0, 0))
        self.rect = self.surf.get_rect()
        