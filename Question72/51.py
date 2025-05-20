def find_max(num1,num2):
    if num1>num2:
        return "Num1 is Greter Than Num2"
    else:
        return "Num1 is less Than num2"
    
data1 = int(input("Enter The number :"))    
data2 = int(input("Enter The number :"))    
result = find_max(data1,data2)
print(result)