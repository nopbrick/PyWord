from argparse import ArgumentParser, RawDescriptionHelpFormatter
import datetime, os



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
monthsEs = [
        'Enero',
        'Febrero',
        'Marzo',
        'Abril',
        'Mayo',
        'Junio',
        'Julio',
        'Agosto',
        'Septiembre',
        'Octubre',
        'Noviebre',
        'Diciembre'
]

monthsDe = [
        'Januar',
        'Janner',
        'Februar',
        'Marz',
        'April',
        'Mai',
        'Juni',
        'Juli',
        'August',
        'September',
        'Oktober',
        'November',
        'Dezember'
]

#END of data
currentDate = datetime.datetime.now()
varDict = {'monthsEng': monthsEng, 'monthsPl': monthsPl, 'monthsEs': monthsEs, 'monthsDe': monthsDe}


#START of functions



#Creates words with current year ending as yyyy
def get_long_year_pass(myDict, endFile, argDict, yearDict):
        if len(argDict) == 1:
                tempVar = "months" + str(argDict[0])
        else:
                for item in argDict:
                        tempVar = "months" + item
                        if tempVar in myDict:
                                for stuff in myDict[tempVar]:
                                        if not yearDict:
                                                passwd=str(stuff)+currentDate.strftime("%Y")
                                                endFile.write(passwd+'\n')
                                        else:
                                                for year in yearDict:
                                                        passwd=str(stuff)+str(year)
                                                        endFile.write(passwd+'\n')

def get_years(myDict, endFile, argDict, yearDict):
        if len(argDict) == 1:
                tempVar = "months" + str(argDict[0])
        else:
                for item in argDict:
                        tempVar = "months" + item
                        if tempVar in myDict:
                                for stuff in myDict[tempVar]:
                                        if not yearDict:
                                                passwd=str(stuff)+currentDate.strftime("%y")
                                                endFile.write(passwd+'\n')
                                        else:
                                                for year in yearDict:
                                                        passwd=str(stuff)+str(year[-2:])
                                                        endFile.write(passwd+'\n')
                                

#Creates a wordlist with all languages starting with capital letter and long date format
def get_all_languages(myDict, endFile, *args):
        for key in myDict.items():
                for item in key[1]:
                        passwd=str(item)+currentDate.strftime("%y")
                        endFile.write(passwd+'\n')

def get_all_languages_long(myDict, endFile, *args):
        for key in myDict.items():
                for item in key[1]:
                        passwd=str(item)+currentDate.strftime("%Y")
                        endFile.write(passwd+'\n')

#Creates a wordlist with specified languages
def get_langs(myDict, endFile, argDict, yearDict):
        if len(argDict) == 1:
                tempVar = "months" + str(argDict[0])
        else:
                for item in argDict:
                        tempVar = "months" + item
                        if tempVar in myDict:
                                for stuff in myDict[tempVar]:
                                        if not yearDict:
                                                passwd=str(stuff)+currentDate.strftime("%y")
                                        else:
                                                if type(yearDict) is str:
                                                        passwd=str(stuff)+str(yearDict[-2:])
                                                else:
                                                        for year in yearDict:
                                                                passwd=str(stuff)+str(year[-2:])
                                        endFile.write(passwd+'\n')


def get_all_cases():
        endFile = open("wordlist.txt", "r")
        content = endFile.readlines()
        tempFile = open("temp.txt", "w+")
        for line in content:
                passwd = line.lower()
                tempFile.write(passwd)
        endFile.close()
        tempFile.close()
        endFile = open("wordlist.txt", 'a')
        tempFile = open("temp.txt", "r")
        content = tempFile.readlines()
        for line in content:
                endFile.write(line)
        endFile.close()
        tempFile.close()
        os.remove("temp.txt")

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


        parser.add_argument("--years",
                                nargs='+',
                                default=currentDate.strftime("%Y"),
                                dest='year_dict',
                                help="Specify years to create a wordlist with: pass strings in yyyy format. "
                                )
        parser.add_argument("--langs",
                                nargs='+',
                                default="Eng",
                                dest='lang_dict',
                                help="Limit word list to certain languages: Pl, Eng, Es"
                                )
        parser.add_argument("--long",
                                action="store_true", 
                                dest="get_long_year",
                                help="Add long year format"
                                )
        parser.add_argument("--allcases",
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
        #words = "months" + args.lang_dict


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

        #yearEnding = currentDate.strftime("%")

        

        if args.get_long_year:
                get_long_year_pass(varDict, wordlist, args.lang_dict, args.year_dict)

        if args.get_all_langs:
                get_all_languages(varDict,wordlist)

        if args.get_all_langs and args.get_long_year:
                get_all_languages(varDict,wordlist)
                get_all_languages_long(varDict, wordlist)

        if args.year_dict:
                get_years(varDict, wordlist, args.lang_dict, args.year_dict)

        if args.lang_dict:
                get_langs(varDict,wordlist,args.lang_dict,args.year_dict)

        wordlist.close()
        if args.get_all_cases:
                get_all_cases()
                


        for lan in args.lang_dict:
                print(lan)
        print("Wordlist created successfully!\n")

if __name__ == "__main__":
    main()