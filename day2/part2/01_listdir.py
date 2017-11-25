#!/usr/bin/python

# python 01_listdir.py .

import sys
import os

def ListDir(dir):
	filenames = os.listdir(dir)
	for filename in filenames:
		path = os.path.join(dir, filename)
		print path
		print os.path.abspath(path)

def main():
	ListDir(sys.argv[1])

if __name__ == '__main__':
	main()
