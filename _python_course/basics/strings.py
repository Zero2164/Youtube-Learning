# print("\033c", end="")

# ----new lines in Strings example----
# print("String\nhaha")

# storing Variables example
# phrase = "String\nhaha"
# print(phrase)

# ----Strings and Variables concatenation example----
# phrase = "Strings"
# print(phrase + 'are cool')


# ----String Functions example----
# import time function
# from hashlib import new
# import numbers
# import time
# from tokenize import maybe

# phrase = 'Strings'

# # String to Lowercase function with lower()
# print('This string is in lowercase:',phrase.lower())

# # Test if String is uppercase with isupper()
# print('String Uppercase?',phrase.isupper())

# print('Converting to uppercase....')
# # call time.sleep() and enter a perameter to sleep for x seconds
# time.sleep(2)

# # convert the String to uppercase with upper() function, 
# # then save to the 'phrase' variable
# phrase = phrase.upper()

# # Test if String is uppercase
# print('String Uppercase?',phrase.isupper())
# time.sleep(1)

# print('Counting String Characters....')
# # call time.sleep() and enter a perameter to sleep/pause code for x seconds
# time.sleep(2)

# # Return a numbered-length for the number of characters within the parameter String
# print('This the number of Characters in the String are:', len(phrase));

# time.sleep(1)
# print('Printing the String-Character at the Index of the specified number....')
# # call time.sleep() and enter a perameter to sleep/pause code for x seconds
# time.sleep(2)

# # Indexing Lookup Function
# #  Parse a number to square-brackets[] to return the String-Character 
# #   at the position of the specified number
# print('Here is the Character at position two: ', phrase[2])
# time.sleep(1)

# print('Printing the Index number of the specified String-Character ....')
# # call time.sleep() and enter a perameter to sleep/pause code for x seconds
# time.sleep(2)

# # Index function example
# # Parse a String-Character to the index() function to return 
# # the index numerical position of that charcter
# letter = "G"
# print('Here is the Index number for letter',"'"+letter+"'",'in the phrase String:', phrase.index(letter))

# time.sleep(1)

# # Replace function example
# replce_txt = "Your String Variable Has Been Replaced!"
# # Parse the characters or String for the first parameter, 
# # then, parse a String to replace what was parsed in the first parameter
# print('You String called:', phrase+'. Will be replaced in 2 seconds...')
# time.sleep(2)
# print(phrase.replace(phrase, replce_txt))
# phrase = replce_txt

# time.sleep(1)

# print('Exiting running code in 10 seconds....')
# # sleep/pause for 10 seconds
# time.sleep(10)

# # clear the console window
# print("\033c", end="")