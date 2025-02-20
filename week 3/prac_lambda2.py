# Using lambda with map()
nums = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, nums)
print(list(squared))    # [1, 4, 9, 16, 25]

# Using lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = filter(lambda x: x % 2 ==0, numbers)
print(list(even_num))     # [2, 4, 6, 8, 10]

# Using lambda with sorted()
points = [(1, 2), (4, 1), (5, -1), (3, 3)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)    # [(5, -1), (4, 1), (1, 2), (3, 3)]

# Using lambda with reduce()
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)      # 120


# List Comprehension

# Example 1: Creating a list of squares from 1 to 8
squares = [i ** 2 for i in range(1, 9)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64]

# Example 2: Storing only even numbers from 1 to 10 in a list
even = [i for i in range(1, 11) if i % 2 == 0]
print(even)     # [2, 4, 6, 8, 10]

# Example 3: Filtering tuples that satisfy a specific condition
points = [(1, 2), (4, 1), (5, -1), (3, 3)]
filtered_points = [(x, y) for x, y in points if x > 1 and y > 0]
print(filtered_points)  # [(4, 1), (3, 3)]


# Nested List Comprehension

# Example 1: Creating a nested list
nested_lst1 = [[j for j in range(1, 4)] for _ in range(3)]
print(nested_lst1)   # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# Example 2: Creating a list with consecutive numbers
nested_lst2 = [[j + (i - 1) * 3 for j in range(1, 4)] for i in range(1, 4)]
print(nested_lst2)

n2 = []
for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(j + (i-1) * 3)
    n2.append(row)

print(n2)