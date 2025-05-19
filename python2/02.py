#String--> its Storethe squence of Charecter!
#=================================== concatination ===============================================================================================================
# str1= "kiran"
# str2= "rathod"
# sumstr = str1+" "+str2;
# print(sumstr)
#================================== length  of String ============================================================================================================
# str = "kiran"
# strle = len(str)
# print(strle)
#=================================  indexsing    =================================================================================================================
# str = "kiran"
# ch = str[2]
# print(ch)
#=============================     slicing     ===================================================================================================================
# breking of the string in python this concept called slicing
# str[starting_index:Ending_index]# is give word in between but Ending_index not incude
# str = "kiran"
# ch = str[0:4] #(its retrun string from this index (0,1 , 3 ,) (kira))  Ending_index not incude
# print(ch)
#============================== string functions ==============================================================================================================
# str = "kiran"
# var = str.endswith("n")    # its check eding is same or nor is same its give true .| false value!
# var = str.capitalize()     # its make the first words word capital!
# var = str.replace("k","r") # its replace value! from old to new!
# var  = str.find("kiran")   # its find the string in origin string and return the first index!
# var = str.count("a")       # its give the how  many time the word is in this sentance!
#================================= practice Quesions ==========================================================================================================
# str = input("Enter Your Name:")
# ch = len(str)
# print("The Length of your number:",ch)
# str = input("Enter Your Name:")
# ch = str.count("$")
# print(ch)
#================================= conditinal statement ========================================================================================================
# light = "green"
# if(light == "red"):
#     print("Stop")
# elif(light== "green"):
#     print("Go")
# elif(light=="Yellow"): // indentation{}
#     print("Look")
# else:
#     print("helo")

#======================================================#
# strm = int(input("Enter the marks :"))
# marks = strm
# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"
# print("Grade of Student of is ==>",grade)

#======================================================#
# inp = int(input("Enter the Number: "))
# remp = inp % 2
# if(remp == 0):
#     print("The Above Number is  even")
# else:
#     print("The Number is odd")
#======================================================#
# inp1 = int(input("Enter The Number:"))
# inp2 = int(input("Enter The Number:"))
# inp3 = int(input("Enter The Number:"))
# if(inp1>inp2 and inp1>inp3):
#     print("First Number is Largest")
# elif(inp2>inp1 and inp2>inp3):
#     print("Secound Number is Largest")
# elif(inp3>inp2 and inp3>inp1):
#     print("Third Number is Largest")
#=======================================================#
# int1 = int(input("Enter The Number:"))
# rem = int1%7
# if(rem==0):
#     print("IT is a Mutiple of 7")
# else:
#     print("Is not Multiple of 7")
