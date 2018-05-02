import requests
import argparse
from bs4 import BeautifulSoup


class Poet:
	def __init__(self, word):
		self.word = word

	def rhyming_words(self):
		print("[*] Getting rhyming words for the word:", self.word,"...")

		url = "http://www.b-rhymes.com/rhyme/word/" + self.word
		raw = requests.get(url)

		soup = BeautifulSoup(raw.text, "lxml")
		rows = soup.find_all('tr')

		templist = []
		wordlist = []

		for row in rows:			
			cols = row.find_all('td')
			cols = [x.text.strip() for x in cols]

			templist.append(cols)
		
		for t in templist:
			if len(t)!=0: 
				wordlist.append(t[1])

		return wordlist


	def synonyms(self):
		print("[*] Getting synonyms for the word:", self.word, "...")

		url = "http://www.thesaurus.com/browse/" + self.word

		raw = requests.get(url)
		soup = BeautifulSoup(raw.text, "lxml")

		section = soup.find_all('section')
		ul = section[0].find_all('ul')
		li = ul[0].find_all('li')

		wordlist = []
		
		for element in li:
			for x in element:
				x = x.text.strip()
				if not x.startswith('.css'):
					wordlist.append(x)
				else:
					temp_list = x.split('}')
					wordlist.append(temp_list[len(temp_list)-1])

		return wordlist


	def antonyms(self):
		print("[*] Getting antonyms for the word:", self.word, "...")

		url = "http://www.thesaurus.com/browse/" + self.word

		raw = requests.get(url)
		soup = BeautifulSoup(raw.text, "lxml")

		section = soup.find_all('section')
		ul = section[1].find_all('ul')
		li = ul[0].find_all('li')

		wordlist = []

		for element in li:
			for x in element:
				x = x.text.strip()
				if not x.startswith('.css'):
					wordlist.append(x)
				else:
					temp_list = x.split('}')
					wordlist.append(temp_list[len(temp_list)-1])

		return wordlist


	def meaning(self):
		string = self.word.split(" ")
		string = "+".join(string)

		url = "https://www.google.com/search?q="+string

		session = requests.get(url)
		soup = BeautifulSoup(session.text, "lxml")
		soup = soup.prettify()
		div = soup.find("div", {"class": "lr_dct_ent_vmod"})

		ol = div.find_all('ol')

		for new in ol:
			print(new.text.strip())


	def display_wordlist(self, wordlist, num):
		print("[*] Displaying list; Format: Descending")

		if num>=len(wordlist):
			for w in wordlist: 
				print(w)
		else:
			for i in range(0, num):
				print(wordlist[i])


if __name__=="__main__":
	parser = argparse.ArgumentParser(description='PyPoet: Play with words')
	parser.add_argument("word", help="an input of the word")
	parser.add_argument("-r", "--rhyme", help="get rhyming words", action="store_true")
	parser.add_argument("-s", "--synonym", help="get synonym", action="store_true")
	parser.add_argument("-a", "--antonym", help="get antonyms", action="store_true")
	parser.add_argument("-m", "--meaning", help="get meaning", action="store_true")
	parser.add_argument("-n", "--number", type=int, help="number of words should be returned", default=50)

	args = parser.parse_args()

	poet = Poet(args.word)

	if args.rhyme:
		wl = poet.rhyming_words()
		poet.display_wordlist(wl, args.number)

	if args.synonym:
		wl = poet.synonyms()
		poet.display_wordlist(wl, args.number)

	if args.antonym:
		wl = poet.antonyms()		
		poet.display_wordlist(wl, args.number)

	if args.meaning:
		poet.meaning()