import requests
import argparse
from bs4 import BeautifulSoup

def rhythmic_words(word, num):
	print("[*] Getting rhyming words ...\n")
	print("[*] Format: (Word, Pronunciation) \n")

	url = "http://www.b-rhymes.com/rhyme/word/"+word
	raw = requests.get(url)

	soup = BeautifulSoup(raw.text, "lxml")
	rows = soup.find_all('tr')

	wordlist = []

	for row in rows:
		
		cols = row.find_all('td')
		cols = [x.text.strip() for x in cols]

		wordlist.append(cols)

	if num>=len(wordlist):
		for w in wordlist:
			if len(w)!=0: 
				print("( "+w[1]+", "+w[2]+" )")
	else:
		for i in range(0, num):
			if len(wordlist[i])!=0:
				print("( "+wordlist[i][1]+", "+wordlist[i][2]+" )")


def synonyms(word, num):
	print("\n [*] Getting synonyms for the word: ", word, "...")

	url = "http://www.thesaurus.com/browse/"+word

	raw = requests.get(url)
	soup = BeautifulSoup(raw.text, "lxml")

	section = soup.find_all('section')
	ul = section[0].find_all('ul')
	li = ul[0].find_all('li')

	for element in li:
		for x in element:
			x = x.text.strip()
			if not x.startswith('.css'):
				print(x)
			else:
				temp_list = x.split('}')
				print(temp_list[len(temp_list)-1])


parser = argparse.ArgumentParser(description='PyPoet: Play with words')
parser.add_argument("word", help="an input of the word")
parser.add_argument("-r", "--rhyme", help="get rhyming words", action="store_true")
parser.add_argument("-s", "--synonym", help="get synonym words", action="store_true")
parser.add_argument("-n", "--number", type=int, help="number of words should be returned", default=20)

args = parser.parse_args()

if (args.rhyme):
	rhythmic_words(args.word, args.number)

if (args.synonym):
	synonyms(args.word, args.number)