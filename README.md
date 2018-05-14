# PyLex
Python3 library for performing lexical analysis on words, one word at a time.

## Usage

#### Help Usage

```console
gavy42@jarvis:~/PyLex$ python3 script.py -h
usage: script.py [-h] [-r] [-s] [-a] [-m] [-hg] [-sa] [-n NUMBER] [-f]
                 word

PyLex: Perform lexical analysis, one word at a time.

positional arguments:
  word                  an input of the word

optional arguments:
  -h, --help            show this help message and exit
  -r, --rhyme           get rhyming words
  -s, --synonym         get synonym
  -a, --antonym         get antonyms
  -m, --meaning         get meaning
  -hg, --homographs     get homographs
  -sa, --sound_alike    get words that sound alike
  -n NUMBER, --number NUMBER
                        number of words should be returned
  -f, --full            FULL lexical analysis
```

#### Interpreter Usage

```python3
>>> from script import Lex
>>> lex = Lex("alone")
>>> lex
<script.Lex object at 0x7f8c075c5d68>
>>> wordlist = lex.rhyming_words()
[*] Getting rhyming words for the word: alone...
>>> lex.display_wordlist(wordlist, 4)
[*] Displaying list; Format: Descending
cologne
malone
overblown
blown
```

#### Functions Usage

After creating an object instance as `Lex(<string>)`, these functions are available

- `rhyming_words()` : Returns a list of words rhyming with the entered word.
- `synonyms()` : Returns a list of synonyms
- `antonyms()` : Returns a list of antonyms
- `meaning()` : Returns a list of possible meanings
- `homophones()` : Returns a list of homophones
- `homographs()` : Returns a list of homographs
- `sound_alike()` : Returns a list of words that sound alike the given word

## PyLex Full Analysis

- Run `python3 script.py <word> -f` to get full lexical analysis of any word.
- Returns a JSON format file with contained information.

```console
gavy42@jarvis:~/PyLex$ python3 script.py alone -f
[!][!] Starting full analysis of: alone

[*][*] JSON file saved in local directory named - alone_lex_analysis.json

```

### Note
- Program makes calls to external website to gather the information and scrapes content wherever needed.

## Support
If you have any trouble understading some part of the code, feel free to raise an issue or for contributing, feel free to make a pull request.