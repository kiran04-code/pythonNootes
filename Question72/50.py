def check_Odd_even(number):
    if number%2==0:
        return "Even"
    else:
        return "ODD"
    
data = int(input("Enter The Number:"))    
result = check_Odd_even(data)
print(result)