#!/usr/bin/python

import sys

def OpenFile(filename):
	f = open(filename, 'rU')
	for line in f:
		print line,

def main():
	OpenFile(sys.argv[1])

if __name__ == '__main__':
	main()
