#!/bin/python3

#Print string

print("Strings and things:")
print('Hello, world')
print("""Hello this is
a multi-line string!""")
print("This is"+" a string")

print('\n') #new line

#Math

print("Math time:")
print(50 + 50) #add
print(50 - 50) #sub 
print(50 * 50) #mult
print(50 / 50) #div
print(50 ** 2) #exp
print(50 % 6)  #resto
print(50 // 6) #number without leftovers

print('\n') #new line

#Variables & Methods

print("Fun with variables and methods:")
quote = "All is fair in love and war"
print(len(quote)) #lenght
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title

name = "Heath"
age = 29
gpa = 3.7

print(int(age))
print(int(29.9)) #does not round

print("My name is " + name + " and I am " + str(age) + " years old.") 

print('\n') #new line

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print('\n') #new line

#Functions

print("Now, some functions:")
def who_am_i():
	name = "Heath"
	age = 29
	print("My name is " + name + " and I am " + str(age) + " years old.") 
	
who_am_i()

# adding in parameters

def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)

#add multi parameters

def add(x,y):
	print(x + y)

add(7,7)
add(305,207)

#using return
def multiply(x,y):
	return x * y

print(multiply(7,7))

def square_root(x):
	return x ** .5

print(square_root(64))

print('\n') #new line

# Boolean expressions

print("Boolean expressions:")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool1))

# Relational and Boolean Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than,less_than,greater_than_equal_to,less_than_equal_to)

test_and = (7 > 5) and (5 < 7)
test_or = (7 > 5) or (5 < 7)
test_not = not True

print(test_and,test_or,test_not)

print('\n') #new line

# Conditional statements

print("Conditional statements:")
def soda(money):
	if money >= 2:
		return "You've got yourself a soda!"
	else:
		return "No soda for you!"
	
print(soda(3))
print(soda(1))

def alcohol(age,money):
	if (age >= 21) and (money >= 5):
		return "We're gettin tipsy!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money!"
	elif (age < 21) and (money >= 5):
		return "Nice try kid!"
	else:
		return("You're too poor and too young")
		
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))

print('\n') #new line

# Lists

print("Lists have brackets:")
movies = ["When Harry meet Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[1])
print(movies[0:2])
print(movies[1:])
print(movies[:1])
print(movies[-1])
print(len(movies))

movies.append("JAWS")
print(movies)

movies.pop() #remove last item of a list
print(movies)

movies.pop(1)
print(movies)

movies = ["When Harry meet Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]
person = ["Heath","Jake","Leah","Jeff"]
combined = zip(movies,person)
print(list(combined))

print('\n') #new line

# Tuples

print("Tuples have parentesis and cannot change:")
grades = ("A", "B", "C", "D", "E", "F")
print(grades[1])

print('\n') #new line

# Looping

print("For loops - start to finish of iterate:")

vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print(x)
	
print("While loops - Execute as long as True:")
i = 1
while i < 10:
	print(i)
	i += 1



