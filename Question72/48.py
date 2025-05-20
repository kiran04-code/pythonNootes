# Program to check if two sets have any elements in common

# Sample sets
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}

# Using intersection to check for common elements
common_elements = set1.intersection(set2)

# Check if intersection is non-empty
if common_elements:
    print("The sets have common elements:", common_elements)
else:
    print("The sets have no elements in common.")