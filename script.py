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


parser = argparse.ArgumentParser()
parser.add_argument("-r", "--rhyme", help="get rhyming words", type=str, required=True)
parser.add_argument("-n", "--number", type=int, help="number of words should be returned", default=20)

args = parser.parse_args()

if len(args.rhyme)!=0:
	rhythmic_words(args.rhyme, args.number)