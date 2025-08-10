from bank import value

def test_hello_exact_and_case():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("HelLo") == 0

def test_hello_with_extra_words():
    assert value("hello there") == 0
    assert value("   hello friend") == 0

def test_h_not_hello():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("   Hi there") == 20

def test_other_words():
    assert value("good morning") == 100
    assert value("123") == 100
    assert value("ola") == 100