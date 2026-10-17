import random

numbers = [random.randint(1, 100) for _ in range(10)]
print("Original list:", numbers)

for i in range(1, len(numbers)):
    current = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] > current:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = current

print("Sorted list:", numbers)