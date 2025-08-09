def main():
   text = input('Input: ')
   shorten(text)


def shorten(word):
    output = ""
    for char in word:
        if char not in 'aeiouAEIOU':
            output+=char
    print('Output:',output)


if __name__ == "__main__":
    main()