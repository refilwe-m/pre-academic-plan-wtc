def main():
   text = input('Input: ')
   print(shorten(text))


def shorten(word):
    output = ""
    for char in word:
        if char not in 'aeiouAEIOU':
            output+=char
    return output

if __name__ == "__main__":
    main()