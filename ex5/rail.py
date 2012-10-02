#!/usr/bin/env python

# Christian Harrington & Nicolai Dahl

import sys

class Graph:
	def __init__(self, nodes, edges):
		self.nodes = nodes
		self.edges = edges

class Node:
	def __init__(self, i, name):
		self.id = i
		self.name = name
		self.edges = []
		
	def __str__(self):
		return str(self.id) + ': ' + self.name
		
class Edge:
	def __init__(self, fromNode, toNode, capacity, flow):
		self.fromNode = fromNode
		self.toNode = toNode
		self.capacity = capacity
		self.flow = flow
		
	def __str__(self):
		return str(self.fromNode) + ' ' + str(self.toNode) + ' ' + str(self.capacity)

def loadData(railFile):
	i = 0
	nodes = []
	edges = []
	
	for line in railFile:
		lint = line.strip()
		
		if i == 0:
			n = int(line)
		elif i <= n:
			nodes.append(Node(i - 1, line))
		elif i == n + 1:
			m = int(line)
		else:
			(fromNode, toNode, cap) = line.split(' ')
			
			edge = Edge(int(fromNode), int(toNode), int(cap), 0)
			edges.append(edge)
			nodes[int(fromNode)].edges.append(edge)
			nodes[int(toNode)].edges.append(edge)
			
		i += 1
		
	return Graph(nodes, edges)
	
graph = loadData(open(sys.argv[1], 'r'))

def backtrackPath(source, tempNode):
	if source == tempNode:
		return source
	else:
		return backtrackPath.insert(0, tempNode)

def bfs(source, sink):
	prevDict = {}
	visitedDict = {}

	q = deque()
	q.append(source)
	
	while(not q.empty()):
		t = q.popleft()

		if t == sink:
			return backtrackPath(source, t)
		else:
			for edge in t.edges:
				prevDict(edge.toNode) = edge.fromNode
				visitedDict(edge.fromNode) = True
				q.append(edge)
	
	
