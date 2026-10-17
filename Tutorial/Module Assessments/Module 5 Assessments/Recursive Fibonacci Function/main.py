def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    count = int(input("How many Fibonacci numbers? "))
    for i in range(count):
        print(fibonacci(i))

main()