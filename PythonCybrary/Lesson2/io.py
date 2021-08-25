#!/usr/bin/python3

def take_input():
	x = input("Input text > ")
	return x

#print(take_input())

prompted = "You entered: {}"
str_var = take_input()
print(prompted.format(str_var))
