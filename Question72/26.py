num = int(input("Enter The Number:"))
total_digite =0
while num>0:
    count = num%10
    total_digite +=count
    num = num//10

print("sum of digite is:",total_digite) 