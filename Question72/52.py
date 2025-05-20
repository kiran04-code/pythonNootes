def factorial(num):
    if num==0 or num ==1 :
        return 1
    return num*factorial(num-1)

inputs = int(input("Enter The Number:"))
result = factorial(inputs)
print(result)