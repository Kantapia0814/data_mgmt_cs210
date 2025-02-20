from typing import Tuple

# Using Type hint
def sort_three_numbers(a: int, b: int, c: int) -> Tuple[int, int, int]:
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return a, b, c

x, y, z = sort_three_numbers(3, 1, 2)
print(x, y, z)

# Test cases using assert
assert sort_three_numbers(3,1,2) == (1,2,3)
assert sort_three_numbers(3,2,1) == (1,2,3)
assert sort_three_numbers(2,1,3) == (1,2,3)
assert sort_three_numbers(2,3,1) == (1,2,3)
assert sort_three_numbers(1,3,2) == (1,2,3)
assert sort_three_numbers(-1,-1,-1) == (-1,-1,-1)

def test_sort_three_numbers():
    test_cases = [
        ((3, 2, 1), (1, 2, 3)),
        ((1, 2, 3), (1, 2, 3)),
        ((3, 1, 2), (1, 2, 3)),
        ((1, 3, 2), (1, 2, 3)),
        ((2, 1, 3), (1, 2, 3)),
        ((2, 3, 1), (1, 2, 3))
    ]

    for i, (inputs, expected) in enumerate(test_cases):
        # Tuple unpacking
        result = sort_three_numbers(*inputs)
        assert result == expected, f"Test case {i + 1} failed: input({inputs}) => output({result}), expected({expected})"

    print("All test cases passed!")

test_sort_three_numbers()

# Using assert for postcondition in a function
def sort_three_numbers_v2(a: int, b: int, c: int) -> Tuple[int, int, int]:
    # Preconditions: check that all inputs are integers
    assert isinstance(a, int), "Input 'a' must be an integer"
    assert isinstance(b, int), "Input 'b' must be an integer"
    assert isinstance(c, int), "Input 'c' must be an integer"

    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b 

    # Postcondition: check that the result is in ascending order
    assert a <= b <= c, "Result is not in ascending order"

    return a, b, c

def test_sort_three_numbers_v2():
    test_cases = [
        ((3, 2, 1), (1, 2, 3)),
        ((1, 2, 3), (1, 2, 3)),
        ((3, 1, 2), (1, 2, 3)),
        ((1, 3, 2), (1, 2, 3)),
        ((2, 1, 3), (1, 2, 3)),
        ((2, 3, 1), (1, 2, 3))
    ]
    for i, (inputs, expected) in enumerate(test_cases):
        result = sort_three_numbers_v2(*inputs)
        assert result == expected, f"Test case {i + 1} failed: input({inputs}) => output({result}), expected({expected})"

    print("All test cases passed!")

test_sort_three_numbers_v2()