import random
from util import Stack, Queue  # These may come in handy


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            # creating the two way edges to connect friends
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        # create a new user class with a name
        self.users[self.last_id] = User(name)
        # create a graph of sets() - friendships graph for this new user
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        UNDIRECTED GRAPH
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}  # my NODES!!
        self.friendships = {}  # EDGES!! determine friendships
        # !!!! IMPLEMENT ME
        # 1. add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        # 2. generate all possible friendships
        possible_friendships = []

        # 2a. Avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # 3. shuffle the possible firenships
        random.shuffle(possible_friendships)

        # 4. go through the list of shuffled friendships, adding the right number of them to reach average friendships
        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.

        {friendID: [a ~> b ~> c]}    

        {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
        {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}

        PLAN
        - Hint 1: What kind of graph search guarantees you a shortest path? BREADTH FIRST SESRCH
        - we need a Q
        - we need to enque our input which is a user ID
        - we should create a dict for the visited nodes in order to keep track of connected components
        - create a path for all nodes that are connected
        - find the neighbors for our nodes and return a new copy of the path
        """

        # create a Q storage
        storage = Queue()

        # enqueue our user ID in a list in order to proprly access last vert in that path
        storage.enqueue([user_id])

        # visited is given to us and we use it to look up if a node has been visited in O(1)
        visited = {}  # Note that this is a dictionary, not a set

        # as long as our storage is not empty, find paths and check neighbors to traverse our graph
        while storage.size() > 0:

            # create a temp path which begins with our first item in line aka user_id
            path = storage.dequeue()

            # create a vertex variable that will hold the last index of our path above
            # this vertex will be the last node of every path
            vertex = path[-1]

            # check if our last node of every path is in the visited dict
            if vertex not in visited:

                # if it ^^ is not...take the node index in our visited dict and update it with the current path
                visited[vertex] = path

                # loop through our friendships list and pull all the neighbors / connected nodes at the vertext we are currently on
                for neighbor in self.friendships[vertex]:
                    # create a copy of our path bc we are in a for loop
                    new_path = list(path)
                    # create a path with all connected nodes in one connected component
                    new_path.append(neighbor)
                    # put that path back in the Q to ensure the entire path has been created
                    storage.enqueue(new_path)
        # we return the visited dict bc we are finding the shortest path between friendships which is store in the visited dict()
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
