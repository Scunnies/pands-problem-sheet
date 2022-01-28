#this programme is to calculate a person's body mass index
# Author: Eleanor Sammon

Name = input ("What is your name: ")
print ("Hello " + Name) 

#establish the two values required to do the calculation
Weight = int (input ("What is your weight in kilograms? "))
Height = int (input ("What is your height in centimetres? "))

#perform the calculation
BMI = Weight / (Height*Height) * 10000

#present results
print ("Thank you "+ Name)
print ("Your BMI is " + format(round(BMI, 2)))
#I googled how to keep to two decimal places and found the answer on TuturialDeep.com