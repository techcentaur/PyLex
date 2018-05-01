# PyPoet
Python library for playing with words.

## Usage

```console
gavy42@jarvis:~/PyPoet$ python3 script.py -h
usage: script.py [-h] [-r] [-s] [-a] [-n NUMBER] word

PyPoet: Play with words

positional arguments:
  word                  an input of the word

optional arguments:
  -h, --help            show this help message and exit
  -r, --rhyme           get rhyming words
  -s, --synonym         get synonym
  -a, --antonym         get antonyms
  -n NUMBER, --number NUMBER
                        number of words should be returned
```

## Module calls

```console
>>> from script import Poet

>>> Poet("alone")
<script.Poet object at 0x7f072e1f8d68>

>>> Poet("alone").rhyming_words(3)
[*] Getting rhyming words for the word:  alone  ...
[*] Format: (Word, Pronunciation)

( cologne, kuhluh_uun )
( malone, muhluh_uun )
( overblown, uh_uuvuhrb_luh_uun )
>>> 
```

