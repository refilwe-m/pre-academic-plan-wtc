def value(greeting):
    """
    Returns:
    0 if greeting starts with 'hello' (any case, extra words allowed)
    20 if greeting starts with 'h' but not 'hello'
    100 otherwise
    """
    if not isinstance(greeting, str):
        return 100  # handle non-string inputs defensively

    normalized = greeting.strip().lower()

    if normalized.startswith("hello"):
        return 0
    elif normalized.startswith("h"):
        return 20
    else:
        return 100


def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


if __name__ == "__main__":
    main()