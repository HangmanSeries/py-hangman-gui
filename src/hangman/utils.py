from .categories import *
from random import choice
from yaml import load, Loader
from colorama import init, Fore
from enum import Enum
from platform import system
from cerberus import Validator

r = Fore.RESET

def initialize_colors() -> None:
	if system() == 'Windows':
		init()

class HangmanCategory(Enum):
	Foods = "Foods"
	MusicInstruments = "Music Instruments"
	Coding = "Coding"
	Fruits = "Fruits"
	def to_string(self):
		return self.value

class WordGenerator:
	def __init__(self):
		pass

	def generate_category(self) -> HangmanCategory:
		categories = [
			HangmanCategory.Foods,
			HangmanCategory.MusicInstruments,
			HangmanCategory.Coding,
			HangmanCategory.Fruits
		]
		return choice(categories)

	def generate_word(self, category: HangmanCategory) -> str:
		match category:
			case HangmanCategory.Coding:
				return choice(coding)
			case HangmanCategory.Foods:
				return choice(foods)
			case HangmanCategory.MusicInstruments:
				return choice(music_instruments)
			case HangmanCategory.Fruits:
				return choice(fruits)

class ConfigLoader:
	def __init__(self):
		self.is_ensured = False
		self.is_valid = None
		with open('./src/hangman.yml', 'r') as file:
			self.config = load(file.read(), Loader=Loader)

	def ensure_config(self):
		v = Validator()
		config_schema = {'lives': {'type': 'integer', 'min': 3, 'max': 15}}
		if v.validate(self.config, config_schema):
			self.is_ensured = True
			self.is_valid = True
		else:
			self.is_valid = False
			self.is_ensured = True
			print(Fore.RED+f"Invalid config. Err: {v.errors['lives'][0]}"+r)

	def get_setting(self, settings):
		if self.is_ensured:
			if self.is_valid:
				return self.config[settings]
			else:
				exit()
		else:
			print(Fore.RED + "You cannot get any setting until you ensured this config file. Fix this by adding .ensure_config() to ConfigLoader object" + r)
			exit()
