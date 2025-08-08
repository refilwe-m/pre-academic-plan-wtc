import inflect
p = inflect.engine()
words = []

while True:
    try:
        word = input("Name: ")
        if word == "":
            continue
        words.append(word)
    except EOFError or KeyboardInterrupt:
        break
    
print("\nAdieu, adieu, to",p.join(words))
