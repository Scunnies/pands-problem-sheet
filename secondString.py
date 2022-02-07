#user inputs a string, program outputs every second letter in reverse order
#author: Eleanor Sammon

#ask the user to type a sentence
sentence = input("Please type a sentence: ")

#I found this solution using W3 schools
# slice the string by NOT entering a start or end character
# showing only every second letter in reverse order
#print the result
print(sentence[::-2])