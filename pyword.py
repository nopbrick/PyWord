from argparse import ArgumentParser, RawDescriptionHelpFormatter
import datetime


currentDate = datetime.datetime.now()
monthsEng = (
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
),

#Creates a wordlist with current year ending
def get_long_year_pass(months, endFile, passwd):
    for month in months:
        passwd=month+currentDate.strftime("%Y")
        endFile.Write(passwd+'\n')

def main():



    parser = ArgumentParser()


    parser.add_argument("--file",
                        action="store_true", dest="make_file", default=False,
                        help="Creates a wordlist file. "
                       )
    parser.add_argument("--lang",
                        action="append",
                        dest="lang_dict", default=None,
                        help="Limit word list to certain languages"
                       )
    parser.add_argument("--year",
                        action="store_true",
                        dest="get_long_year_pass",
                        help="Year to create wordlist with"
                       )

    args = parser.parse_args()

    if args.make_file:
        print("todo file export")

if __name__ == "__main__":
    main()