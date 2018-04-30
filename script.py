import requests
import argparse
from bs4 import BeautifulSoup

def rhythmic_words(word):
	print("[*] Getting rhyming words ...\n")

	url = "http://www.b-rhymes.com/rhyme/word/"+word
	raw = requests.get(url)

	soup = BeautifulSoup(raw.text, "lxml")
	rows = soup.find_all('tr')

	for row in rows:
		
		cols = row.find_all('td')
		cols = [x.text.strip() for x in cols]
		
		if len(cols)!=0: 
			print(cols[1], end=' ')

	print("\n")

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--rhyme", help="get rhyming words", type=str)
args = parser.parse_args()

if len(args.rhyme)!=0:
	rhythmic_words(args.rhyme)