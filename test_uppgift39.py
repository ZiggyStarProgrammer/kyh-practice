from uppgift_39 import max, sum_all, mul_all

def test_max():
    expected = 8
    got = max(1, 8, 4)
    assert expected == got


def test_sum_all():
    expected = 6
    got = sum_all([3, 3])
    assert expected == got


def test_mul_all():
    expected = 6
    got = mul_all([2, 3])
    assert expected == got
