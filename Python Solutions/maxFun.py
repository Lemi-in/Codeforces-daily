def max_fun(numbers):
    max = numbers[0]

    for number in numbers:
        if number > max:
            max = number
    return max

user = input("Enter numbers: ")
numbers = list(map(int, user.split()))
largest = max_fun(numbers)
print(largest)