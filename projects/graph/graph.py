"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        # field vertices that contains a dictionary mapping vertex labels to edges.
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # TODO
        # add a set to our dictionary using the vertext_id
        self.vertices[vertex_id] = set()  # set of edges from this vert

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # TODO
        if v1 in self.vertices and v2 in self.vertices:
            # add edge between 2 verts
            # add 1 vert id to a set() ~> just like an adjaency list
            self.vertices[v1].add(v2)  # v2 is added as a neighbor to v1
            # self.vertices[v2].add(v1)  # v1 is added as a neighbor to v1
        else:
            raise IndexError("Vertext connection does not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO
        # all neighbors are stored in the vewrtex_id's set()
        return self.vertices[vertex_id]

    ########### PART TWO ###########
    def bft(self, starting_vertex):
        # print("=" * 25)
        # print("  BFT ")
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # TODO - use a QUEUE
        # Create an empty queue and enqueue the starting vertex ID
        storage = Queue()
        storage.enqueue(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while storage.size() > 0:
            # Dequeue the first vertex
            dqed_vert = storage.dequeue()
            # If that vertex has not been visited...
            if dqed_vert not in visited:
                # Visit it
                print(dqed_vert)
                # Mark it as visited...
                visited.add(dqed_vert)
                # Then add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(dqed_vert):
                    storage.enqueue(next_vert)
        # print("=" * 25)

    def dft(self, starting_vertex):
        # print("=" * 25)
        # print("  DFT ")
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # TODO - use a STACK
        # create and empty stack and set to a var
        storage = Stack()
        # push beginning vertex to top of stack
        storage.push(starting_vertex)
        # create a visited set() var
        visited = set()
        # while the stack is not empty...
        while storage.size() > 0:
            # pop the top item
            popped_vert = storage.pop()
            # if that vertex has not been visited...
            if popped_vert not in visited:
                # visit it
                print(popped_vert)
                # mark it as visited...
                visited.add(popped_vert)
                # then add all of its neighbors to the top of the stack
                for next_vert in self.get_neighbors(popped_vert):
                    storage.push(next_vert)
        # print("=" * 25)

    def dft_recursive(self, vertex, visited=None):
        """
        visted can not be a set() bc
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # TODO
        # initial case needed
        # if we do not have a visited in place initialize it
        if visited is None:
            # add a set() to the visited vertex
            visited = set()

        # base case needed as well - how do we know we are done?
        # when we have no more neighbors
        # no explicit base case here bc we are handling that in our for loop below `self.dft_recursive(neighbor, visited)`

        # track visited nodes
        visited.add(vertex)
        print(vertex)

        # call the function recursively - on neighbors of not visited
        for neighbor in self.vertices[vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # initialize empty list
        path = []
        # Create an empty stack and push A PATH TO the starting vertex ID
        s = Stack()
        s.push(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()

        # While the stack is not empty...
        while s.size() > 0:
            # pop the first PATH
            # Grab the last vertex from the PATH
            vert = s.pop()
            # If that vertex has not been visited...
            if vert not in visited:
                print(vert)
                # Mark it as visited...
                visited.add(vert)
                path.append(vert)

                # CHECK IF IT'S THE TARGET
                if vert == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Then add A PATH TO its neighbors to the back of the stack
                for next_vert in self.get_neighbors(vert):
                    # APPEND THE NEIGHOR TO THE BACK
                    s.push(next_vert)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # Create an empty queue...
        qq = Queue()

        # ...and enqueue A PATH TO the starting vertex ID
        print(qq.enqueue([starting_vertex]))

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while qq.size() > 0:
            # Dequeue the first PATH
            path = qq.dequeue()
            print(path)

            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            print(last_vertex)

            # If that vertex has not been visited...
            if last_vertex not in visited:
                # Mark it as visited...
                visited.add(last_vertex)
                # CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
                    # IF SO, RETURN PATH
                    return path

            # Then add A PATH TO its neighbors to the back of the queue
            for next_vert in self.get_neighbors(last_vertex):
                # COPY THE PATH
                new_path = list(path)
                # APPEND THE NEIGHOR TO THE BACK
                new_path.append(next_vert)
                qq.enqueue(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # TODO
        # initial case needed
        # if we do not have a visited in place initialize it
        if visited is None:
            # add a set() to the visited vertex
            visited = set()

        if path is None:
            path = []

        # base case needed as well - how do we know we are done?
        # when we have no more neighbors
        # no explicit base case here bc we are handling that in our for loop below `self.dft_recursive(neighbor, visited)`

        # track visited nodes
        visited.add(starting_vertex)
        # copy the path
        new_path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return new_path

        # call the function recursively - on neighbors of not visited
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                neighbor_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, new_path)
                if neighbor_path:
                    return neighbor_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    # graph.add_edge(0, 4)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
