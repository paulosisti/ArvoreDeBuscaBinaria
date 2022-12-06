def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU DE OPÇÕES')
    option = 1
    for item in lista:
        print(f'\033[33m[{option}]\033[m - \033[34m{item}\033[m')
        option += 1
    print(linha())
    opt = validaInt('\033[32mSua opção: \033[m')
    return opt


def validaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR: Digite um valor inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERROR: Sistema Interrompido.\033[m')
            return 0
        else:
            return n


def linhaFinal():
    return input('Tecle ENTER para voltar ao MENU')
