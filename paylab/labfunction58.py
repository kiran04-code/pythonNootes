def fact(num):
    if num == 0 or num == 1:
        return 1
    return num * fact(num - 1)
num = int(input("Enter The Number:"))
result = fact(num)
print(f"Factorial of {num} is {result}")
