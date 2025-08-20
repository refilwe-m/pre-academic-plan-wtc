from sys import exit, argv
import re
import os
import csv

try:
    if len(argv)!=3:
        exit('Invalid Number of Arguments')

    [_,fileName,new_file_name] = argv
    
    if os.path.exists(new_file_name):
        os.remove(new_file_name)
    
    with open(fileName,'r') as file:
        reader = csv.reader(file)
        with open(new_file_name,mode='w', newline='') as new_file:
            writer = csv.writer(new_file,delimiter=',')
            for row in reader:
                if 'name' in row:
                    writer.writerow(['first','last','house'])
                else:
                    [surname,name] = row[0].split(',')
                    writer.writerow([f'{name.strip()}', f'{surname.strip()}',row[1]])
        
    # with open(fileName) as ref_file:
    #     for line in ref_file:
    #         match = re.match(r'^"([^"]+)"', line)
    #         if match:
    #             [surname,name] = match.group(1).split(",")
                
    #             with open(new_file_name,'w', newline='') as new_file:
    #                 new_file.write(f'"{name.strip()}, {surname}",{line.split(",")[2]}')
    
                
except FileNotFoundError:
    exit("File does not exit")