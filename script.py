import requests
import argparse
from bs4 import BeautifulSoup


class Poet:
	def __init__(self, word):
		self.word = word

	def rhythmic_words(self, num):
		print("[*] Getting rhyming words for the word: ", self.word," ...\n")
		print("[*] Format: (Word, Pronunciation) \n")

		url = "http://www.b-rhymes.com/rhyme/word/" + self.word
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


	def synonyms(self, num):
		print("\n[*] Getting synonyms for the word: ", self.word, "...")
		print("[*] Format: Descending\n")

		url = "http://www.thesaurus.com/browse/" + self.word

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


	def antonyms(self, num):
		print("\n[*] Getting antonyms for the word: ", self.word, "...")
		print("[*] Format: Descending\n")
		url = "http://www.thesaurus.com/browse/" + self.word

		raw = requests.get(url)
		soup = BeautifulSoup(raw.text, "lxml")

		section = soup.find_all('section')
		ul = section[1].find_all('ul')
		li = ul[0].find_all('li')

		for element in li:
			for x in element:
				x = x.text.strip()
				if not x.startswith('.css'):
					print(x)
				else:
					temp_list = x.split('}')
					print(temp_list[len(temp_list)-1])


if __name__=="__main__":
	parser = argparse.ArgumentParser(description='PyPoet: Play with words')
	parser.add_argument("word", help="an input of the word")
	parser.add_argument("-r", "--rhyme", help="get rhyming words", action="store_true")
	parser.add_argument("-s", "--synonym", help="get synonym", action="store_true")
	parser.add_argument("-a", "--antonym", help="get antonyms", action="store_true")
	parser.add_argument("-n", "--number", type=int, help="number of words should be returned", default=20)

	args = parser.parse_args()

	poet = Poet(args.word)

	if (args.rhyme):
		poet.rhythmic_words(args.number)

	if (args.synonym):
		poet.synonyms(args.number)

	if (args.antonym):
		poet.antonyms(args.number)