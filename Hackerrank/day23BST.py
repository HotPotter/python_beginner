import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def levelOrder(self,root):
        if root == None:
            return None
        else:
            tree_queue = [root]
            order_list = []
            while tree_queue:
                node = tree_queue.pop(0)
                order_list.append(node.data)
                if node.left:
                    tree_queue.append(node.left)
                if node.right:
                    tree_queue.append(node.right)
        print(' '.join(str(i)for i in order_list))


'''solution 1'''
    # def levelOrder(self, root):
    #
    #     queue = [root] if root else []
    #
    #     while queue:
    #         node = queue.pop()
    #         print(node.data, end=" ")
    #
    #         if node.left: queue.insert(0, node.left)
    #         if node.right: queue.insert(0, node.right)
'''solution 2'''
    # def levelOrder(self, root):
    #     q = [root]
    #     # i = 0
    #
    #     # while i < len( q ):
    #     #    current = q[i]
    #     #    i += 1
    #
    #     for current in q:
    #         if current:
    #             print(current.data, end=' ')
    #
    #             q.append(current.left)
    #             q.append(current.right)


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
