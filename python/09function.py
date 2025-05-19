#============================================= 01 =====================================================================================================================================
# num = int(input("Enter the Number:"))
# def sqaure_num(num):
#     return num*2
# result  = sqaure_num(num)
# print(result)
#=========================== 02 ==========================================================================================================================
# num1 = int(input("Enter The Number:"))
# num2 = int(input("Enter The Number:"))
# def multiparam(num1,num2):
#     return num1*num2
# result  = multiparam(num1,num2)
# print(result)

#=============================03=========================================

# str = input("Enter The string:")
# num = int(input("Enter The Number:"))

# def multipy_str(str,num):
#     return str*num

# result = multipy_str(str,num)
# print(result)
#===================================04=========================================
# import math

# r = int(input("Enter the radius: "))

# def circle_stats(r):
#     area = math.pi * r ** 2
#     circumference = 2 * math.pi * r
#     return area, circumference

# area, circumference = circle_stats(r)

# print(f"Area: {area:.2f}")
# print(f"Circumference: {circumference:.2f}")

#========================================== 05 ==============================================================================================================
# name = input("Enter The Name:")
# def greet(name ="radhe"):
#     return "hello," + name +"!"
# result = greet(name)
# print(result)
#====================================== 06 ===============================================================
# cube  = lambda x:x**3 # it function in one line!
# print(cube(2))
#======================================= 07 ===========================================================
# def sum_all(*args):  # its give the multiple arguments! 
#     return sum(args)
# print(sum_all(1,2,4,7,8,5,9,6,3))

#========================================08==============================================================
# def print_kwargs(name,power):
#     print("Name:", name,",power:",power)
# print_kwargs(name="kiran",power="normalperson")  
#=========================================09==============================================================
# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1
# counter = count_up_to(3)
# for number in counter:
#     print(number)
 
#========================================10==================================================================
# num = int(input("Enter The Number: "))

# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     return num * factorial(num - 1)

# result = factorial(num)
# print("Factorial:", result)
#================================= end of function ==============================================================