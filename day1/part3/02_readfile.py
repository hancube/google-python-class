#!/usr/bin/python

# python 02_readfile.py test.txt

import sys

def ReadFile(filename):
	f = open(filename, 'rU')
	text = f.read()
	print text

def main():
	ReadFile(sys.argv[1])

if __name__ == '__main__':
	main()
