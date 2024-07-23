import numpy as np
from functools import reduce
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squared_even_numbers = list(map(lambda x: x ** 2, even_numbers))
product = reduce(lambda x, y: x * y, squared_even_numbers)
print(product)  # Output: 256