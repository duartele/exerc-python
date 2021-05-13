from time import sleep
from ex01.arquivo import *
from ex01.funcoes import *

arquivo = 'base_ex01.txt'

if not arqExiste(arquivo):
    criarArq(arquivo)

while True:
    resposta = menu(['Criar Arquivo', 'Cadastar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('Opção 3')
    elif resposta == 4:
        print('Finalizando. Obrigado, volte sempre....')
        break
    else:
        print('Valor inválido. Escolha outra opcao.')
    sleep(2)
