from colorama import Fore, Style
from hangman.utils import WordGenerator, ConfigLoader, initialize_colors
from string import ascii_letters
from letters import Letters
from pygame.surface import Surface
from pygame.sprite import Sprite
import pygame
from ground import Ground
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_a,
    K_s,
    K_d,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

initialize_colors()

# choosing a word
wgen = WordGenerator()
category = wgen.generate_category()
string_category = category.to_string()
word = wgen.generate_word(category)

# config file
config = ConfigLoader()
config.ensure_config()

# returns a set (just like list but no duplicates (easy hack))
def indices(word, letter):
  char_indices = set()
  for x in range(len(word)):
    if word.find(letter, x) != -1:
      char_indices.add(word.find(letter, x))
  return char_indices

# all alternative but False if ' '
def all_not_blank(iterable):
  for element in iterable:
    if element == ' ':
      return False
  return True


# any alternative but False if all are ' '
def any_wrong_letter(iterable):
  for element in iterable:
    if element != ' ':
      return True
  return False

# ensure lives
def lives_color(lives):
  r = Fore.RESET
  if lives == 3 or lives == 2:
    return Fore.YELLOW + str(lives) + r
  elif 10 >= lives >= 4:
    return Fore.GREEN + str(lives) + r
  else:
    return Fore.RED + str(lives) + r

# lives
lives = config.get_setting('lives')
# print(lives)

# welcome message
print("Welcome to the Game of Hangman :D\n")

# guessed letters
guessed_letters = [' ' for _ in range(len(word))]
wrong_letters = [' ' for _ in range(lives)]

pygame.init()
width = 1000
height = 600

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Py-Hangman')
screen.fill((255,255,255))
pygame.display.flip()

#letter1 = letters()
Letters.create_all_letters(screen, 620, 90, 65, 90, 5)
Letters.create_word(screen, 120, 90, word)

running =  True
while running:
  for event in pygame.event.get():
      if event.type == KEYDOWN:
          if event.key == K_ESCAPE:
              running = False

      elif event.type == QUIT:
          running = False

  pressed_keys = pygame.key.get_pressed()
  
  pygame.display.flip()


  # # letters guessed
  # print(Fore.GREEN + Style.BRIGHT + "|  W O R D  |" + Style.RESET_ALL)
  # # Category
  # print("Category: {}".format(string_category))
  # for x in guessed_letters:
  #   print(x, end=" ")

  # # new line
  # print()
  
  # # blanks
  # for x in range(len(word)):
  #   print("\u203e", end=" ")

  # if any_wrong_letter(wrong_letters):
  #   print((Fore.RED + "\tWrong letters: " + Fore.RESET).expandtabs(6))
  #   for x in wrong_letters:
  #     print(x, end=" ")

  # # new line
  # print()

  # # if all blanks are filled up
  # if all_not_blank(guessed_letters):
  #   print(f'\nAnswer: {word}')
  #   print("complete!")
  #   exit()

  # # number of lives
  # print(f"Lives: {lives_color(lives)}")

  # if not lives:
  #   print("You lose BOOMER!")
  #   print("Answer: {}".format(word))
  #   break

  # # simply input
  # letter_input = input("\n=> ")

  # # exit
  # if letter_input == 'exit':
  #   break
  # # player giving up
  # elif letter_input == "giveup":
  #   print("Answer:", word)
  #   break
  # # empty string
  # elif letter_input == '':
  #   print("Letter letter LEEEEETTTTTEEERRRRRR!")
  # elif letter_input not in ascii_letters:
  #   print("Not a symbol")
  # elif letter_input == 'clue':
  #   print("Starts with {}".format(word[0]))
  # # not 1 letter
  # elif len(letter_input) != 1:
  #   print("letter please.")
  # # letter not in chosen word
  # elif letter_input not in word:
  #   print("wrong letter :P")
  #   if letter_input not in wrong_letters:
  #     lives -= 1
  #     wrong_letters.append(letter_input)

  # # correct letter
  # elif letter_input in word:
  #   # if letter not in guessed letters
  #   if letter_input not in guessed_letters:
  #     print("letter guessed!")
  #     guessed_letters[word.index(letter_input)] = letter_input

  #     # if a letter has more than two characters on a word
  #     if word.count(letter_input) >= 2:
  #       for x in indices(word, letter_input):
  #         guessed_letters[x] = letter_input
  #   # if letter already guessed
  #   else:
  #     print("letter already guessed.")
