#this programme is to calculate a person's body mass index
# Author: Eleanor Sammon

name = input ("What is your name: ")
print ("Hello " + name) 

#establish the two values required to do the calculation
weight = int (input ("What is your weight in kilograms? "))
height = int (input ("What is your height in centimetres? "))

#perform the calculation
bmi = weight / (height*height) * 10000

#present results
print ("Thank you "+ name + ". Your BMI is " + format(round(bmi, 2)))
#I googled how to keep to two decimal places