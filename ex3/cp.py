#!/usr/bin/env python

# Christian Harrington & Nicolai Dahl

import sys
import math

points = []

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def loadFile():
	print "Parse"

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
	ypoints_sorted = ypoints.sort(cmp=lambda po1,po2:cmp(po1.y, po2.y))
	print(ypoints)
	
			
	for p1 in ypoints:
		for p2 in range(15):
			if p1 != p2:
				delta = min(dist(p1, p2), delta)
				
	return delta
	
exampleInput = [Point(1.0,5.0), Point(1.5, 0.5), Point(2.0,1.0), Point(11.0, 0.0)]
print(closestPath(exampleInput))	

