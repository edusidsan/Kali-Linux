#!/usr/bin/python3

class IterDemo:
	def __init__(self):
		self.alphabet = 'abcdefghijklmnopqrstuvxwyz'
		self.i = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.i == 26:
			raise StopIteration
		letter = self.alphabet[self.i]
		self.i = self.i + 1
		return letter

ID = IterDemo()
print(type(ID))
for i in ID:
	print(i)
