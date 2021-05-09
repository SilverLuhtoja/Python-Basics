
# user_name = input("Enter your name:")
# print(f"{user_name.upper()}")

# Len method
sentence = "This text has this much letters"
print(len(sentence))
#  index method
findThisChar = "AEMMKSOCXZPRIWOEKSMFPEWKGJNBVMKJQ"
print(findThisChar.index("Q"))

# Get char in that number spot
spotNr5 = "Birthday"
print(spotNr5[4])
# Extracts substring from the string
print(spotNr5[5:8])
print(spotNr5[-3:])
# Extracts substring from the string, omitting every second character
print(spotNr5[0:8:2])
print(spotNr5[::3])
# Prints characters in reverse order (from start to end, reverse every letter starting from end)
print(spotNr5[::-1])

# .upper method & .lower method
kity = "CATENHOF"
woofy = "blenderkush"
kityLow = kity.lower()
woofyUp = woofy.upper()
print(kityLow,woofyUp,sep="-")
# count method
# print(user_name.count('a'))
print("This sentenc has ", input("Enter your sentence:").lower().count('a')," a's in it." )


