H = int(input("Enter hours (0-11): "))
M = int(input("Enter minutes (0-59): "))
S = int(input("Enter seconds (0-59): "))

angle = 30 * H + 0.5 * M + (0.5 / 60) * S

print(f"The angle of the hour hand is {angle:.2f} degrees.")
