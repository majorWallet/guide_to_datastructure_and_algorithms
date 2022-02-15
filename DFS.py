class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
            if vertex in self.adjacent_vertices:
                return None
            self.adjacent_vertices.append(vertex)
            vertex.add_adjacent_vertex(self)

def dfs_traverse(vertex, visited_vertices={}):
    visited_vertices[vertex.value] = True
    print(vertex.value)
    for adjacent_vertex in vertex.adjacent_vertices:
        if adjacent_vertex.value in visited_vertices:
            None
        else:
            dfs_traverse(adjacent_vertex, visited_vertices)

def dfs(vertex, search_value, visited_vertices={}):
    if vertex == search_value:
        return vertex
    visited_vertices[vertex.value] = True
    for adjacent_vertex in vertex.adjacent_vertices:
        if adjacent_vertex.value in visited_vertices:
            None
        else:
            if adjacent_vertex.value == search_value:
                return adjacent_vertex
            vertex_were_searching_for = dfs(adjacent_vertex, search_value, visited_vertices)
            if vertex_were_searching_for:
                return vertex_were_searching_for

alice = Vertex("alice")
bob = Vertex("bob")
fred = Vertex("fred")
helen = Vertex("helen")
candy = Vertex("candy")
derek = Vertex("derek")
gina = Vertex("gina")
irena = Vertex("irena")
elaine = Vertex("elaine")

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(candy)
alice.add_adjacent_vertex(derek)
alice.add_adjacent_vertex(elaine)
bob.add_adjacent_vertex(fred)
fred.add_adjacent_vertex(helen)
helen.add_adjacent_vertex(candy)
derek.add_adjacent_vertex(elaine)
derek.add_adjacent_vertex(gina)
gina.add_adjacent_vertex(irena)

#dfs_traverse(alice)
print(dfs(alice, "helen").value)