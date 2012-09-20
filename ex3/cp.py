#!/usr/bin/env python

# Christian Harrington & Nicolai Dahl

import sys
import math
import os

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def loadFile(file, points):
	wait = False
	
	for line in file:
		if "NAME" in line:
			wait = True
		elif "NODE_COORD_SECTION" in line:
			wait = False
		elif line.strip() and wait == False and not "EOF" in line:
			s = line.strip().split(" ")
			points.append(Point(float(s[1]), float(s[2])))

def split_in_two(alist):
    length = len(alist)
    return [ alist[i*length // 2: (i+1)*length // 2] 
             for i in range(2) ]

def dist(point1, point2):
	return math.sqrt(math.pow(abs(point1.x - point2.x), 2) + math.pow(abs(point1.y - point2.y), 2))
	

def closestPath(points):
	point_count = len(points)
	
	if point_count == 1:
		return float('inf')
	elif point_count == 2:
		return dist(points[0], points[1])
		
	(left, right) = split_in_two(points)
	
	xline = right[0].x
	
	delta = min(closestPath(left), closestPath(right))	
	
	ypoints = [p for p in points if delta >= abs(p.x - xline)]
	ypoints.sort(lambda po1,po2:cmp(po1.y, po2.y))
	
	sorted_len = len(ypoints)
					
	p1counter = 0
	for p1 in ypoints:
		for p2 in ypoints[p1counter+1:p1counter + 1 + 15]:
			delta = min(dist(p1, p2), delta)
		p1counter += p1counter + 1
					
	return delta
	
# exampleInput = [Point(1.0,5.0), Point(1.5, 0.5), Point(2.0,1.0), Point(11.0, 0.0)]
# print(closestPath(exampleInput))	

for file in sys.argv:
	if file != sys.argv[0] and os.path.exists(file):
		print "Parsing", file
		points = []
		loadFile(open(file, 'r'), points)
		print(closestPath(points))

