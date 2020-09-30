# med f string
tal = 5
datum = "2020-01-01"
value = 5.6

print(f"tal: {tal}, datum {datum}, värde: {value}")

print(f"hello {tal:0}")

# med .format()
tal = 5
datum = "2020-01-01"
value = 5.6

print("tal: {:20}, datum {}, värde: {}".format(tal, datum, value))

print(f"hello {tal:0}")

# med %s/d
tal = 5
datum = "2020-01-01"
value = 5.6

print("tal: %20d, datum %s, värde: %f" % (tal, datum, value))

print(f"hello {tal:0}")