file_name = input("File Name: ").strip().lower()
file_type = ''
if file_name.endswith('.gif'):
    file_type = 'image/gif'
elif file_name.endswith('.png'):
    file_type = 'image/png'
elif file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
     file_type = 'image/jpeg'
elif file_name.endswith('.pdf'):
    file_type = 'application/pdf'
elif file_name.endswith('.zip'):
    file_type = 'application/zip'
elif file_name.endswith('.txt'):
    file_type = 'text/plain'
else:
    file_type ='application/octet-stream'
    
print(file_type, end='')
