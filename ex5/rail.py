#!/usr/bin/env python

# Christian Harrington & Nicolai Dahl

from collections import deque

class Graph:
	def __init__(self, vertices, edges):
		self.vertices = vertices
		self.edges = edges

class Node:
	def __init__(self, n):
		self.id = n
		self.edges = []
		
class Edge:
	def __init__(self, fromNode, toNode, capacity, flow):
		self.fromNode = fromNode
		self.toNode = toNode
		self.capacity = capacity
		self.flow = flow

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
	
	
