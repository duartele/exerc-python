from time import sleep
from ex01.arquivo import *
from ex01.funcoes import *

arquivo = 'base_ex01.txt'

if not arqExiste(arquivo):
    criarArq(arquivo)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArq(arquivo)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        print('Finalizando. Obrigado, volte sempre....')
        break
    else:
        print('Valor inválido. Escolha outra opcao.')
    sleep(2)
