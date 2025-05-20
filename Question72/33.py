number = [1,2,4,8,9,8,7]

unique_Number = list(set(number))
unique_Number.sort(reverse=True)
if len(unique_Number)>=2:
   secoud_largest_value = unique_Number[1]
   print(secoud_largest_value)

else:
    print("NO second Largest Value is there ")    