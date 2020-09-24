from uppgift_36.pwstrength import compute_strength


def test_password_with_length_11_gives_1_point():
    pw = '1' * 11
    assert compute_strength(pw) == 1


def test_password_with_length_5_gives_0_point():
    pw = '1' * 5
    assert compute_strength(pw) == 0


def test_password_with_numbers_and_letters_gives_1_point():
    pw = 'abc123'
    assert compute_strength(pw) == 1


def test_contains_special_characters():
    pw = '###___'
    assert compute_strength(pw) == 1


def test_char_and_letter_and_specialchar_give_2_point():
    pw = 'abc123#_'
    assert compute_strength(pw) == 2


def test_hit_all_3_points():
    pw = 'abc123###___%%%+++&&&---'
    assert compute_strength(pw) == 3


def test_0_points():
    pw = '1'
    assert compute_strength(pw) == 0


def test_illegal_character_give_0_points():
    pw = '123abc###???'
    assert compute_strength(pw) == 0

