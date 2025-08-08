from random import randint

def prompt():
    return int(input("Level: "))

while True:
    try:
        n = prompt()
        break
    except:
        continue
target = randint(1,n)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <=0:
            continue
        elif guess < target:
            print("Too small!")
            continue
        elif guess > target:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break
    except:
        continue

