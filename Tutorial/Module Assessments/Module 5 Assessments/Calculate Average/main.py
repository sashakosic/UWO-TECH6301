def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

def main():
    items = [10, 20, 30, 40, 50]
    result = calculate_average(items)
    print(result)
    return result

main()
