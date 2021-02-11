import random
import os

with open(os.path.dirname(__file__)+"/lifeQuotes.txt","r",encoding="utf-8") as f:
	matter=f.read().split("\n")
def getRandomQuote():
	return random.choice(matter)