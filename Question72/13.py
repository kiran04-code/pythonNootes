year = int(input("Enter The Number:"))

if year%4==0 and (year%100!=0) or(year%400 ==0):
    print(f"{year} Is Leap Year!")
else:
    print(f" This {year} is not the leap Year!")    