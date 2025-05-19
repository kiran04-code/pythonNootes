# Creating a dictionary it is mutaable!
User_type = {"name":"kiran","email":"kr551344@gmail.com" ,"pass":"969696"}
# print(User_type["names"]) # it return the error when the key is wrrong!
# print(User_type.get("nameS"))  # with this syntax it not give the error when the key is not right
# User_type["name"] ="rathod"
# print(User_type)

#===== first type to print key and values ==============================
# for user in User_type:  # it return the key from the dictonory!!
#     print(user,User_type[user])

# =========== secound type to print key values ====================================

# for key ,value in User_type.items():
#     print(key,value)
#=======================================================================================
# if "name" in User_type:
#     print("Yes!present of masala name is in dictonory!")
# print(len(User_type))
#================================================================================================
# User_type["loggedIN"] = 'true'
# # print(User_type)
# print(User_type.popitem()) # it remove the last key value pair from dictonoty 
