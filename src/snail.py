from ast import Pass
from pygame.sprite import Sprite
import pygame

class Snail(Sprite):
    def __init__(self,posx,posy,index):
        self.speedchanger=1
        self.posx = posx
        self.posy = posy
        #adding all the images to sprite array
        self.images = []
        self.images.append(pygame.image.load('snails/spr_snail0.png'))
        self.images.append(pygame.image.load('snails/spr_snail1.png')) 
        
        #index value to get the image from the array
        #initially it is 0 
        self.index = index
 
        #now the image that we will display will be the index from the image array 
        self.image = self.images[self.index]
 
        #creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite 
        self.rect = pygame.Rect(self.posx, self.posy, 150, 198)
        super(Snail, self).__init__()
        
    def move(self):
        self.rect.x += self.speedchanger
        self.image = self.images[self.index]

    def update(self):
        pass
        #when the update method is called, we will increment the index
        #self.index += 1
 
        #if the index is larger than the total images
        #if self.index >= len(self.images):
            #we will make the index to 0 again
        #    self.index = 0
        
        #finally we will update the image that will be displayed
        #self.image = self.images[self.index]