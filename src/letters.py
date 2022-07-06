from pygame.sprite import Sprite
import pygame


class Letters(Sprite):
    def __init__(self,screen,character,col,row,origin_x, origin_y, color):
        self.color = color
        # basic font for user typed
        self.text_size = 80
        base_font = pygame.font.Font(None, self.text_size-10)
        self.text = base_font.render(character, True, (254,254,254))

        # create rectangle
        self.text_rect = self.text.get_rect(center=(origin_x + row*self.text_size,origin_y +col*self.text_size))
        # set the center of the rectangular object.
        pygame.draw.circle(screen, self.color, self.text_rect.center, self.text_size//2-5)
        # draw text
        screen.blit(self.text, self.text_rect)

        super(Letters,self).__init__()

    def select(self,screen):
        self.color = pygame.Color('DarkSlateGray')
        pygame.draw.circle(screen, self.color, self.text_rect.center, self.text_size//2-5)
        screen.blit(self.text, self.text_rect)
        super(Letters,self).__init__()


class Lists(Sprite):
    def __init__(self):
        super(Lists,self).__init__()
        self.all_letters = []

    def append_to_list(self, obj):
        self.all_letters.append(obj)

    def create_all_letters(self,screen,origin_x,origin_y,start_letter,end_letter,required_col):
        current_row, current_col  = 0,0
        for i in range(start_letter,end_letter+1):
            obj = Letters(screen, chr(i), current_row, current_col, origin_x, origin_y, pygame.Color('Turquoise'))
            self.append_to_list(obj)
            current_col += 1
            if current_col == required_col:
                current_row += 1
                current_col = 0
    
    def create_word(self,screen,origin_x,origin_y,word,bgcolor):
        for i in range(0,len(word)):    
            obj = Letters(screen, word[i], 0, i, origin_x, origin_y, bgcolor)
            self.append_to_list(obj)
    
    def update(self,screen,origin_x,origin_y,letter,index):
        obj = Letters(screen, letter, 0, index, origin_x, origin_y, pygame.Color('LimeGreen'))
        self.all_letters[index] = obj

class Textbox:
    def __init__(self, screen, originx, originy, strtext,fgcolor, bgcolor, text_size):
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        # basic font for user typed
        self.text_size = text_size
        self.base_font = pygame.font.Font(None, self.text_size-10)
        self.text = self.base_font.render(strtext, True, self.fgcolor)

        # create rectangle
        self.text_rect = self.text.get_rect(center=(originx,originy))
        # set the center of the rectangular object.
        pygame.draw.rect(screen, self.bgcolor, self.text_rect)
        # draw text
        screen.blit(self.text, self.text_rect)
        super(Textbox,self).__init__()        
    
    def update_stats(self,screen,lives):
        screen.fill(pygame.Color('White'),self.text_rect)
        if lives < 5:
            self.fgcolor = pygame.Color('Red')
        self.text = self.base_font.render('Lives: '+str(lives), True, self.fgcolor)
        screen.blit(self.text, self.text_rect)

         