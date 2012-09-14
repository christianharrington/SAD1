#!/usr/bin/env python

# Christian Harrington & Nicolai Dahl

import sys
import os

points = []

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def loadFile(file):
	wait = False
	
	for line in file:
		if "NAME" in line:
			wait = True
		elif "NODE_COORD_SECTION" in line:
			wait = False
		elif line.strip() and wait == False and not "EOF" in line:
			s = line.strip().split(" ")
			points.append(Point(float(s[1]), float(s[2])))

def closestPath(points):
	print "closestPath"

for file in sys.argv:
	if file != sys.argv[0] and os.path.exists(file):
		print "Parsing", file
		points = []
		loadFile(open(file, 'r'))
		closestPath(points)
