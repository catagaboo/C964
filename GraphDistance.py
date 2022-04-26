# Vertex class creates Vertex objects to be place inside the graph
class Vertex:
    def __init__(self, vertex_id, name, address, city, state, zip_code):
        self.id = vertex_id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code


# Graph class creates a graph object that contains Vertex objects and weighted edges between vertices
class Graph:
    vertices = []
    edges = []

    # This takes the Vertex object, adds it to a 2d matrix, and appends all edge weights to zero to fill graph - O(N)
    def add_vertex(self, new_vertex):
        self.vertices.append(new_vertex)
        for row in self.edges:
            row.append(0)
        self.edges.append([0] * (len(self.edges) + 1))

    # This takes two Vertex ID's and the distance between those vertices - O(1)
    def add_edge(self, u, v, distance):
        self.edges[u - 1][v - 1] = distance
        self.edges[v - 1][u - 1] = distance

    # This takes two Vertex ID's and returns the distance between them - O(1)
    def get_distance(self, current_index, package_index):
        return float(self.edges[current_index - 1][package_index - 1])
