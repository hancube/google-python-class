#!/usr/bin/python

# python 03_wordcount.py test.txt

import sys


class WordCount:
	def __init__(self, word, count):
		self.word = word
		self.count = count

def getWords(filename):
	f = open(filename, 'rU')
	text = f.read()
	words = text.split()
	return words


def countWords(words):
	word_counts = []
	for word in words:
		count = 1
		i = findWord(word_counts, word)
		if i > -1:
			count = word_counts[i].count + 1
			word_counts.pop(i)
		word_counts.append(WordCount(word, count))
	return word_counts


def findWord(words, find_word):
	for i in range(0, len(words) - 1):
		if words[i].word == find_word:
			return i
	return -1


def rsortByCount(words):
	return sorted(words, key=lambda x: x.count, reverse=True)


def printWordCounts(word_counts):
	for word_count in word_counts:
		print word_count.word, word_count.count



def main():
	words = getWords(sys.argv[1])
	word_counts = countWords(words)
	rsorted_word_counts = rsortByCount(word_counts)
	printWordCounts(rsorted_word_counts)



if __name__ == '__main__':
	main()
