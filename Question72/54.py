def find_Number_of_vowels(chars):
    vowels = ["a","e","i","o","u"]
    count =  0
    for char in chars:
        if char in vowels:
          count += 1 
    return count      

inputs = input("Enter The Name:")
result = find_Number_of_vowels(inputs)
print(result)
