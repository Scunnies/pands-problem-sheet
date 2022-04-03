#user inputs a string, program outputs every second letter in reverse order
#author: Eleanor Sammon

#ask the user to type a sentence
sentence = input("Please type a sentence: ")

#I found this solution using W3 schools
# slice the string by NOT entering a start or end character
# showing only every second letter in reverse order
#print the result
print(sentence[::-2])

# references:
# - https://realpython.com/reverse-string-python/
# - https://www.w3schools.com/python/gloss_python_string_slice.asp
# - https://stackoverflow.com/questions/36003289/- - - 
# write-programs-that-read-a-line-of-input-as-a-string-and-print-every-second-lett