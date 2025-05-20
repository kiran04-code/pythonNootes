with open("kiran.txt","r") as f :
   line_count = 0
   words_count = 0
   the_count = 0

   for line  in f:
      line_count+=1
      words = line.split()
      words_count+=len(words)
      the_count += words.count("is")
print("Number of lines in the file:", line_count)
print("Number of words in the file:", words_count)
print("Number of 'is' in the file:", the_count)
