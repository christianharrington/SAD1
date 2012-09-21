#!/usr/bin/env python

# Christian Harrington & Nicolai Dahl

import sys

def loadFile(file):
	seqs = {}
	
	for line in file:
		line = line.strip()
		if line[0] == '>':
			name = line[1:].split(' ')[0]
			seqs[name] = ''
		else:
			seqs[name] += line
			
	return seqs
	
def alignment(x, y):
	penaltyArray = []
	
	for i in range(0, len(x)):
		penaltyArray.append([max(len(x), len(y)) for item in range(0, len(y))])
	
	
	
def seqAlg(seqs):
	return seqs
			
print seqAlg(loadFile(open(sys.argv[1], 'r')))

print alignment('hej', 'ehje')