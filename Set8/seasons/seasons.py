from datetime import date, time
from sys import exit
import inflect
p = inflect.engine()

def is_valid_date(d:str):
    try:
        yyyy,mm,dd = d.split("-")
        if not yyyy.isdigit() or len(yyyy)!=4:
            return False
        if not mm.isdigit() or len(mm)!=2:
            return False
        if not dd.isdigit() or len(dd)!=2:
            return False
    except:
        return False
    return True
    

def main():
    dob = input('Date of Birth: ').strip()
    if not is_valid_date(dob):
        exit("Invalid date")
    year,mon,day = dob.split('-')
    dob_date = date(int(year), int(mon), int(day))
    today = date(2000,1,1)
    delta = abs(date.today() - dob_date)
    seconds = delta.days * 24 * 60 * 60
    minutes = int(seconds/60)
    print(p.number_to_words(minutes).capitalize().replace(' and',''),p.plural_noun("minute",minutes))
    #print('Five hundred twenty-five thousand, six hundred minutes')


if __name__ == "__main__":
    main()