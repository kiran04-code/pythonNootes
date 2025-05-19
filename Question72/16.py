string_input = input("Enter The Name:")

dummy_string = ""

for i in range(len(string_input)):
    if i == 0 or i % 3==0:
        dummy_string += string_input[i]
print(dummy_string)        