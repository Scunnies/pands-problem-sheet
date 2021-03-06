# this program reads in a text file and outputs the number of e's it contains
# Author: Eleanor Sammon
# my data file is called mobydick.txt
# I have assumed that all instances of 'e's are to be counted


# read in the filename, 'read' only from the command line
import sys
filename = open(sys.argv[1]) #the first argument being the filename itself, second argument is file to be read in


with filename as f:
    count = 0 # define count and set to zero
    word = f.read() # read in the contents of the file 
    for w in word:  
        if w[0] =='e' or w[0]=='E': # count lower and upper case occurences of letter E
            count = count+1 # adds them up until it reaches the end of the text
 
print(count)





# https://www.sanfoundry.com/python-program-read-file-counts-number/
# https://stackoverflow.com/questions/18647707/count-letters-in-a-text-file
# https://www.delftstack.com/howto/python/occurrences-of-a-character-in-a-string-in-python/
# https://www.cs2study.com/wp-content/uploads/2021/03/Text-File-exam-based-questions.pdf
