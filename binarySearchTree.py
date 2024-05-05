class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class binarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = node(data)
        else:
            self._insert(self.root, data)
        return None

    def _insert(self, new_node, data):
        if data < new_node.data:
            if new_node.left is None:
                new_node.left = node(data)
            else:
                self._insert(new_node.left, data)
        else:
            if new_node.right is None:
                new_node.right = node(data)
            else:
                self._insert(new_node.right, data)
        return None

    def show_tree(self, new_node, level=0):
        if new_node is not None:
            self.show_tree(new_node.right, level + 1)
            print(' ' * 4 * level + '->', new_node.data)
            self.show_tree(new_node.left, level + 1)

    def main(self):
        for i in [1, 2, 3, 4, 5, 6, 7]:
            self.insert(i)
        self.show_tree(self.root)


test_binaryTree = binarySearchTree()
test_binaryTree.main()