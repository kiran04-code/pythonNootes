def find_vowels(chars):
    vowels  = ["a","e","i","o","u"]
    count = 0
    for char in chars :
      if char in vowels:
         count+=1
    return count 

chars = input("Enter The Name To Find vowels:").lower()   
result =  find_vowels(chars)
print(f" your Name is {chars} Number of  vowels is :{ result} ")