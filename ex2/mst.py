#!/usr/bin/env python

import sys

nodes = {}
edges = []

class Node:
	def __init__(self, n):
		self.id = n
		self.edges = {}
		self.parent
		self.rank
	
class Edge:
	def __init__(self, node1, node2, weight):
		self.node1 = node1
		self.node2 = node2
		self.weight = weight
		
	def __str__(self):
		return str(self.weight)

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

				print node1, '-', node2, ':', weight

def find(node):
	if node.parent != node:
		node.parent = find(node.parent)
	return node.parent
				
def makeSet(node):
     node.parent = node
     node.rank   = 0

def union(node1, node2):
	root1 = find(node1)
	root2 = find(node2)
	
	if root1 == root2:
		return
	
	if root1.rank > root2.rank:
		root2.parent = root1
	else if root1.rank < root2.rank:
		root1.parent = root2
	else:
		root2.parent = root1
		root1.rank = root1.rank + 1

def kruskal(nodes, edges):
	queue = list(edges)
	while queue:
		edge = queue.pop(0)
		print edge
		# INSERT ALGORITHM HERE

loadFile()
edges.sort(cmp=lambda x,y:cmp(x.weight, y.weight))
kruskal(nodes, edges)
