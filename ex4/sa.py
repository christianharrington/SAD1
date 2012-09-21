#!/usr/bin/env python

# Christian Harrington & Nicolai Dahl

import sys
import re

# Loads the score table
def loadScores(file):
	scores = {}
	scoreOrder = []
	
	indicesPattern = re.compile('[A-Z*]')
	scoresPattern = re.compile('\-?[0-9]+')
	
	for line in file:
		line = line.strip()
		if line[0] != '#' and not scores:
			indices = indicesPattern.findall(line)
			
			for i in indices:
				scores[i] = {}
				scoreOrder.append(i)
		
		elif line[0] != '#':
			n = 0
			scoreMatches = scoresPattern.findall(line[1:])

			for s in scoreMatches:
				scores[line[0]][scoreOrder[n]] = s
				n += 1

	return scores			

# Loads the sequences
def loadSequence(file):
	seqs = {}
	
	for line in file:
		line = line.strip()
		if line[0] == '>':
			name = line[1:].split(' ')[0]
			seqs[name] = ''
		else:
			seqs[name] += line
			
	return seqs

# The algorithm
def opt(x, i, y, j):
	penalty = scores[x[i]][y[j]]
	max(penalty + opt(x, i - 1, y, j - 1), max(penalty + opt(x, i - 1, y, j, opt(x, i, y, j - 1))))

def alignment(x, y):
	penaltyArray = []
	
	for i in range(0, len(x)):
		penaltyArray.append([max(len(x), len(y)) for item in range(0, len(y))])


#print alignment('hej', 'ehje')

scores = loadScores(open(sys.argv[1], 'r'))
seqs = loadSequence(open(sys.argv[2], 'r'))

for s in 