# ================================== find nigative number! =========================================================================================================
# number = [1,-2,3,-4,5,-6,7,-8, 9 ,-10]
# positive_number_count = 0
# for num in number:
#     if num>0:
#         positive_number_count +=1

# print("Final Count is:",positive_number_count)        
# =================================== 02 sum of all even number! ==============================================================================================================
# n = int(input("Enter The Number:"))
# sum_even = 0
# for i in range(0,n+1):
#     if i%2 ==0:
#         sum_even +=i
       
# print(sum_even)  
# =================================== 03 table  input number! but skip teh itreation of 5th ==============================================================================================================  
# n = int(input("Enter The Number:"))
# for i in range(1, 11):
#     if i == 5: 
#         continue
#     table = i * n
#     print(f"{n} x {i} = {table}")
         
# ========================================== 04 reverse_strings  ===============================================================================
# str = input("Enter The Numeber:") 
# str_reverse = ""
# for char in str:
#     str_reverse = char + str_reverse 
# print(str_reverse)    
# ========================================  05 print char it is only once in the string! ==================================================================================================
# input_str = "teeter"   
# for char in input_str:
#     print(char)
#     if input_str.count(char) == 1:
#         print("char is" ,char)
#         break

# ========================================= 06 find the factorial of the number! ==============================================================================================================
# ======================== for looops! ===========================================
# n = int(input("Enter The number:"))
# fact = 1
# for i in range(1, n + 1): 
#     fact *= i   
# print(f"The factorial of {n} is {fact}")
# =================== while loops  =================================================
# origina_n  = n
# while n>0:
#     fact = fact *n
#     n = n-1
    
# print(f"The factorial of {origina_n} is {fact}")   
# ====================================== 07 validate input ====================================================================

# while True:
#     nums = int(input("Enter The Numberb/w 1 and 10 :"))
#     if 1<=nums<=10:
#         print("Thanks")
#         break
#     else:
#         print("Invalid Number,try Again")  
  
# ====================================== 08 prime Number Checker! ====================================================================
# nums = int(input("Enter The Number:"))


# if nums>1:
#     for i in range(2,nums):
#         if (nums%i) ==0:
#             print(f"Yes! {nums} Number is ordinory number!")  
           
#             break
#         else:
#             print(f"Yes {nums} Number is Prime ")    
#             break
        
#================================================= 09 find unique in the list  =======================================================================================================   
# Iteams = ["apple","banana","orange","mango"]
# Uique_item = set(Iteams)
# if(len(Uique_item) == len(Iteams)):
#     print("No Unique elment this list")
# else:
#     print("Yes have same element is list!")    
# ================================================= 10  ==============================================================================================================================



    
           