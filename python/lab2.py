str_input = input("Enter the string: ")
strigs = ""
for i in range(len(str_input)):
    if i == 0 or i % 3 != 0:
      strigs += str_input[i]
print(strigs)
