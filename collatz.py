# this program reads in any positive integer 
# and outputs successive values 
# if it is even, divide it by two
# if it is odd, multiply it by three and add one
# program ends if the current value is one

# ask user to input a positive integer
userint = int(input("Enter an integer: "))

# allow for a correction if they put in a minus number
while userint < 0:
  print("Sorry, your number must be greater than 0.")
  userint = int(input('Enter a positive integer: '))



# use def to create a user defined function called collatz
# and implement the calculations



def collatz(number):
  lst=[] # the list into which our calculations will be appended
  lst.append(number)
  
  while(number!=1):  #execute while loop until output value equals 1
    if(number%2==0): # if the number is divisible by 2
        number=number//2
        lst.append(number) # adds the number to the list
    else:
        number=number*3+1 # if the number is uneven
        lst.append(number)
  print(*lst, sep=", ") # to show our list without the square brackets


collatz(userint) #runs our user-defined number through the programme


# references:
# https://www.educative.io/edpresso/how-to-implement-the-collatz-sequence-in-c-and-python
# https://www.pythonpool.com/collatz-sequence-python/
# https://www.educative.io/edpresso/how-to-implement-the-collatz-sequence-in-c-and-python
# https://arxiv.org/abs/1902.07312
# https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
# Sweigart, A., *Automate the boring stuff with python*, Chapter 3. 