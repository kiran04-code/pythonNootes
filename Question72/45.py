dict_1 = {
    "a":"2",
    "b":"1",
    "c":"3"
    }
dict_2 = {
    "t":"2",
    "e":"1",
    "d":"3"
    }
dict_3 = {
    "k":"2",
    "u":"1",
    "o":"3"
    }

new_dist = {**dict_1,**dict_2,**dict_3}
print(new_dist)