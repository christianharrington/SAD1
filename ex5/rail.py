#!/usr/bin/env python

# Christian Harrington & Nicolai Dahl

class Graph:
	def __init__(self, vertices, edges):
		self.vertices = vertices
		self.edges = edges

class Node:
	def __init__(self, n):
		self.id = n
		self.edges = []
		
class Edge:
	def __init__(self, from, to, capacity, flow):
		self.from = from
		self.to = to
		self.capacity = capacity
		self.flow = flow

