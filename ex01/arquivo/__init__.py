from ex01.funcoes import *


def arqExiste(nome):
    try:
        a = open(nome, 'rt') #rt = read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome):
    try:
        a = open(nome, 'wt+') #wt = write text and + = create one if it not exists
        a.close()
    except:
        print('Hove um erro na criacao do arquivo')
    else:
        print('Arquivo criado com sucesso')


def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Hove um erro na leitura do arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at') # at = append no txt
    except:
        print('Houve um erro ao cadastrar')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve erro ao executar a.write')
        else:
            print('Novo registro adicionado com sucesso')
            a.close()


