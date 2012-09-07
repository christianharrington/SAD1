import math
import sys

try:
	file = open(sys.argv[1]);
except IOError:
	print("File {0} does not exist".format(sys.argv[1]))
	exit()
except IndexError:
	print("Usage: python3 matcher.py filename.in")
	exit()
	
class City:
	def __init__(self, n):
		self.name = n
		self.connections = {}
	
	
cities = {}
roads = []

for line in file:
	if "--" in line:
		edge = line.split("--")
		f = edge[0]
		t = edge.split(" ")[0]
		weight = edge.split(" ")[1].replace("[", "").replace("]", "")
		
		
	else:
		n = line.replace("\"", "").strip()
		
	
	cities[n] = City(n)
	
print(cities)