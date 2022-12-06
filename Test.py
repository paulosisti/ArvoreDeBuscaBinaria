
from BinarySearchTree import BinarySearchTree


class Test_BST:

    def example_tree():
        values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 100, 90]
        tree = BinarySearchTree()
        for v in values:
            tree.insert(v)
        return tree

    bst = example_tree()
    print('Árvore Binária')
    bst.show(bst.getRoot())
    print('\n------')

    print('AB: Ordem Simétrica')
    bst.inorder_traversal()

    print('\n------')
    print('AB: Pós Ordem')
    print('AB: Before Remove')
    bst.postorder_traversal()
    bst.remove(89)
    print('\nAB: After Remove')
    bst.postorder_traversal()

    print('\n------')
    print('AB: Pré Ordem')
    print('AB: Before Remove')
    bst.preorder_traversal()
    bst.remove(66)
    print('\nAB: After Remove')
    bst.preorder_traversal()

    print('\n------')
