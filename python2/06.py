 #--------------------------------(function)---------------------------------------------------------------------------------------------------------------------------- 
# def number(num1,num2):  #function defination( #formal paramerters)!!
#    sum = num1+num2;     
#    return sum;

# ok = number(14,5)       #function call(#actula paramerters)
# print(ok)
# def Print_hello():
#     print("Hello World!!") # when in function is not pass any parameretr its return  none!
# Print_hello()
#===================================== (avrage ok 3 number) =====================================================================================
# def avg(num1,num2,num3):
#     avgr = num1+num2+num3/3
#     return avgr
# res = avg(2,5,7)

#========================================(function method )====================================================================================
# print("hello","from","kiran",end="")#seprateter is all ready define in this print function =(" ") || end="" for next function in same line 
# print("kiranrathod") # and end is Atomatically assign (\n)
#==========================================(problem 01) =====================================================================================================

# city = ["pune","mumbai","naida","gurgaon","bangluru"]
# print(city[0],end=" ") //end=" " make the element in one line 
# print(city[1],end=" ")
# print(city[2],end=" ")
# print(city[3],end=" ")
# def printlenth(city):
#     print(len(city))
# printlenth(city)
#=================================(Recursion)===============================================================================================================
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(4)    

# def facts(n ):
#     if(n  == 0 and n  == 1):
#         return 1;
#      return   n *facts( n-1)
#    
# mama = facts(5);
# print(mama)
# def facts(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * facts(n - 1)

# mama = facts(5)
# print(mama)
#=================== (problem 02) =================================================================================================================================
# def sum(n):
#     if(n==0):
#         return 0;
#     return n + sum(n-1)
# mama = sum(2)
# print(mama)