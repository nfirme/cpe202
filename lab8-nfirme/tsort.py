from sys import argv
from stack_array import *


class Vertex:
    def __init__(self, name):
        self.name = name
        self.degree = 0
        self.adj_verts = []

    def add_adjacent(self, vertex):
        self.adj_verts.append(vertex)

    def get_adj_verts(self):
        return self.adj_verts

    def inc_degree(self):
        self.degree += 1

    def dec_degree(self):
        self.degree -= 1

    def get_degree(self):
        return self.degree

    def __repr__(self):
        s = str(self.adj_verts)
        d = str(self.degree)
        return "In degree: " + d + ", Adjacent vertices: " + s

def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
    if len(vertices) == 0:
        raise ValueError("input contains no edges")

    if len(vertices) % 2 == 1:
        raise ValueError("input contains an odd number of tokens")

    output = ""
    vert_order = []
    dict = {}
    stack = Stack(len(vertices))

    for index, i in enumerate(vertices):
        if i not in dict:
            vert_order.append(i)
            dict[i] = Vertex(i)
        if index % 2 == 1:
            dict[i].inc_degree()
            dict[vertices[index - 1]].add_adjacent(i)

    for i in vert_order:
        if dict[i].get_degree() == 0:
            stack.push(i)

    if stack.is_empty():
        raise ValueError("input contains a cycle")

    while not stack.is_empty():
        popped = stack.pop()
        output = output + popped + "\n"
        for j in dict[popped].get_adj_verts():

            dict[j].dec_degree()

            if dict[j].get_degree() == 0:
                stack.push(j)

        dict.pop(popped)

    if len(dict) != 0:
        raise ValueError("input contains a cycle")

    return output


def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()
    
    vertices = []
    for line in f:
        vertices += line.split()
       
    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)
    
if __name__ == '__main__': 
    main()
