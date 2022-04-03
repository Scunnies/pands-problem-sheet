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

# ### REFERENCES:
# - https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# - https://data-flair.training/blogs/python-function/
# - https://stackoverflow.com/questions/16005123/how-can-i-make-a-recursive-square-root-in-python#:~:text=The%20basic%20strategy%20for%20a,
# the%20true%20root%20to%20return.
# - https://stackoverflow.com/questions/48823833/simple-program-to-find-squre-root-using-recursion/48823931
# - https://beapython.dev/2020/05/14/is-recursion-bad-in-python/#:~:text=Recursion%20can%20be%20considered%20bad,
# calls%20on%20the%20call%20stack.
# - https://stackoverflow.com/questions/4278327/danger-of-recursive-functions