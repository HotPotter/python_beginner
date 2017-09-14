
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)

        else:
            node = self.root
            while True:
                if data < node.data and node.left is None:
                    node.left = Node(data)
                    break
                elif data < node.data and node.left is not None:
                    node = node.left
                elif data > node.data and node.right is None:
                    node.right = Node(data)
                    break
                elif data > node.data and node.right is not None:
                    node = node.right

    def get_height(self):
        node = self.root
        nodes = [node]
        height = 1
        while True:
            child_nodes_list = [[node.left, node.right] for node in nodes]
            child_nodes = [node for child_nodes in child_nodes_list for node in child_nodes]
            non_empty_nodes = [node for node in child_nodes if node is not None]
            nodes = non_empty_nodes
            if nodes == []:
                break
            else:
                height += 1
        return height

    def get_height_r(self):
        return self.get_height_r_(self.root)
    def get_height_r_(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.get_height_r_(node.left), self.get_height_r_(node.right))




t = Tree()
t.insert(3)
print(t.get_height())
print(t.get_height_r())
t.insert(1)
print(t.get_height())
print(t.get_height_r())
t.insert(2)
print(t.get_height())
print(t.get_height_r())
t.insert(0.5)
print(t.get_height())
print(t.get_height_r())
t.insert(1.5)
print(t.get_height())
print(t.get_height_r())


'''
t = Tree()
for i in range(0, 990):
    t.insert(i)
print(t.get_height_r())
'''
'''
def get_height(Node):
    if Node.left == None and Node.right == None:
        return 0
    else:
        return 1 + max(get_height(Node.left, get_height(Node.right))
'''

