def add_numbers(a, b):
    return a+b

assert add_numbers(2, 3) == 5, "2 + 3 should equal 5"
assert add_numbers(10, -5) == 5, "10 + (-5) should equal 5"
assert add_numbers(0, 0) == 0, "0+0 should equal 0"
assert add_numbers(-1, 1) == 0, "-1 + 1 should equal 0"