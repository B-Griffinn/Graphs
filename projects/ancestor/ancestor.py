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

    def earliest_ancestor(self, ancestors, starting_node):
        """
        USING A BREADTH FIRST SEARCH APPROACH
        """
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
            for next_vert in self.get_neighbors(last_vert):
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

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
#                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(graph.vertices)
# print(graph.earliest_ancestor(test_ancestors, 1))


"""
- ancestors input is a list of sets
- starting node is a numeric value which lives in the ancestors list of set
- DESIGN THE CONNECTIONS IN `http://madebyevan.com/fsm/`
- WHAT approach do we take? 
-- this is a search problem - bfs or dfs?
-- we need to track that path that gets us all the way to our our starting node
-- then we check the index in the path with the lowest value furthest from the starting node
"""
