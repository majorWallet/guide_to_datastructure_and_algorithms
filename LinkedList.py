class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self): #14-1 solution
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur=cur.next

    def get_node(self, index):
        cnt = 0
        cur = self.head
        while cnt < index:
            cnt += 1
            cur = cur.next
        return cur

    def get_last_node(self): #14-3 solution
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        return cur

    def add_node(self, index, data):
        newNode = Node(data)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            prev_node = self.get_node(index-1)
            newNode.next = prev_node.next
            prev_node.next = newNode

    def reverse(self): #14-4 solution
        prev = None
        cur = self.head
        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def del_node_1(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            prevNode = self.get_node(index-1)
            prevNode.next = prevNode.next.next

    def del_node_2(node): #14-4 solution
        node = node.next
        node.next = node.next.next

linkedList = LinkedList("yellow")
linkedList.append("blue")
linkedList.append("green")
linkedList.append("red")
linkedList.print_all()
linkedList.add_node(2, "purple")
linkedList.del_node_1(3)
linkedList.print_all()
print(linkedList.get_last_node().data)