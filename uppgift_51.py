add_as_lambda = lambda a, b: a + b
print(add_as_lambda(4, 4))

obj = lambda s: s.upper()
# samma som
def upper(s):
    obj = s.upper()
    return obj

join_as_lamba = lambda string, inbetween: inbetween.join(string)
# samma som
def join_as_lambda(string, inbetween):
    text = inbetween.join(string)
    return text

print(join_as_lambda("join", "!"))