# dijkstra shortest path

class myGraph:
    pass

import sets
import sys

graph = {}

graph['a'] = {}
graph['b'] = {}
graph['c'] = {}
graph['d'] = {}
graph['e'] = {}
graph['f'] = {}
graph['g'] = {}
graph['h'] = {}
graph['i'] = {}
graph['j'] = {}
graph['k'] = {}
graph['l'] = {}
graph['m'] = {}

INF = float('inf')

nodes = 'abcde'

vertices = sets.Set(list(nodes))

print 'vertices:', vertices

for i in vertices:
    for j in vertices:
        graph[i][j] = INF


print graph

graph['a']['b'] = 10
graph['a']['d'] = 30
graph['a']['e'] = 100
graph['b']['c'] = 50
graph['c']['e'] = 10
graph['d']['c'] = 20
graph['d']['e'] = 60




print graph
sys.exit(0)

'''
def myMin(start, vertices):
    global graph
    
    L = list(vertices)
    mindex = 0
    i = mindex
    for i in range(1, len(L)):
        if graph[start][L[i]] < graph[start][L[mindex]]:
            mindex = i
    return L[mindex]
'''
                                         
def myMin(start, vertices):
    global graph
    
    newMin = float('inf')
    for i in vertices:
        if graph[start][i] < newMin:
            minVertex = i
            newMin = graph[start][i]
    return minVertex





S = sets.Set()
S.add('a')
vertices.remove('a')
print 'vertices:', vertices
print 'S:', S

for i in range(len(vertices)):
    w = myMin('a', vertices)
    print 'w:', w

    S.add(w)
    vertices.remove(w)
    print 'S:', S
    print 'vertices:', vertices

    # update w's neighbors
    for v in vertices:
        if graph['a'][w] + graph[w][v] < graph['a'][v]:
            graph['a'][v] = graph['a'][w] + graph[w][v]


print graph['a']
    


