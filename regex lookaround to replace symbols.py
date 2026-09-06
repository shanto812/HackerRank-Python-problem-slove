

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Complete the code below:

# Step 1: Read column by column to extract characters
decoded_message = ""
for column in range(m):
    for row in range(n):
        decoded_message += matrix[row][column]

# Step 2: Use regex lookaround to replace symbols/spaces between alphanumerics with a single space
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", decoded_message))
