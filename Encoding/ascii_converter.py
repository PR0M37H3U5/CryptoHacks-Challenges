#!/usr/bin/env python3

ascii_list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

ascii_string = r"0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def ascii_meaning():
	crypto_flag = []
	for i in ascii_list:
		c = i - 48
		crypto_flag.append(ascii_string[c])
	print(" ".join(crypto_flag))
	
	
ascii_meaning()

