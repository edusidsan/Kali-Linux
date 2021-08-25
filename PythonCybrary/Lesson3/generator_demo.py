#!/usr/bin/python3

def custom_range(last):
	i = 0
	while i < last:
		# Yield eh um return que volta na mesma posicao que saiu
		yield i
		i += 1

for i in custom_range(10):
	print (i)
