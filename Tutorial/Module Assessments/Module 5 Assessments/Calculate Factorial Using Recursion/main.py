def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    number = int(input("Enter a number: "))
    result = factorial(number)
    print(result)
    return result

main()