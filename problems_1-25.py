# Question-001 : Let's start with easy things first. What will the following code produce?
a = 2
a = 4
a = 6
print(a + a + a)

# Question-002 : What's wrong with the following script?
a   = 1
_a  = 2
_a2 = 3
2a  = 4

# Question-003 : Executing the code will throw an error. Can you explain why?
a = 1
b = 2
print(a == b)
print(b == c)

# Question-004 : The last line so that it outputs the sum of 1 and 2. Please do not change the first two lines. Only the last one.
a = "1"
b = 2
print(a + b)

Expected output: 3 

# Question-005 : Complete the script so that it prints out the second item of the list.
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

Expected output: b

# Question-006 : Please complete the script so that it prints out a list slice containing items d , e , and f .
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

Expected output: ['d', 'e', 'f'] 

# Question-007 : Please complete the script so that it prints out the first three items of list letters.		
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

Expected output: ['a', 'b', 'c'] 

# Question-008 : Complete the script so that it prints out letter i using negative indexing.
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

Expected output: i 

# Question-009 : Complete the script so that it prints out a list slice containing the last three items of list letters .
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
Expected output: ['h', 'i', 'j'] 

# Question-010 : Complete the script so that it prints out a list slice containing letters a, c, e, g, and i. 

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

Expected output: ['a', 'c', 'e', 'g', 'i'] 

# Question-011 : Create a script that generates and prints a list of numbers from 1 to 20. Please do not create the list manually.

# Question-012 : Please complete the script so that it prints out the expected output.

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

Expected output: 
b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Question-013 :Complete the script so that it produces the expected output. Please use my_range as input data.

Expected output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200] 

# Question-014 : Complete the script so it generates the expected output using my_range as input data. 
#			     Please note that the items of the expected list output are all strings.

Expected output: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']  

# Question-015 : Complete the script so that it removes duplicate items from list a. ***

a = ["1", 1, "1", 2]

Expected output: ['1', 2, 1] 

# Question-016 : Create a dictionary that contains the keys a and b and their respective values 1 and 2.

# Question-017 : Please complete the script so that it prints out the value of key b .

d = {"a": 1, "b": 2}

Expected output: 2  

# Question-018 : Calculate the sum of the values of keys a and b.

d = {"a": 1, "b": 2, "c": 3}

Expected output: 3 

# Question-019 : Explain the KeyError with key dictionary

d = {"Name": "John", "Surname": "Smith"}
print(d["Smith"])

# Question-020 : Add a new pair of key (e.g. c ) and value (e.g. 3 ) to the dictionary and print out the new dictionary.

d = {"a": 1, "b": 2}

Expected output: {'a': 1, 'c': 3, 'b': 2} 

# Question-021 : Calculate the sum of all dictionary values.

p = {"a": 1, "b": 2, "c": 3}
q = {"a": 1, "b": 2, "c": 3,"e": 1, "f": 2, "g": 3,"h": 1, "i": 2, "j": 3,"k": 1, "l": 2, "m": 3, "n":5}

Expected output: 6 and 29

# Question-022: Filter the dictionary by removing all items with a value of greater than 1. ***

d = {"a": 1, "b": 2, "c": 3}

Expected output: {'a': 1}  

# Question-023 : Create a dictionary of keys a, b, c where each key has as value a list from 1 to 10, 11 to 20, and 21 to 30 respectively. 
#               Then print out the dictionary in a nice format. ***

# Question-024 : Access the third value of key b  from the dictionary.

from pprint import pprint

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

Expected output: 13 

# Question-025 : Please complete the script so that it prints out the expected output ***

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

Expected output: 

b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]






























