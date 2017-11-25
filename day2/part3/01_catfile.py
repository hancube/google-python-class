#!/usr/bin/python

# python 01_catfile.py aaa.txt bbb.txt
# python 01_catfile.py aaa.txt bbb.txt ccc.txt

import sys

def Cat(filename):
	try:
		f = open(filename)
		text = f.read()
		print '---', filename
		print text
	except IOError:
		print 'IOError ', filename



def main():
	args = sys.argv[1:]
	for arg in args:
		Cat(arg)



if __name__ == '__main__':
	main()
