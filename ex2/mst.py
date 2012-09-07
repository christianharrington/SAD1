#!/usr/bin/env python

import math
import sys

try:
	file = open(sys.argv[1]);
except IOError:
	print("File {0} does not exist".format(sys.argv[1]))
	exit()
	
class City:
	def __init__(self, n):
		self.name = n
		self.connections = {}
	
cities = {}
roads = []

for line in file:
	if "--" not in line:
		name = line.strip().strip("\"")
		cities[name] = City(name)
	else: 
		road = line.replace("\"", "").split("--")
		city1 = road[0]
		city2 = road[1][:road[1].find("[")].strip()
		
		weight = road[1][road[1].find("[")+1:].strip().strip("]")
		
		print city1, '-', city2, ':', weight
		
		cities[city1].connections[city2] = weight
		cities[city2].connections[city1] = weight

#print(cities)