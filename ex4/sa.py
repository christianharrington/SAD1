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
    
# Compare results
def loadCompare(cfile):
    compareResults = []
    
    for line in cfile:
        line = line.strip()
        if ':' in line:
            (compare1, t1) = line.split('--')
            (compare2, r) = t1.split(': ')
            
            result = (compare1, compare2, r, None, None)
        else:
            if result[3] == None:
                result = (result[0], result[1], result[2], line.strip(), None)
            elif result[4] == None:
                result = (result[0], result[1], result[2], result[3], line.strip())
                compareResults.append(result)
                
    return compareResults

# The algorithm
def opt(x, i, y, j):
    if i == 0 and j == 0:
        penalty = scores[x[i]][y[j]]
        if penalty < delta:
            return (delta, '-', y[j])
        else:
            return (penalty, x[i], y[j])
    elif i < 0:
        return (delta * (j + 1), '-' * (j + 1), y[0:j + 1])
    elif j < 0:
        return (delta * (i + 1), x[0:i + 1], '-' * (i + 1))
    else:
        if penaltyArray[i][j][0] is None:
            penalty = scores[x[i]][y[j]]
            first = opt(x, i - 1, y, j - 1)
            snd = opt(x, i - 1, y, j)
            third = opt(x, i, y, j - 1)
                
            maxval = (penalty + first[0], first[1] + x[i], first[2] + y[j])
                        
            if delta + snd[0] > maxval[0]:
                maxval = (delta + snd[0], snd[1] + x[i], snd[2] + '-')
                    
            if delta + third[0] > maxval[0]:
                maxval = (delta + third[0], third[1] + '-' , third[2] + y[j])
                
            return maxval
        else:
            return penaltyArray[i][j]
        
def alignment(x, y):
    for _ in range(0, len(x)):
        penaltyArray.append([(None, '', '') for i in range(0, len(y))])

    for i in range(0, len(x)):
        for j in range(0, len(y)):
            penaltyArray[i][j] = opt(x, i, y, j)
        
    return penaltyArray[len(x) - 1][len(y) - 1]
    
# Load files and run the algorithm./sa.py data/BLOSUM62.txt data/HbB_FASTAs.in data/HbB_FASTAs.out
scores = loadScores(open(sys.argv[1], 'r'))
delta = scores['*']['A']
seqs = loadSequence(open(sys.argv[2], 'r'))
compareResults = loadCompare(open(sys.argv[3], 'r'))

incorrect = 0

for s in compareResults:
    penaltyArray = []
    
    v1 = seqs[s[0]]
    v2 = seqs[s[1]]
    
    sa = alignment(v1, v2)
    
    print '{}--{}: {}/{}'.format(s[0], s[1], s[2], sa[0])
    
    print s[3]
    print s[4]
    print 
    print sa[1]
    print sa[2]
    print
    
    if sa[0] == float(s[2]):
        print 'CORRECT'
    else:
        print 'INCORRECT'
        incorrect += 1
    
    print
    
print 'Incorrect results: {}\n'.format(incorrect)
