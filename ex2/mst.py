#!/usr/bin/env python

# Christian Harrington & Nicolai Dahl

import sys

nodes = {}
edges = []

class Node:
	def __init__(self, n):
		self.id = n
		self.edges = {}
		self.parent = self
		self.rank = 0
	
class Edge:
	def __init__(self, node1, node2, weight):
		self.node1 = node1
		self.node2 = node2
		self.weight = weight
		
	def __str__(self):
		return str(self.weight)

# Loads a file. Nodes and edges are as follows
# Nodes: One node per line. The string representing the node will be used as an ID, and must be unique. If the string has spaces, the string must be encapsualted in qoutes.
# Edges: One edge per line, written as follows: "Node 1"--Node2 [weight]
# The nodes specified in the edge must be declared first as described above.
def loadFile():
	with open(sys.argv[1], 'r') as file:
		for line in file:
			if "--" not in line:
				nodeID = line.strip().strip("\"")
				nodes[nodeID] = Node(nodeID)
			else: 
				s = line.replace("\"", "").split("--")
				node1 = s[0]
				node2 = s[1][:s[1].find("[")].strip()
				weight = s[1][s[1].find("[")+1:].strip().strip("]")
				
				road = Edge(nodes[node1], nodes[node2], int(weight))
				edges.append(road)
				
				nodes[node1].edges[node2] = road
				nodes[node2].edges[node1] = road

def find(node):
	if node.parent != node:
		node.parent = find(node.parent)
	return node.parent

def union(root1, root2):
	if root1.rank > root2.rank:
		root2.parent = root1
	elif root1.rank < root2.rank:
		root1.parent = root2
	else:
		root2.parent = root1
		root1.rank = root1.rank + 1

def kruskal(nodes, edges):
	queue = list(edges)
	weight = 0
	while queue:
		edge = queue.pop(0)
		f1 = find(edge.node1)
		f2 = find(edge.node2)
		if f1 != f2:
			union(f1, f2)
			weight += edge.weight
	print weight

loadFile()
edges.sort(cmp=lambda x,y:cmp(x.weight, y.weight))
kruskal(nodes, edges)
