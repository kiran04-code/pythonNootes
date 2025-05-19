n = int(input("Enter the number: "))
sumofnum = 0

for i in range(1, n + 1):
    sumofnum += i

average = sumofnum / n

print("Sum:", sumofnum)
print("Average:", average)
