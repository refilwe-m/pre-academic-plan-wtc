text = input('Input: ')
output = ""
for char in text:
    if char not in 'aeiouAEIOU':
        output+=char
print('Output: ',output)