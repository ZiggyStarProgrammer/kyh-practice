from uppgift_40 import reverse, upper, blank


def test_rev():
    expected = [3, 2, 1]
    got = reverse([1, 2, 3])
    assert expected == got

def test_rev_char():
    expected = ["c", "b", "a"]
    got = reverse(["a", "b", "c"])
    assert expected == got

def test_rev_wrong_in():
    expected = [3, 2, 1]
    got = reverse([1, 3, 2])
    assert expected == got

def test_upper():
    expected = 2
    got = upper("hej HopPop")
    assert expected == got

def test_upperM():
    expected = 2
    got = (upper("Hej GOpp"))
    assert expected <= got

def test_blank():
    expected = 3
    got = blank("as d sa d")
    assert expected == got