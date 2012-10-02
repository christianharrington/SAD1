#!/usr/bin/env python

# Christian Harrington & Nicolai Dahl

import sys
import collections

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
        line = line.strip()
        
        if i == 0: # Number of nodes
            n = int(line)
        elif i <= n: # Load nodes
            nodes.append(Node(i - 1, line))
        elif i == n + 1: # Number of edges
            m = int(line)
        elif i <= n + m + 1: # Edges
            (fromNode, toNode, cap) = line.split(' ')
            
            edge = Edge(int(fromNode), int(toNode), int(cap), 0)
            edges.append(edge)
            nodes[int(fromNode)].edges.append(edge)
            nodes[int(toNode)].edges.append(edge)
            
        i += 1
        
    return Graph(nodes, edges)


prevDict = {}

def bottleneck(path):
    return min([e.capacity - e.flow for e in path])


def backtrackPath(source, tempNode):
    if source == tempNode:
        return source
    else:
        return backtrackPath(source, prevDict[tempNode.id]).insert(0, tempNode)

def bfs(source, sink):
    prevDict = {}
    visitedDict = {}

    q = collections.deque()
    q.append(source)
    
    while(not q.empty()):
        t = q.popleft()

        if t == sink:
            return backtrackPath(source, t)
        else:
            for edge in t.edges:
                if not visitedDict[edge.toNode] == None:
                    prevDict[edge.toNode] = edge.fromNode
                    visitedDict[edge.fromNode] = True
                    q.append(edge)
        
        return None

                
def augment(path):
    b = bottleneck(path)
    
    for edge in path:
        edge.flow -= b
        reverseEdge = next(x for x in edge.toNode.edges if x.toNode == edge.fromNode)
        reverseEdge += b
    
    return b
    
def maxFlow():
    flow = 0
    
    graph = loadData(open(sys.argv[1], 'r'))
    resGraph = copy.deepcopy(graph)
    
    s = resGraph.nodes.first
    t = resGraph.nodes.last
    
    path = bfs(s, t)
    while not path == None:
        flow += augment(path)
        path = bfs(s, t)
        
    return f    
         
maxFlow()
    
    







