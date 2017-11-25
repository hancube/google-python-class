#!/usr/bin/python

# python 02_logpuzzle.py happy_www.corp.google.com
# python 02_logpuzzle.py --todir output happy_www.corp.google.com


import sys
import os
import re
import commands
import urllib


def showError(output):
	sys.stderr.write('there was an error:' + output)
	sys.exit(1)


def getPuzzleImages(filename):
	urls = []
	try:
		f = open(filename)
		for line in f:
			m = re.search('GET /edu/languages/google-python-class/images/puzzle/(a-\w+.jpg) ', line)
			if m:
				url = 'https://developers.google.com/edu/python/images/puzzle/' + m.group(1)
				if url not in urls:
					urls.append(url)
	except IOError:
		print 'IOError ', filename
		sys.exit(1)
	return sorted(urls)


def makesureTodir(todir):
	if not os.path.exists(todir):
		cmd = 'mkdir ' + os.path.abspath(todir)
		(status, output) = commands.getstatusoutput(cmd)
		if status:
			showError(output)


def getUrlContents(url):
	uf = urllib.urlopen(url)
	return uf.read()


def storeFile(data, target):
	f = open(target, 'w')
	f.write(data)


def makeIndexHTML(images):
	html = '<html><body>'
	for image in images:
		html = html + '<img src="' + image + '">'
	html = html + '</body></html>'
	return html


def showPuzzleImages(filename):
	for url in getPuzzleImages(filename):
		print url


def solvePuzzle(filename, todir):
	makesureTodir(todir)
	urls = getPuzzleImages(filename)
	images = []
	for i in range(0, len(urls) - 1):
		url = urls[i]
		data = getUrlContents(url)
		target = os.path.join(todir, 'img' + str(i))
		storeFile(data, target)
		images.append('img' + str(i))

	html = makeIndexHTML(images)
	storeFile(html, os.path.join(todir, 'index.html'))



def main():
	if sys.argv[1] == '--todir':
		solvePuzzle(sys.argv[3], sys.argv[2])
	else:
		showPuzzleImages(sys.argv[1])



if __name__ == '__main__':
	main()
