# Question-026 : Make a script that prints out letters of English alphabet from a to z, one letter per line in the terminal. **

# Question-027 : The code produces an error. Please understand the error and try to fix it

print(type("Hey".replace("ey","i")[-1])

# Question-028 : The code is supposed to ask the user to enter their name and surname and then it prints out those user submitted values. Instead, the code throws a TypeError. Please fix it so that the expected output is printed out.
 		    

firstname  = input("Enter first name: ")
secondname = input("Enter second name: ")
print("Your first name is %s and your second name is %s" % firstname, secondname)

Expected output: Your first name is John and your second name is Smith 

# Question-029 : Print out the last name of the second employee.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
     "owners":  [{"firstName": "Jack", "lastName": "Petter"},
                {"firstName": "Jessy", "lastName": "Petter"}]}

Expected output: Smith 

# Question-030: Make a script that prints out numbers from 1 to 10

Expected output:
1
2
3
4
5
6
7
8
9
10

# Question-031 : Create a function that calculates acceleration given initial velocity v1, final velocity v2, start time t1, and end time t2. The formula for acceleration is: a = (v2-v1) / (t2-t1) call the function by inputting values 0, 10, 0, 20 for v1, v2, t1, and t2 respectively

Expected output: 0.5

# Question-032 :  Why is there an error in the code and how would you fix it?

def foo(a, b):
    print(a + b)

x = foo(2, 3) * 10

# Question-033 : Why do you get an error and how would you fix it?

def foo(a=2, b):
    return a + b

# Question-034 : Why is there an error in the code and how would you fix it?

def foo(a=1, b=2):
    return a + b

x = foo - 1

# Question-034: What will the following script output? 

c = 1
def foo():
    return c
c = 3
print(foo())

# Question-035: Here's another similar exercise. What will the following script output? 

c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())

# Question-036 : The following script throws a NameError in the last line saying that c is not defined. Please fix the function so that there is no error and the last line is able to print out the value of c  (i.e. 1 ).
				 
def foo(): 
    c = 1 
    return c 
foo() 
print(c)

Expected output: 1 

# Question-037 : Create a function that takes any string as input and returns the number of words for that string.

# Question-038 : Please download the words1.txt file from the attachment and then create a function that takes a text file as input and returns the number of words contained in the text file ***			 

Expected output : 10 

# Question-039 : The following code is supposed to print out the square root of 9, but it throws an error instead because another line before that is missing. Please fix the script so that it prints out the square root of 9.
				
math.sqrt(9) 

# Question-040 : The script is supposed to output the cosine of angle 1 radian, but instead it is throwing an error. Please fix the code so that it prints out the expected output.    

import math
print(math.cosine(1))

# Question-041 : Please try to guess what is missing in the following code and add the missing part so that the code works fine.

import math
print(math.pow(2))

# Question-042 : Create a script that generates a text file with all letters of English alphabet inside it, one letter per line.

# Question-043 : Print out in each line the sum of homologous items of the two sequences.

a = [1, 2, 3]
b = (4, 5, 6)

Expected output: 

5
7
9