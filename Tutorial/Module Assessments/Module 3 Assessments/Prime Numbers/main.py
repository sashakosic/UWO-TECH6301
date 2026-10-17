n = int(input("Enter a number: "))

for num in range(2, n + 1):
    is_prime = True
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num)