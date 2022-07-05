from requests import get, ConnectionError

try:
  foods = \
      get("https://raw.githubusercontent.com/imsky/wordlists/master/nouns/food.txt").text.split()
  music_instruments = \
      get("https://raw.githubusercontent.com/imsky/wordlists/master/nouns/music_instruments.txt").text.split()
  coding = \
      get("https://raw.githubusercontent.com/imsky/wordlists/master/nouns/coding.txt").text.split()
  fruits = \
      get("https://raw.githubusercontent.com/imsky/wordlists/master/nouns/fruit.txt").text.split()
except ConnectionError:
  print("Failed to fetch words")
  print("Internet connection is required.")
  exit()
