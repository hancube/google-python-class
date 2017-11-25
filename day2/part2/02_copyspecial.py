#!/usr/bin/python

# python 02_copyspecial.py .
# python 02_copyspecial.py --todir /tmp/test
# python 02_copyspecial.py --tozip blah.zip

import sys
import os
import re
import commands


def showError(output):
	sys.stderr.write('there was an error:' + output)
	sys.exit(1)


def ShowSpecial(dir):
	filenames = os.listdir(dir)
	special_files = []
	for filename in filenames:
		m = re.search('\w+__\w+__\.\w+', filename)
		if m:
			special_files.append(filename)

	for special_file in special_files:
		path = os.path.join(dir, special_file)
		print os.path.abspath(path)


def CopySpecial(todir):
	if not os.path.exists(todir):
		cmd = 'mkdir ' + os.path.abspath(todir)
		(status, output) = commands.getstatusoutput(cmd)
		if status:
			showError(output)

	cmd = 'cp ./*__*__* ' + os.path.abspath(todir)
	(status, output) = commands.getstatusoutput(cmd)
	if status:
		showError(output)


def ZipSpecial(zipname):
	cmd = 'zip ' + zipname + ' *__*__*'
	(status, output) = commands.getstatusoutput(cmd)
	if status:
		showError(output)



def main():
	if sys.argv[1] == '--todir':
		CopySpecial(sys.argv[2])
	elif sys.argv[1] == '--tozip':
		ZipSpecial(sys.argv[2])
	else:
		ShowSpecial(sys.argv[1])



if __name__ == '__main__':
	main()
