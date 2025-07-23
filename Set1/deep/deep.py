answer = input('What is the answer to the Great Question of Life, the Universe and Everything? ')
correct_answers = ['42','forty-two','forty two']
feedback = 'Yes' if answer in correct_answers else 'No'
print(feedback)