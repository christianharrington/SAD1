#!/usr/bin/env python

# Christian Harrington & Nicolai Dahl

import sys
import math
import re
import os

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def loadFile(a_file, points):
    start = False
    
    for line in a_file:
        if 'NODE_COORD_SECTION' in line:
            start = True
        elif start and line.strip() and ':' not in line and 'NODE_COORD_SECTION' not in line and not 'EOF' in line:
            s = re.sub('\s+', ' ', line).strip().split(' ')
            points.append(Point(float(s[1].strip()), float(s[2].strip())))

def split_in_two(alist):
    length = len(alist)
    return [ alist[i * length // 2: (i + 1) * length // 2] 
             for i in range(2) ]

def dist(point1, point2):
    return math.sqrt(math.pow(point1.x - point2.x, 2) + math.pow(point1.y - point2.y, 2))

def closestPair(points):
    point_count = len(points)
    
    if point_count == 1:
        return float('inf')
    elif point_count == 2:
        return dist(points[0], points[1])
    elif point_count == 3:
        return min(dist(points[0], points[1]), min(dist(points[0], points[2]), dist(points[1], points[2])))
        
    (left, right) = split_in_two(points)
    
    xline = right[0].x
    
    delta = min(closestPair(left), closestPair(right))    
    
    ypoints = [p for p in points if delta >= abs(p.x - xline)]
    ypoints.sort(lambda po1, po2:cmp(po1.y, po2.y))
                    
    p1counter = 0
    for p1 in ypoints:
        comparisonPoints = ypoints[p1counter + 1:p1counter + 1 + 15]
        for p2 in comparisonPoints:
            delta = min(dist(p1, p2), delta)
        p1counter += 1
                    
    return delta
	
def findClosestPair(file, printResults = False):
	points = []
	loadFile(open(file, 'r'), points)
	points.sort(lambda po1, po2:cmp(po1.x, po2.x))
	if printResults:
		print '{}: {} {}'.format(file, len(points), closestPair(points))
	return closestPair(points)
	
def compare(file):
	error = False
	for line in file:
		filePattern = re.compile('^.*\.tsp')
		resultPattern = re.compile('[E0-9.]*$')
		
		compareFile = filePattern.findall(line)[0]
		compareResult = resultPattern.findall(line)[0]
		
		print 'Checking', compareFile
		
		result = findClosestPair(compareFile)
		
		if abs(result - float(compareResult)) < float('1e-7'):
			print 'Correct:', compareResult, result
		else:
			print '\nIncorrect:', compareResult, result
			error = True
			
		if error:
			print 'There were errors'

for file in sys.argv:
	if '.out' in sys.argv[1]:
		compare(open(sys.argv[1], 'r'))
		break
	elif file != sys.argv[0] and os.path.exists(file):
		findClosestPair(file, True)
