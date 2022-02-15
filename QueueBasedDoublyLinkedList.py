class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
        cur.next.prev = cur

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cnt = 0
        cur = self.head
        while cnt < index:
            cnt += 1
            cur = cur.next
        return cur

    def add_node(self, index, data):
        newNode = Node(data)
        if index == 0:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        else:
            prev_node = self.get_node(index-1)
            newNode.next = prev_node.next
            newNode.prev = prev_node
            prev_node.next = newNode
            newNode.next.prev = newNode

    def del_node(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            prev_node = self.get_node(index-1)
            prev_node.next = prev_node.next.next
            prev_node.next.prev = prev_node

class Queue:
    def __init__(self, data):
        self.data = LinkedList(data)

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        removed_node = self.data.get_node(0)
        self.data.del_node(0)
        return removed_node

    def read(self):
        return self.data.get_node(0)

queue = Queue("yellow")
queue.enqueue("blue")
queue.enqueue("green")
queue.enqueue("red")
for i in range(4):
    print(queue.dequeue().data)