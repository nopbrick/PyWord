# PyWord

PyWord is a python script to create wordlists of any kind. Initially created to create most common passwords wordlist suited for your needs. 

![PyWord](/preview.png)

## Installation

**NOTE**: Python 3 is required.

```bash
# clone the repo
$ git clone https://github.com/filipceglik/PyWord.git

# change the working directory to PyWord
$ cd PyWord
```

## Usage

```bash
$ python3 pyword.py --help
usage: pyword.py [-h] [--years YEAR_DICT [YEAR_DICT ...]]
                 [--langs LANG_DICT [LANG_DICT ...]] [--long] [--allcase]
                 [--alllangs]

optional arguments:
  -h, --help            show this help message and exit
  --years YEAR_DICT [YEAR_DICT ...]
                        Specify years to create a wordlist with: pass strings
                        in yyyy format.
  --langs LANG_DICT [LANG_DICT ...]
                        Limit word list to certain languages: Pl, Eng
  --long                Add long year format
  --allcase             Create wordlist both with regular words and lowercase
                        words
  --alllangs            Create a wordlist using all supported languages
```

<p></p>
<a href="https://www.buymeacoffee.com/hydLneBap" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/black_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a><p></p>
If you like my project and want me to keep expanding it, you can donate with BuyMeaCoffee button above. 
