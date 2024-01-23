n = input("enter string:")
vowel = 0
constant = 0
for i in n:
    if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u'):
        vowel=vowel+1
    else:
        constant=constant+1
print("No.of Vowel:",vowel)
print("No.of Constant:",constant)            