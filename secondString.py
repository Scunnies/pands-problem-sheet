#user inputs a string, program outputs every second letter in reverse order
#author: Eleanor Sammon

#ask the user to type a sentence
sentence = input("Please type a sentence: ")

#slice the string
#step it backwards by two places each time
#print the result
print(sentence[::-2])