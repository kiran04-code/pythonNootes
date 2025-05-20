list = [1,2,3,4,5,6,7,8,9,10]
Even = []
odd = []
for i in range(len(list)):
    if list[i] %2==0:
        Even.append(list[i])
    else:
        odd.append(list[i])
print(Even)           
print(odd)           