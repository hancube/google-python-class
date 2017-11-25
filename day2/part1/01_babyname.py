#!/usr/bin/python

# python 01_babyname.py baby*.html
# python 01_babyname.py --summaryfile baby*.html

# grep 'Daniel ' *.summary
# grep 'Trinity ' *.summary

import sys
import re



class Baby:
	def __init__(self, name, rank):
		self.name = name
		self.rank = rank



def FindName(babies, name):
	for baby in babies:
		if baby.name == name:
			return baby.rank
	return False



def AddBaby(babies, rank, name):
	r = FindName(babies, name)
	# unique baby name (with higer(=lower in number) rank)
	if not r or r > rank:
		babies.append(Baby(name, rank))
	return babies



def BabyName(filename, summary):
	f = open(filename, 'r')
	html = f.read()

	# get year
	m = re.search('<h3 align="center">Popularity in (\d\d\d\d)', html)
	year = m.group(1)

	# get unique baby names
	babies = []
	for baby in re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', html):
		babies = AddBaby(babies, baby[0], baby[1])
		babies = AddBaby(babies, baby[0], baby[2])

	# sort by name
	babies = sorted(babies, key=lambda baby: baby.name)

	# output
	output = ''
	output = output + year + "\n"
	for baby in babies:
		output = output + baby.name
		output = output + ' '
		output = output + baby.rank
		output = output + "\n"

	# print
	if summary:
		f = open(filename + '.summary', 'w')
		f.write(output)
	else:
		print output



def main():
	summary = sys.argv[1] == '--summaryfile'
	for i in range(2, len(sys.argv) - 1):
		BabyName(sys.argv[i], summary)



if __name__ == '__main__':
	main()
