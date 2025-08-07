import re
from datetime import datetime
        
def is_valid_input(s):
    
    month_pattern = r"^(January|February|March|April|May|June|July|August|September|October|November|December) ([1-9]|[12][0-9]|3[01]), \d{4}$"
    numeric_pattern = r"^(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/\d{4}$"
    
    if re.match(month_pattern, s):
        try:
            print(datetime.strptime(s, "%B %d, %Y").strftime("%Y-%m-%d"))
            return True
        except ValueError:
                return False
    elif re.match(numeric_pattern, s):
        try:
            ts = datetime.strptime(s, "%m/%d/%Y")
            ds = ts.strftime("%m-%d-%Y")
            [month,day,year] = ds.split("-")
            print(f"{year}-{month}-{day}", end="")
            return True
        except ValueError:
            return False

while True:
        date = input('Date: ').strip()
        if is_valid_input(date):
            break
            