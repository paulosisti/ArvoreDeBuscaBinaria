from BinarySearchTree import BinarySearchTree
from Menu import *
from time import sleep

# inserção manual item a item
# tree = BinarySearchTree()

# inserção automática de vários itens


def example_tree():
    values = [53, 30, 72, 14, 39, 61, 84, 9, 23, 34, 49, 79]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree


bst = example_tree()

while True:
    resposta = menu(['Inserir', 'Remover', 'Travessia Pre-Ordem', 'Travessia In-ordem', 'Travessia Pos-Ordem',
                     'Mostrar Ligações Pré-Ordem', 'Mostrar Ligações Pós-Ordem', 'Busca', 'Altura', 'Sair'])

    if resposta == 1:
        res = validaInt('Valor a ser inserido: ')
        bst.insert(res)
        print('Valor inserido com sucesso!')
    elif resposta == 2:
        res = validaInt('Valor a ser removido: ')
        bst.remove(res)
    elif resposta == 3:
        print("\nPRE:\n")
        bst.preorder_traversal()
        print('\n------\n')
        linhaFinal()
    elif resposta == 4:
        print("\nIN:\n")
        bst.inorder_traversal()
        print('\n------\n')
        linhaFinal()
    elif resposta == 5:
        print("\nPOS:\n")
        bst.postorder_traversal()
        print('\n------\n')
        linhaFinal()
    elif resposta == 6:
        bst.preorder_traversal_collumn()
    elif resposta == 7:
        bst.postorder_traversal_collumn()
    elif resposta == 8:
        res = validaInt('Valor a ser procurado: ')
        print('Buscando...')
        sleep(2)
        bst.search(res)
    elif resposta == 9:
        print(f'Altura da Árvore: {bst.height()}')
    elif resposta == 10:
        cabecalho('Desligando sistema...')
        break
    elif resposta == 11:
        bst.nivel_traversal()
        linhaFinal()
    else:
        print('\033[31mERROR: Digite uma opção válida!\033[m')
    sleep(2)
