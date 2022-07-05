from ast import Pass
from pygame.sprite import Sprite
from pygame import Surface
import pygame


class Letters(Sprite):
    def __init__(self,screen,character,col,row,origin_x, origin_y):
        # basic font for user typed
        text_size = 80
        base_font = pygame.font.Font(None, text_size-10)
        self.text = base_font.render(character, True, (254,254,254))

        # create rectangle
        self.text_rect = self.text.get_rect(center=(origin_x + row*text_size,origin_y +col*text_size))
        # set the center of the rectangular object.
        pygame.draw.circle(screen, pygame.Color('chartreuse4'), self.text_rect.center, text_size//2-5)
        # draw text
        screen.blit(self.text, self.text_rect)

        super(Letters,self).__init__()

    #I regret using recursion, might change this to for loop soon
    def create_all_letters(screen,origin_x,origin_y,start_letter,end_letter,required_col):
        all_letters = []
        def list_all(list, start_letter, end_letter, required_col, current_col, current_row):
            list.append(chr(start_letter))
            Letters(screen, chr(start_letter), current_row, current_col, origin_x, origin_y)
            current_col = current_col + 1
            if current_col==required_col:
                current_row = current_row + 1
                current_col = 0
            
            if start_letter!=end_letter:
                return list_all(list, start_letter+1, end_letter, required_col, current_col, current_row)
            return list
            
        all_letters = list_all(all_letters,start_letter,end_letter,required_col,0,0)
    
    def create_word(screen,origin_x,origin_y,word):
        for i in range(0,len(word)):    
            Letters(screen, word[i], 0, i, origin_x, origin_y)
        