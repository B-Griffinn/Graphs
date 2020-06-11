"""
Simple graph implementation
"""
from util import Queue  # These may come in handy


class Graph:
    def __init__(self):
        # field vertices that contains a dictionary mapping vertex labels to edges.
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add directed edge to the graph in order to connect verts
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That connection does not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex given
        """
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):
    """
    USING A BREADTH FIRST SEARCH APPROACH
    """
    # create our graph for every time we call this function on a family tree
    graph = Graph()

    # map our graph using the graph class by adding vertexes to the graph
    for i in ancestors:
        # print(i)
        # plot first value of tuple in ancestors to the graph
        graph.add_vertex(i[0])
        # plot second value of tuple in ancestors to the graph
        graph.add_vertex(i[1])

    # map our edges to their respected nodes using the ancestors list of tuples
    for x in ancestors:
        graph.add_edge(x[1], x[0])

    # we are using a BFS approach so we need to use a q
    storage = Queue()

    # we need to add our starting node to front of Q
    # we do not make our added item a list bc we are returning a value of a node only
    storage.enqueue([starting_node])
    # print('fasfsadf', storage.size())

    # we need to create a set() visited var to track our path
    visited = set()

    result = []

    while storage.size() > 0:
        # pop off the starting node of our Q to create a path
        path = storage.dequeue()
        # print('path after dequeue', path)

        # >> grab the last vertex in the path bc that is the furthest point from beginning var
        last_vert = path[-1]
        # print('last_vert', last_vert)

        # check if that last vertex is in our visited set()
        if last_vert not in visited:
            visited.add(last_vert)

        # check if its the smallest value if there are two parents
        # return the parent with smallest numeric id
        for next_vert in graph.get_neighbors(last_vert):
            new_path = list(path)
            new_path.append(next_vert)
            storage.enqueue(new_path)
            # print('New PAth', new_path)
            result.append(new_path[-1])

        if result == []:
            return -1

    # print('VISITED', visited)
    # print('result', result)
    return result[-1]


# GRAPH DESIGN
    '''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''


# if __name__ == '__main__':
#     graph = Graph()  # create new graph instance
#     # add vertexes
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(3)
#     graph.add_vertex(4)
#     graph.add_vertex(5)
#     graph.add_vertex(6)
#     graph.add_vertex(7)
#     graph.add_vertex(8)
#     graph.add_vertex(9)
#     graph.add_vertex(10)
#     graph.add_vertex(11)
#     # add edges / connections of verts
#     graph.add_edge(1, 10)
#     graph.add_edge(3, 1)
#     graph.add_edge(3, 2)
#     graph.add_edge(5, 4)
#     graph.add_edge(6, 3)
#     graph.add_edge(6, 5)
#     graph.add_edge(7, 5)
#     graph.add_edge(8, 4)
#     graph.add_edge(8, 11)
#     graph.add_edge(9, 8)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 2))
# print(graph.vertices)
# print(graph.earliest_ancestor(test_ancestors, 2))


"""
- ancestors input is a list of sets
- starting node is a numeric value which lives in the ancestors list of set
- DESIGN THE CONNECTIONS IN `http://madebyevan.com/fsm/`
- WHAT approach do we take? 
-- this is a search problem - bfs or dfs?
-- we need to track that path that gets us all the way to our our starting node
-- then we check the index in the path with the lowest value furthest from the starting node
"""
