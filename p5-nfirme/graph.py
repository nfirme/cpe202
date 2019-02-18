from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.color = None

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated
           with the edge.'''
        with open(filename, 'r') as f:
            self.vertices = []
            self.graph = {}
            self.dfs_visited = set()

            for line in f:
                self.vertices += line.split()

            for index, i in enumerate(self.vertices):
                if i not in self.graph:
                    self.graph[i] = Vertex(i)
                if index % 2 == 1:
                    self.graph[i].adjacent_to.append(self.vertices[index - 1])
                    self.graph[self.vertices[index - 1]].adjacent_to.append(i)

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if key not in self.graph:
            self.graph[key] = Vertex(key)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key in self.graph:
            return self.graph[key]
        else:
            return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.graph[v1].adjacent_to.append(v2)
        self.graph[v2].adjacent_to.append(v1)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        vlist = []
        for i in self.graph:
            vlist.append(i)

        vlist.sort()
        return vlist

    def conn_components(self): 
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        component_list = []
        self.dfs_visited = set()

        for x in self.graph:
            if x not in self.dfs_visited:
                component_list.append(sorted(self.dfs(x)))

        component_list = sorted(component_list)

        return component_list

    def dfs(self, vertex):
        visited = set()
        stack = Stack(len(self.graph))

        visited.add(vertex)
        self.dfs_visited.add(vertex)
        stack.push(vertex)

        while not stack.is_empty():
            vertex = stack.pop()
            for i in self.get_vertex(vertex).adjacent_to:
                if i not in visited:
                    stack.push(i)
                    visited.add(i)
                    self.dfs_visited.add(i)

        return list(visited)

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''

        cclist = self.conn_components()

        for component in cclist:
            if not self.bfs(component[0]):
                return False

        return True

    def bfs(self, vertex):
        queue = Queue(len(self.graph))

        queue.enqueue(vertex)
        self.graph[vertex].color = 'B'

        while not queue.is_empty():
            vertex = queue.dequeue()

            for i in self.graph[vertex].adjacent_to:
                if self.graph[i].color is None:
                    if self.graph[vertex].color == 'B':
                        self.graph[i].color = 'R'
                    elif self.graph[vertex].color == 'R':
                        self.graph[i].color = 'B'
                    queue.enqueue(i)
                elif self.graph[i].color == self.graph[vertex].color:
                    return False

        return True
