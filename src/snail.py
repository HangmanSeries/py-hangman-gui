from ast import Pass
from pygame.sprite import Sprite
import pygame

class Snail(Sprite):
    def __init__(self,posx,posy,type):
        self.fps = 1
        self.startframe = 0
        self.endframe = 17
        self.speedchanger=1
        self.posx = posx
        self.posy = posy
        #adding all the images to sprite array
        self.images = []
        for i in range(0,47):
            i = str(i).zfill(2)
            for j in range(0,4): #more frames equals slower snail motion at 10fps
                if type == 1: #if user snail
                    img = pygame.image.load('snails/RedSnail/sprite_'+i+'.png')
                               # create a 2x bigger image than self.image
                else:
                    img = pygame.image.load('snails/GoldSnail/sprite_'+i+'.png')
                img =  pygame.transform.scale(img, (240,240))
                self.images.append(img)
        
    
        #index value to get the image from the array
        #initially it is 0 
        self.index = 0
 
        #now the image that we will display will be the index from the image array 
        self.image = self.images[self.index]
 
        #creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite 
        self.rect = pygame.Rect(self.posx, self.posy, 150, 198)
        super(Snail, self).__init__()
        
    def move(self):
        self.rect.x += self.speedchanger

    # def weaken(self,startframe,endframe):
    #     #when the update method is called, we will increment the index
    #     self.index += 1
    #     #if the index is larger than the total images
    #     if self.index >= endframe*4:
    #        #we will make the index to 0 again
    #        self.index = startframe
        
    #     #finally we will update the image that will be displayed
    #     self.image = self.images[self.index]
    def changefps(self, startframe, endframe,fps):
        self.startframe = startframe
        self.endframe = endframe
        self.fps = fps

    def update(self):
        #when the update method is called, we will increment the index
        if self.endframe<=47:
            self.index += self.fps
            #if the index is larger than the total images
        if (self.index >= self.endframe*4) and self.endframe<47:
        #we will make the index to 0 again
            self.index = self.startframe*4
        
        #finally we will update the image that will be displayed
        if self.index<47*4:
            self.image = self.images[self.index]