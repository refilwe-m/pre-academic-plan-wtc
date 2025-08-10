import twttr

def test_shorten():
    assert twttr.shorten("Twitter") == "Twttr"
    assert twttr.shorten("What's your name?") == "Wht's yr nm?"
    assert twttr.shorten("CS50") == "CS50"
    assert twttr.shorten("TWITTER") == "TWTTR"
    assert twttr.shorten(".gugu") == ".gg"
    assert twttr.shorten("123") == "123"
