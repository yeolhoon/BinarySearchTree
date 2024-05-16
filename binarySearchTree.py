from binaryTree import binaryTree, node


class binarySearchTree(binaryTree):
    def __init__(self):
        super().__init__()

    def _insert(self, cur_node, data):
        if data < cur_node.data:
            if not cur_node.left:
                cur_node.left = node(data)
            else:
                self._insert(cur_node.left, data)
        else:
            if not cur_node.right:
                cur_node.right = node(data)
            else:
                self._insert(cur_node.right, data)


def main():
    test_binarySearchTree = binarySearchTree()
    for i in [4, 3, 7, 10, 5, 6, 8]:
        test_binarySearchTree.insert(i)
    test_binarySearchTree.show_tree(test_binarySearchTree.root)


if __name__ == "__main__":
    main()
