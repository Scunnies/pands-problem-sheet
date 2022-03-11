# program that outputs whether or not today is a weekday
# Author: Eleanor Sammon


# For today's date use the datetime.today() function 
# from imported datetime module and weekday() function 
# to get the week number from the date

 
# Import Module
import datetime


# To Get the Week Number
weekNumber = datetime.datetime.today().weekday()


# if the week number is greater than 5 then it's a weekend otherwise it is a weekday
if weekNumber < 5:
    print("Get ready for work! Today is a weekday")
else:
    print ("You can relax! It's the weekend")