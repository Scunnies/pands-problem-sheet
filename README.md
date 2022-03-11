# Pands Problem Sheets - Weekly solutions
## This is my repository for weekly problem sheets containing solutions to problems and supporting references

### Eleanor Sammon
### Student ID: G00411277


## Week 2 Task – bmi.py

This program calculates a person’s Body Mass Index (BMI). The inputs are the person's height in centimeters and weight in kilograms.  The output is their BMI.

The formula for BMI is weight in kilograms divided by height in meters squared. Since the height input here is in centimeters, I modified the calculation formula, dividing the weight in kilograms by the height in centimeters squared and multiplying the result by 10,000 to achieve the correct output. 

I then researched how to keep the result to two decimal places. 

### REFERENCES:
- https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html
- https://tutorialdeep.com/knowhow/round-float-to-2-decimal-places-python/
- https://www.code4example.com/python/body-mass-index-code-in-python/

 
## Week 3 Task – secondstring.py

This program asks a user to input a string and outputs every second letter of the given string in reverse order.

At first a daunting task, I found the real python website a huge help and it explained the process very well.  I didn’t specify a start or end point so the program reads in the whole string and steps it back (-2), printing every second character of the given sentence in reverse order. 

### REFERENCES:
- https://realpython.com/reverse-string-python/
- https://www.w3schools.com/python/gloss_python_string_slice.asp
- https://stackoverflow.com/questions/36003289/write-programs-that-read-a-line-of-input-as-a-string-and-print-every-second-lett

 
## Week 4 Task – collatz.py

This program asks the user to input any positive integer and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.  The program ends if the current value is one.

I created a function that had one parameter `number` which, depending on whether the number was even or odd, would return a value and keep calling the function on that number until a value of 1 was returned. 

### REFERENCES:
- https://www.educative.io/edpresso/how-to-implement-the-collatz-sequence-in-c-and-python
- https://www.pythonpool.com/collatz-sequence-python/
- https://www.educative.io/edpresso/how-to-implement-the-collatz-sequence-in-c-and-python
- https://arxiv.org/abs/1902.07312
- Sweigart, A., *Automate the boring stuff with python*, Chapter 3. 

## Week 5 Task – weekday.py

This program outputs whether today is a weekday.

The first step in this program was to `import datetime`.  From this module, in order to establish today's date, I used the `datetime.today` function and also the `weekday` function to establish the week number.  Then, based on Monday to Friday being numbered 1 – 5, I checked `if` the week no. is greater than 5 then it’s a weekend `else` it is a weekday.

In my output I also assumed that the user works Monday to Friday!

### REFERENCES:
- https://www.geeksforgeeks.org/python-program-to-find-day-of-the-week-for-a-given-date/
- https://www.geeksforgeeks.org/python-datetime-module/
- https://www.tutorialsrack.com/articles/324/how-to-find-the-current-day-is-weekday-or-weekends-in-python
 
## Week 6 Task – squareroot.py

This program takes a positive floating-point number as input and outputs an approximation of its square root.  We were asked to create our own function and not to use the built-in functions x ** .5 or `math.sqrt(x)`.

I struggled a lot just to get my head around the concept of approximating a square root, never mind coding it, never mind not being able to use the obvious functions in Python of math.sqrt. 

I thought recursion was a good option when I read about it, this is when a function calls itself in its own body until the set tolerance is reached.  A guess is made of the square root which is checked for accuracy against the actual square root by squaring it and making the difference, or tolerance, a small number, in this case 0.001.  If the guess isn’t accurate enough a new guess is created and so the programme keeps performing this calculation recursively until the guess comes within the tolerance and the recursion and function ends. 

I understand that some schools of thought that recursion is a poor approach in Python because it’s perceived as slower than an iterative solution and because Python's recursion depth is limited to 1000 and there is potential for stack overflow (although the recursion depth can be reset to a higher number).  Having researched opinions on the use of recursion I felt that it was appropriate to use it for this particular task and also, if nothing else, I learned a lot.

### REFERENCES:
- https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
- https://data-flair.training/blogs/python-function/
- https://stackoverflow.com/questions/16005123/how-can-i-make-a-recursive-square-root-in-python#:~:text=The%20basic%20strategy%20for%20a,the%20true%20root%20to%20return.
- https://stackoverflow.com/questions/48823833/simple-program-to-find-squre-root-using-recursion/48823931
- https://beapython.dev/2020/05/14/is-recursion-bad-in-python/#:~:text=Recursion%20can%20be%20considered%20bad,calls%20on%20the%20call%20stack.
- https://stackoverflow.com/questions/4278327/danger-of-recursive-functions
 
## Week 7 Task

This program counts the occurrences of the letter ‘e’ in a text file of my own creation.  I made the assumption that I could select my own text.

I created a text file called ‘poem.txt’ and containing the poem Do Not Go Gentle Into that Good Night by Dylan Thomas and read it in as an argument, read only.  

For the purposes of the exercise I assumed that all instances of the letter ‘e’ should be counted, both uppercase and lowercase and had to specify accordingly in my code. 

Initially I had over-coded this and ran into difficulties straightaway.  I had mistakenly thought from my research that the program would have to read my text line by line.  Taking away a couple of lines and simplifying it meant that it ran better for me. 

The program iterates through code in the `for` loop detecting and counting lowercase and uppercase instances of the letter ‘E’, of which there are a total of 79. 

### REFERENCES:
- https://stackoverflow.com/questions/18647707/count-letters-in-a-text-file
- https://www.delftstack.com/howto/python/occurrences-of-a-character-in-a-string-in-python/
- https://www.cs2study.com/wp-content/uploads/2021/03/Text-File-exam-based-questions.pdf
- https://www.sanfoundry.com/python-program-read-file-counts-number/


## Ancillary references for readme file:
- https://www.makeareadme.com/
- https://code.visualstudio.com/docs/languages/markdown
- https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/


## **WITH THANKS TO:**
### Andrew Beatty


