def compute_strength(pw):
    special_chars = ['#', '%', '&', '+', '_', '-']
    points = 0
    if len(pw) >= 10:
        points += 1
    if any(c.isalpha() for c in pw) and any(c.isnumeric() for c in pw):
        points += 1
    if any(i in pw for i in special_chars):
        points += 1
    for c in pw:
        if c not in special_chars and not c.isnumeric() and not c.isalpha():
            points = 0

    return points
