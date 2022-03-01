# this program takes a positive floating-point number 
# as input and outputs an approximation of its square root

#Author: Eleanor Sammon

# read in the variables needed to perform the calculation
num = int(input("Enter a number: "))
given = num/2
tol = 0.0001

# this function will loop the iteration until the tolerance is reached
def sqRoot(x):
    if((x * x > num - tol) and (x * x <= num + tol)):
        return x
    x = (x + num/x)/2
    return sqRoot(x)

# call the function
root = sqRoot(given)

# rounding the output so that it is more approximate!
roundRoot = round(root, 2)

print("The square root of {} is approximately {}".format(num,roundRoot))