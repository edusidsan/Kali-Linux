#!/usr/bin/python3


class CustomException(Exception):
	print("Exception Found.")

def main():
	#list_one = [1,2,3,4,5]
	#try:
	#	for i in range(6):
	#		print(list_one[i])
	#except IndexError:
	#	print("Index out of range")

	for i in range(10):
		if i % 3 == 0:
			raise CustomException

main()
