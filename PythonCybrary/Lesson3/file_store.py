#!/usr/bin/python3

def main():
	file_name = input("Filename: ")
	f = open(file_name, 'w')
	f.write(input("Insert data to store> "))
	f.close()
	return

main()
