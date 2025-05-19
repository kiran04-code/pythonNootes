num1 =int(input("Enter The Number:"))
num2 =int(input("Enter The Number:"))
num3 =int(input("Enter The Number:"))

if num1>num2 and  num1>num3:
 maximum = num1
elif num2>num1 and num2>num3:
 maximum =  num2
else:
 maximum = num3 

print(f"Maximum Number in above number is :{maximum}")

