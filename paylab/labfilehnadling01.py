with open("kiran.txt", "r") as file:
    line_count = 0
    word_count = 0
    the_count = 0

    for line in file:
        line_count += 1
        words = line.split()
        word_count += len(words)
        the_count += words.count("is")  # Change "is" to match case-sensitively

print("Number of lines in the file:", line_count)
print("Number of words in the file:", word_count)
print("Number of 'is' in the file:", the_count)
