import ast
import click
import json
import requests
import argparse
from bs4 import BeautifulSoup

class Lex:
	def __init__(self, word):
		self.word = word

	def rhyming_words(self):
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

	def sound_alike(self):
		templist = []
		wordlist = []
		url = "https://api.datamuse.com/words?sl=" + self.word

		data = requests.get(url)

		for dlist in data:
			dlist = dlist.decode("utf-8")
			templist.append(dlist)

		string = "".join(templist)
		strdict = ast.literal_eval(string)

		for dlist in strdict:
			wordlist.append(dlist['word'])
		
		return wordlist


	def homophones(self):
		wordlist = []
		url = "https://api.datamuse.com/words?rel_hom=" + self.word

		data = requests.get(url)

		for dlist in data:
			dlist = ast.literal_eval(dlist.decode("utf-8"))

			for d in dlist:
				wordlist.append(d["word"])

		return wordlist

	# def homographs(self):
	# 	wordlist = []
	# 	url = "http://www.roget.org/BRIAN0.html"

	# 	raw = requests.get(url)
	# 	soup = BeautifulSoup(raw.text, "lxml")
	# 	rows = soup.find_all('tr')

	# 	for row in rows:			
	# 		cols = row.find_all('td')
	# 		cols = [x.text.strip() for x in cols]

	# 		print(cols)
		
	def meaning(self):
		string = self.word.split(" ")
		string = "-".join(string)

		url = "http://www.dictionary.com/browse/"+string
		session = requests.get(url)
		
		soup = BeautifulSoup(session.text, "lxml")
		
		sec = soup.find_all('section')
		content = sec[0].find_all("div", {"class": "def-content"})

		meaninglist = []

		for c in content:
			meaninglist.append(c.text.strip())

		return meaninglist


	def display_wordlist(self, wordlist, num):
		print("[*] Displaying list; Format: Descending")

		if num>=len(wordlist):
			for w in wordlist: 
				print(w)
		else:
			for i in range(0, num):
				print(wordlist[i])


if __name__=="__main__":
	parser = argparse.ArgumentParser(description='PyLex: Perform lexical analysis, one word at a time.')
	parser.add_argument("word", help="an input of the word")

	parser.add_argument("-r", "--rhyme", help="get rhyming words", action="store_true")
	parser.add_argument("-s", "--synonym", help="get synonym", action="store_true")
	parser.add_argument("-a", "--antonym", help="get antonyms", action="store_true")
	parser.add_argument("-m", "--meaning", help="get meaning", action="store_true")

	parser.add_argument("-hp", "--homophones", help="get homophones", action="store_true")
	parser.add_argument("-hg", "--homographs", help="get homographs", action="store_true")
	parser.add_argument("-sa", "--sound_alike", help="get words that sound alike", action="store_true")

	parser.add_argument("-n", "--number", type=int, help="number of words need to be returned", default=50)

	parser.add_argument("-f", "--full", help="FULL lexical analysis", action="store_true")


	args = parser.parse_args()

	lex = Lex(args.word)

	if args.rhyme:
		print("[*] Getting rhyming words for the word:", args.word,"...")

		wl = lex.rhyming_words()
		lex.display_wordlist(wl, args.number)

	if args.synonym:
		print("[*] Getting synonyms for the word:", args.word, "...")

		wl = lex.synonyms()
		lex.display_wordlist(wl, args.number)

	if args.antonym:
		print("[*] Getting antonyms for the word:", args.word, "...")

		wl = lex.antonyms()		
		lex.display_wordlist(wl, args.number)

	if args.homophones:
		print("[*] Getting homophones for the word:", args.word, "...")
		print("[!] Homophones are words that sound identical but are written differently [!]\n")
		wl = lex.homophones()		
		lex.display_wordlist(wl, args.number)

	# if args.homographs:
	# 	print("[*] Getting homographs for the word:", args.word, "...")
	# 	print("[!] Homographs are words that spelled identical but have different meaning [!]\n")
	# 	wl = lex.homographs()		
	# 	lex.display_wordlist(wl, args.number)

	if args.sound_alike:
		print("[*] Getting words that sound alike with :", args.word, "...\n")
		wl = lex.sound_alike()		
		lex.display_wordlist(wl, args.number)

	if args.meaning:
		print("[*] Fetching meaning of the word...")
		wl = lex.meaning()
		print((wl[0].split(":")[0]))

	if args.full:
		print('[!][!] Starting full analysis of:', args.word)
		analysis_dict = {}

		wl = lex.meaning()
		if len(wl) == 0:
			analysis_dict['meaning'] = []
		else:
			analysis_dict['meaning'] = (wl[0].split(":")[0])

		wl = lex.synonyms()
		analysis_dict['synonyms'] = wl

		wl = lex.antonyms()
		analysis_dict['antonyms'] = wl

		wl = lex.homophones()
		analysis_dict['homophones'] = wl

		# wl = lex.homographs()
		# analysis_dict['homographs'] = wl

		wl = lex.sound_alike()
		analysis_dict['sound_alike'] = wl

		wl = lex.rhyming_words()
		analysis_dict['rhyming_words'] = wl

		with open(args.word + "_lex_analysis.json", 'w') as outfile:
			json.dump(analysis_dict, outfile, indent=4)			

		print('\n[*][*] JSON file saved in local directory named - ' + args.word + "_lex_analysis.json")