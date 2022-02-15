class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.leftchild = left
        self.rightchild = right

def search(searchValue, node):
    if node is None or node.value == searchValue:
        return node
    elif searchValue < node.value:
        return search(searchValue, node.leftchild)
    elif searchValue > node.value:
        return search(searchValue, node.rightchild)

def insert(value, node):
    if value < node.value:
        if node.leftchild is None:
            node.leftchild = TreeNode(value)
        else:
            insert(value, node.leftchild)
    elif value > node.value:
        if node.rightchild is None:
            node.rightchild = TreeNode(value)
        else:
            insert(value, node.rightchild)

def delete(value, node):
    if node is None:
        return None

    elif value < node.value:
        node.leftchild = delete(value, node.leftchild)
        return node

    elif value > node.value:
        node.rightchild = delete(value, node.rightchild)
        return node

    elif value == node.value:
        if node.leftchild is None:
            return node.rightchild

        elif node.rightchild is None:
            return node.leftchild

        else:
            node.rightchild = lift(node.rightchild, node)
            return node

def lift(node, nodeToDelete):
    if node.leftchild is not None:
        node.leftchild = lift(node.leftchild, nodeToDelete)
        return node

    else:
        nodeToDelete.value = node.value
        return node.rightchild

def max(node): #15-4 solution
    if node.rightchild is not None:
        node.rightchild = max(node.rightchild)
        return node

    else:
        return node.value

node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)
print(search(25, root).value)