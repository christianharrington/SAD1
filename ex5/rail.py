#!/usr/bin/env python

# Christian Harrington & Nicolai Dahl

import sys
import collections
import copy

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
            
            if int(cap) == -1:
                cap = sys.maxint
            
            edge = Edge(nodes[int(fromNode)], nodes[int(toNode)], int(cap), 0)
            edgeRev = Edge(nodes[int(toNode)], nodes[int(fromNode)], int(cap), 0)
            
            edges.append(edge)
            nodes[int(fromNode)].edges.append(edge)
            nodes[int(toNode)].edges.append(edgeRev)
            
        i += 1
        
    return Graph(nodes, edges)

def bottleneck(path):
    return min([e.capacity - e.flow for e in path])


def backtrackPath(source, tempNode, prevDict):
    if source == tempNode:
        return []
    else:
        prevNode = prevDict[tempNode.id]
        ret = backtrackPath(source, prevNode, prevDict)
        forwardEdge = next(x for x in prevNode.edges if x.toNode == tempNode)
        ret.append(forwardEdge)
        return ret 

def bfs(source, sink):
    prevDict = {}
    visitedDict = {}

    q = collections.deque()
    q.append(source)
    
    while(not len(q) == 0):
        n = q.popleft()
        visitedDict[n] = True

        if n == sink:
            return backtrackPath(source, n, prevDict)
        else:
            for edge in n.edges:
                if not edge.capacity - edge.flow == 0:
                    if edge.toNode not in visitedDict:
                        prevDict[edge.toNode.id] = n
                        q.append(edge.toNode)
    return None

def findSetA(source):
    visitedDict = {}

    q = collections.deque()
    q.append(source)
    
    while(not len(q) == 0):
        n = q.popleft()
        visitedDict[n] = True

        for edge in n.edges:
            if not edge.capacity - edge.flow == 0:
                if edge.toNode not in visitedDict:
                    q.append(edge.toNode)
    
    return visitedDict

def bottleneckEdges(sink, setA):
    visitedDict = {}

    q = collections.deque()
    q.append(sink)
    
    retList = []
    
    while(not len(q) == 0):
        n = q.popleft()
        visitedDict[n] = True

        for edge in n.edges:
            if not edge.capacity - edge.flow == 0:
                if edge.toNode in setA:
                    retList.append(edge)
                elif edge.toNode not in visitedDict:
                    q.append(edge.toNode)
    
    return retList
                
def augment(path):
    b = bottleneck(path)
    
    for edge in path:
        edge.flow += b
        
        reverseEdge = next(x for x in edge.toNode.edges if x.toNode == edge.fromNode)
        reverseEdge.flow -= b
    
    return b
    
def maxFlow():
    flow = 0
    
    graph = loadData(open(sys.argv[1], 'r'))
    #graph = loadData(open('test.txt', 'r'))
    resGraph = copy.deepcopy(graph)
    
    s = resGraph.nodes[0]
    t = resGraph.nodes[len(resGraph.nodes) - 1]
    
    path = bfs(s, t)
    while path is not None:
        flow += augment(path)
        path = bfs(s, t)
    
    setA = findSetA(s)
    be = bottleneckEdges(t, setA)
    for e in be:
        print e

    print flow
    
maxFlow()    
    


