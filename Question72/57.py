try:
    with open("kiran.txt", "r") as f:
        data = f.read()        
    print(data)               
except FileNotFoundError:
    print("Error: 'kiran.txt' not found. Make sure it’s in the same folder as your script.")
