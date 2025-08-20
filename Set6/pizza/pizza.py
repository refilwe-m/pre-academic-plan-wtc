from tabulate import tabulate
from sys import exit,argv

try:
    if len(argv)!=2:
        exit("Invalid Argmunents")
    [_,fileName]=argv
    if not fileName.endswith(".csv"):
         exit("Not a CSV file")
    
    with open(fileName) as file:
        table = []
        for line in file:
            table.append(line.replace('\n','').split(","))
        print(tabulate(table,headers="firstrow",tablefmt="grid"))
          
except FileNotFoundError:
    exit("File does not exist")