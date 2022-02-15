class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, element):
        self.data.append(element)
    
    def dequeue(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        else:
            return False

    def read(self):
        if len(self.data) > 0:
            return self.data[0]
        else:
            return False

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
            if vertex in self.adjacent_vertices:
                return None
            self.adjacent_vertices.append(vertex)
            vertex.add_adjacent_vertex(self)

def bfs_traverse(starting_vertex):
    queue = Queue()
    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True
    queue.enqueue(starting_vertex)

    while queue.read():
        current_vertex = queue.dequeue()
        print(current_vertex.value)
        for adjacent_vertices in current_vertex.adjacent_vertices:
            if adjacent_vertices.value in visited_vertices:
                None
            else:
                visited_vertices[adjacent_vertices.value] = True
                queue.enqueue(adjacent_vertices)

def bfs(starting_vertex, search_value): #18-4 solution
    queue = Queue()
    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True
    queue.enqueue(starting_vertex)

    while queue.read():
        current_vertex = queue.dequeue()
        if current_vertex.value == search_value:
            return current_vertex
        for adjacent_vertices in current_vertex.adjacent_vertices:
            if adjacent_vertices.value in visited_vertices:
                None
            else:
                visited_vertices[adjacent_vertices.value] = True
                queue.enqueue(adjacent_vertices)

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

bfs_traverse(alice)
print(bfs(alice, "bob").value)