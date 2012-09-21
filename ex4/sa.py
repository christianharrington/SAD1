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
	
def seqAlg(seqs):
	return seqs
			
print seqAlg(loadFile(open(sys.argv[1], 'r')))
