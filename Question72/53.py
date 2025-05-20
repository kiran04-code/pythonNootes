def sum_of_digite(num):
     if num == 0:
        return 0
     
     return (num%10 )+ sum_of_digite(num//10)

data = int(input("Enter The Number:"))
result = sum_of_digite(data)

print(result)
