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
