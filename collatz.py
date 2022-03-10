# this program reads in any positive integer 
# and outputs successive values 
# if it is even, divide it by two
# if it is odd, multiply it by three and add one
# program ends if the current value is one

# ask user to input a positive integer
userInt = int(input("Enter an integer: "))

# allow for a correction if they put in a minus number
while userInt < 0:
  print("Sorry, your number must be greater than 0.")
  userInt = int(input('Enter a positive integer: '))



# use def to create a user defined function called collatz
# and implement the calculations
def collatz(number):
    if number % 2 == 0:  # for even numbers
       return number // 2
    
    elif number % 2 == 1:  # for odd numbers
       return 3 * number + 1
       
# execute while loop until output value equals 1
while userInt != 1:
  userInt = collatz(userInt)

# print values derived from the original input
  print(userInt, end=" ")