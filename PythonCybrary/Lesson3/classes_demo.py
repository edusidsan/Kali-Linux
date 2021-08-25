#!/usr/bin/python3
class Person:
	name = ''
	age = 0
	def __init__(self, name, age):
		self.name = name
		self.age = age
		return
	def print_vals(self):
		print("Name: {} | Age: {}".format(self.name, self.age))

class Employee(Person):
	def __init__(self, name, age, department):
		Person.__init__(self, name, age)
		self.department = department
	def extended_print_vals(self):
		print("Name: {}, Age: {}, Department: {}".format(self.name, self.age, self.department))

emp = Employee("Eduardo", 28, "Tech")
emp.extended_print_vals()
