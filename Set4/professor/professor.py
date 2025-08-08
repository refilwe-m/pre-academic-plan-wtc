import random


def main():
    ...


def get_level():
    levels = ["1","2","3"]

    while True:
        level = input("")
        if level in levels:
            return level


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()

