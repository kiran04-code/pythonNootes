#=============================== { (dictionary and set)  } ==========================================================================================================================#
# dictionary is data type thats's store the  key-value paire! it is mutable or there no any proper orderunorder items(there is no index from) or its has  unique key!
# info = {

#       "name":"kiran",
#       "email":"kr551344@gmail.com",
#       "mobile":"7774025744",
#       "PRN": "12413076",
#       "age":35,
#       "IsLoggedin": True

# }
# info["name"] = "karan" # it is mutable as well as call by reference!
# info["age"] = 19
# info["sirname"] = "rathod"
# print(info["sirname"]) 
#======================================(Nested Dictinary)==============================================================================================
# studet = {
#     "name":"kiran",
#     "sub" :{
#        "phy":47.60,
#        "che":98.06,
#        "math":94.03,
#        "total":94.03
#     }
# }
# print(studet["sub"]["total"])
# print(list(studet.keys()))
# print(len(list(studet.keys())))
# print(list(studet["sub"].keys()))     # it's give  the key of value
# print(list(studet["sub"].values()))   # it's give  the value of key
# print(list(studet["sub"].items()))    # it's give  the key in tuple from
# print(studet.get("name"))             # it's give value of the perticular keys that you passed in get 
# print(studet.update({"sirname" : "rathod"})) # its help to update the new key and paires!!
# print(studet)
 
#======================================={set}=====================================================================================================================
# sets = { 1 , 2 , 5 } # it is collection of unorder items(there is no index from) or the iteam is mutable or unique but there  elment is immutable
# print(len(sets))# finds the length of sets
# set1 = {1,2,3,5}
# set2 = {2,3,4,5}
# emptyset = set() # it's is empty sets!!
# emptyset.add(5)
# emptyset.add(2)
# emptyset.add((1,2, 4, 5 ,7)) # we can add the tupes 
# emptyset.add("kiran")          #  we can add string!
# emptyset.add(4)                #  add value in sets
# emptyset.add(4)                #  same value is invalid in sets
# emptyset.remove(4)             #  remove value in sets 
# emptyset.clear()               #  its clear the set
# emptyset.pop()                 #  its remove the random value 
# print(set1.union(set2))        #  combines both  different set value & return new
# print(set1.intersection(set2)) #  combines both  common value & return new 
#================================= practice Questions  -->01      ============================================================================ 