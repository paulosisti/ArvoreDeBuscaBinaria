from Node import Node
from BinaryTree import BinaryTree

ROOT = "root"


class BinarySearchTree(BinaryTree):

    def insert(self, value):
        parent = None
        x = self.root
        while (x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif parent.data == value:
            return print('Valor já existe')
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return print(f'Elemento {value} não existe')
        if node.data == value:
            return print(f'Valor {value} encontrado\nEndereço: {BinarySearchTree(node)}')
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)

    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def remove(self, value, node=ROOT):
        # Se for o valor padrão, executa a partir da raiz
        if node == ROOT:
            node = self.root
        # Se desceu até um ramo nulo, não há nada a fazer
        if node is None:
            return print(f'Elemento {value} não existe')
        # Se o valor for menor, desce à esquerda
        if value < node.data:
            node.left = self.remove(value, node.left)
        # Se o valor for maior, desce à direita
        elif value > node.data:
            node.right = self.remove(value, node.right)
        # Se não for nem menor, nem maior, encontramos! Vamos remover...
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Substituto é o sucessor do valor a ser removido
                substitute = self.min(node.right)
                # Ao invés de trocar a posição dos nós, troca o valor
                node.data = substitute
                # Depois, remove o substituto da subárvore à direita
                node.right = self.remove(substitute, node.right)
        return node

    def show(self, current_node):
        if current_node != None:
            print('%d' % current_node.data, end=' ')
            # RECURSIVO
            self.show(current_node.left)
            self.show(current_node.right)

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node, end=' ')

    def preorder_traversal(self, node=None):
        if node is None:
            node = self.root
        print(node, end=' ')
        if node.left:
            self.preorder_traversal(node.left)
        if node.right:
            self.preorder_traversal(node.right)

    def preorder_traversal_collumn(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print(node, '->', node.left, end='\n')
            self.preorder_traversal_collumn(node.left)
        if node.right:
            print(node, '->', node.right, end='\n')
            self.preorder_traversal_collumn(node.right)

    def postorder_traversal_collumn(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal_collumn(node.left)
            print(node.left, '->', node, end='\n')
        if node.right:
            self.postorder_traversal_collumn(node.right)
            print(node.right, '->', node, end='\n')

    def getRoot(self):
        return self.root

    def nivel_traversal(self, node=None, level=0):
        if node is None:
            node = self.root
        if node.right:
            self.nivel_traversal(node.right, level + 1)
        print('    '*level + str(node))
        if node.left:
            self.nivel_traversal(node.left, level + 1)

    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1
