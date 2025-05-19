from datetime import datetime

date_input = input("Enter a date (DD-MM-YYYY): ")

try:
    valid_date = datetime.strptime(date_input, "%d-%m-%Y")
    print(f"{date_input} is a valid date.")
except ValueError:
    print(f"{date_input} is NOT a valid date.")
