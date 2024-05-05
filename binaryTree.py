class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class binaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = node(data)
        else:
            self._insert(self.root, data)
        return None

    def _insert(self, queue_data, data):
        queue = [queue_data]
        new_node = node(data)

        while queue:
            cur_node = queue.pop(0)
            if cur_node.left == None:
                cur_node.left = new_node
                break
            else:
                queue.append(cur_node.left)

            if cur_node.right == None:
                cur_node.right = new_node
                break
            else:
                queue.append(cur_node.right)
        return None

    def show_tree(self, new_node, level=0):
        if new_node is not None:
            self.show_tree(new_node.right, level + 1)
            print(' ' * 4 * level + '->', new_node.data)
            self.show_tree(new_node.left, level + 1)
        return None

    def main(self):
        for i in [1, 2, 3, 4, 5, 6, 7]:
            self.insert(i)
        self.show_tree(self.root)


test_binaryTree = binaryTree()
test_binaryTree.main()