
def to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

h1 = int(input("Firts_User:Enter Hour:")) 
m1 = int(input("Firts_User:Enter minute:")) 
s1 = int(input("Firts_User:Enter secound:")) 
h2 = int(input("secound_User:Enter Hour:")) 
m2 = int(input("secound_User:Enter minute:")) 
s2 = int(input("secound_User:Enter secound:")) 

 

time1_seconds = to_seconds(h1, m1, s1)
time2_seconds = to_seconds(h2, m2, s2)

difference = time2_seconds - time1_seconds

# Output the result
print("Seconds between timestamps:", difference)