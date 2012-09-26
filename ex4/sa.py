#!/usr/bin/env python

# Christian Harrington & Nicolai Dahl

import sys
import re

delta = float('-inf')
penaltyArray = []

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
                scores[line[0]][scoreOrder[n]] = float(s)
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
    if penaltyArray[i][j][0] is None:
    
        if i == 0 and j == 0:
            penalty = scores[x[i]][y[j]]
            return (max(penalty, delta), y[j])
        elif i < 0:
            return (delta * (j + 1), '-' * (j + 1))
        elif j < 0:
            return (delta * (i + 1), '-' * (i + 1))
        else:
            penalty = scores[x[i]][y[j]]
            first = opt(x, i - 1, y, j - 1)
            snd = opt(x, i - 1, y, j)
            third = opt(x, i, y, j - 1)
            
            maxval = (penalty + first[0], first[1] + y[j])
                    
            if delta + snd[0] > maxval[0]:
                maxval = (delta + snd[0], snd[1] + '-')
                
            if delta + third[0] > maxval[0]:
                maxval = (delta + third[0], third[1] + '-')
                
            return maxval
    else:
        return penaltyArray[i][j]
        
def alignment(x, y):
    
    
    for i in range(0, len(x)):
        penaltyArray.append([(None, '') for _ in range(0, len(y))])
        

    for i in range(0, len(x)):
        for j in range(0, len(y)):
            penaltyArray[i][j] = opt(x, i, y, j)
    
    print penaltyArray
    
    return penaltyArray[len(x) - 1][len(y) - 1]


scores = loadScores(open('BLOSUM62.txt', 'r'))
delta = scores['*']['A']
print delta
print alignment('KQRK', 'KQRIKAAKABK')

#seqs = loadSequence(open(sys.argv[2], 'r'))










