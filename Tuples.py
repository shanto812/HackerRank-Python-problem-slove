# Read the number of elements
n = int(input())

# Read the space-separated integers and convert to tuple
numbers = tuple(map(int, input().split()))

# Compute and print the hash value
print(hash(numbers))
