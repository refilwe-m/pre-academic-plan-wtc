def convert():
    emoticon_to_emoji = {":)":'🙂',':(':'🙁'}
    input_text = input()
    
    print(input_text.replace(':)',"🙂").replace(':(','🙁'))

convert()