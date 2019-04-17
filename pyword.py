from argparse import ArgumentParser, RawDescriptionHelpFormatter
import datetime


currentDate = datetime.datetime.now()
monthsEng = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
monthsPl = [
        'Styczen',
        'Luty',
        'Marzec',
        'Kwiecien',
        'Maj',
        'Czerwiec',
        'Lipiec',
        'Sierpien',
        'Wrzesien',
        'Pazdziernik',
        'Listopad',
        'Grudzien'
]

#END of data

varDict = {'monthsEng': monthsEng, 'monthsPl': monthsPl}

#START of functions



#Creates words with current year ending as yyyy
def get_long_year_pass(months, endFile):
    for month in months:
        passwd=str(month)+currentDate.strftime("%Y")
        endFile.write(passwd+'\n')

def get_long_year_pass_lower(months, endFile):
    for month in months:
        passwd=str(month)+currentDate.strftime("%Y")
        endFile.write(passwd.lower()+'\n')

#Creates words with current year ending as yy
def get_short_year_pass(months, endFile):
    for month in months:
        passwd=month+currentDate.strftime("%y")
        endFile.write(passwd+'\n')

def get_short_year_pass_lower(months, endFile):
        for month in months:
                passwd=month+currentDate.strftime("%y")
                endFile.write(passwd.lower()+'\n')




def main():


        wordlist = open("wordlist.txt", "w+")
        
        parser = ArgumentParser()


        parser.add_argument("--file",
                                action="store_true", dest="make_file", default=False,
                                help="Creates a wordlist file. "
                                )
        parser.add_argument("--lang",
                                action="store",
                                default="Eng",
                                dest="lang_dict",
                                help="Limit word list to certain languages: Pl, Eng"
                                )
        parser.add_argument("--short",
                                action="store_true", 
                                dest="get_short_year",
                                help="Add short year format"
                                )
        parser.add_argument("--long",
                                action="store_true", 
                                dest="get_long_year",
                                help="Add long year format"
                                )
        parser.add_argument("--allcase",
                                action="store_true", 
                                dest="get_all_cases",
                                help="Create wordlist both with regular words and lowercase words"
                                )
        parser.add_argument("--alllangs",
                                action="store_true", 
                                dest="get_all_langs",
                                help="Create a wordlist using all supported languages"
                                )

        args = parser.parse_args()
        words = "months" + args.lang_dict


        print("""
  _____    __          __           _ 
 |  __ \   \ \        / /          | |
 | |__) |   \ \  /\  / /__  _ __ __| |
 |  ___/ | | \ \/  \/ / _ \| '__/ _` |
 | |   | |_| |\  /\  / (_) | | | (_| |
 |_|    \__, | \/  \/ \___/|_|  \__,_|
         __/ |                        
        |___/                         
        
        """)

        if args.get_short_year:
                get_short_year_pass(varDict[words], wordlist)

        if args.get_long_year:
                get_long_year_pass(varDict[words],wordlist)

        if args.get_all_cases:
                get_short_year_pass_lower(varDict[words],wordlist)
                get_long_year_pass_lower(varDict[words],wordlist)

        #if args.get_all_langs:

        
        wordlist.close()
        print("Wordlist created successfully!\n")

if __name__ == "__main__":
    main()