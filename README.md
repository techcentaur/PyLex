# PyPoet
Python library for playing with words.

## Usage

#### Help Usage

```console
gavy42@jarvis:~/Desktop/github/PyPoet$ python3 script.py -h
usage: script.py [-h] [-r] [-s] [-a] [-m] [-ho] [-n NUMBER] word

PyPoet: Play with words

positional arguments:
  word                  an input of the word

optional arguments:
  -h, --help            show this help message and exit
  -r, --rhyme           get rhyming words
  -s, --synonym         get synonym
  -a, --antonym         get antonyms
  -m, --meaning         get meaning
  -ho, --homophones     get homophones
  -n NUMBER, --number NUMBER
                        number of words should be returned
```

#### Interpreter Usage

```python3
>>> from script import Poet
>>> p = Poet("alone")
>>> p
<script.Poet object at 0x7f8c075c5d68>
>>> wordlist = p.rhyming_words()
[*] Getting rhyming words for the word: alone...
>>> p.display_wordlist(wordlist, 4)
[*] Displaying list; Format: Descending
cologne
malone
overblown
blown
```

#### Functions Usage

After creating an object instance as `Poet(<string>)`, these functions are available

- `rhyming_words()` : Returns a list of words rhyming with the entered word.
- `synonyms()` : Returns a list of synonyms
- `antonyms()` : Returns a list of antonyms
- `meaning()` : Returns a list of possible meanings
- `homophones()` : Returns a list of homophones