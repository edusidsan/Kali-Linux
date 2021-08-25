#!/usr/bin/python3

def main():
	num_tokens = []
	str_tokens = []
	user_data = input("Insert delimited data: ")
	split_data = user_data.split(sep = "|")
	for i in split_data:
		if i.strip().isnumeric():
			num_tokens.append(i)
		else:
			str_tokens.append(i)	
	print("String tokens: {}\nNumeric Tokens: {}".format(len(num_tokens),len(str_tokens)))
	return

main()

