from sys import argv,exit

num_lines = 0

try:
    if len(argv)==1:
         exit("Too few command-line arguments")
    if len(argv)>2:
        exit("Too many command-line arguments") 
        
    [_,fileName] = argv
    
    if not fileName.endswith('.py'):
        exit('Invalid file type, expected a python file')
    with open(fileName) as file:
        for line in file:
            if not (line.strip() == "\n" or  line.strip().startswith("#") or line.strip()==''):
                num_lines+=1
        print(num_lines,end='')
except FileNotFoundError:
    exit('File does not exist')