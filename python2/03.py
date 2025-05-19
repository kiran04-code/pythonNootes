#{{{{{{{{{{{{{{{ lists }}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
# list is same like arrys one things is diffrent is arrys store the same data type Element and the list is Store multiple data type 
# marks  = [75, 85,96, 99, 87, 92,1 ];
# print(marks.pop()) #it's remove the elment from there end 
# marks[0] = "kiran" #It is multable(it is Changeable)
# mm = marks[1:4] #slicing #ending INDEX is not Include!!
# print(mm)
# print(marks)
# var = marks.append(77) # it append element at the end of list
# var = marks.sort()# it's sort the value in Assending Order by Defoult
# var = marks.sort(reverse = True) #It's sort the element in dessending order
# var = marks.reverse() #Its help to reverse the list
# var = marks.insert(0,2) #its help to add elmet in the perticular index!!
# var = marks.remove(1) #its help to remove the assing in list 
# var = marks.pop(0)   # its help to remove the elment in there perticular index! 
# print(marks) 
#{{{{{{{{{{{{{{{  tuple }}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
# A built-in datatype thats lest us create Immutable sequence of value 
# tup  = (87)  # is simpel on interger <class 'int'>
# tup1 = (87,) # is a tuple 
# print(tup1) # <class 'tuple'>
# print(tup) # <class 'tuple'>
# print(type(tup1))
# print(type(tup))
# tupl= (1 , 5 ,4, 4 ,8 , 9 , 7 )
# var = tupl.index(1) # its help to give index of value thats present in tuble 
# var = tupl.count(4) #its helip to give how may time value is given in the tuple 
# print(var)
#================================= practice Questions  -->01 ============================================================================
# inp1= input("Enter The 1st name:")
# inp2= input("Enter The 2nd name:")
# inp3= input("Enter The 3rd name:")
# movie = []
# var = movie.append(inp1)
# var = movie.append(inp2)
# var = movie.append(inp3)
# print(movie)
#================================= practice Questions  -->02 ============================================================================
# list1  =  [1,2,3,2,1]
# copy01 =  list1.copy()
# copy01.reverse()
# if(copy01 == list1):
#     print("palindrom!")
# else:
#     print("Not Palimdrom!")
#================================= practice Questions  -->03============================================================================
# Grade = ("C","D","A","A","B","B","A")
# CONST = Grade.count("A")
# print(CONST)
#================================= practice Questions  -->04 ============================================================================
# lis = ["C","D","A","A","B","B","A"]
# lis.sort()
# print(lis)