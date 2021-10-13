# This is a Python script.

import os, fnmatch, shutil

def find_all(name, path):
    result = []
    count = 0
    for root, dirs, files in os.walk(path):
        if name in files:
            count = count + 1
            print(os.path.join(root, name))
            result.append(os.path.join(root, name))
    print(f'Total encontrados de ', {name}, ' # ', count)
    return result


def findMatch(pattern, path):
    result = []
    count = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                count = count + 1
                print(os.path.join(root, name), ' | arquivo ', pattern, ' # ' ,count )
              #  result.append(os.path.join(root, name))
    if count == 0:
       print('Nao encontrou arquivo ', pattern)
    return  # result

def pesqLista(filepath, dirpesq):
    # abrir arquivo e montar a lista e pesquisar
    print('Pesquisando arquivos de ', filepath, ' em ', dirpesq)
    file = open(filepath, 'r' )
    count = 0
    for line in file:
        count+=1
        # remove linebreak
        nomeArquivo =line.rstrip('\n')
        nomeArquivo = '*' + nomeArquivo + '*'
        findMatch(nomeArquivo, dirpesq)
    return count

def findMatchCopy(pattern, path, dest):
    # acha o aquivo em path com padrao pattern (exemplo '*nome*') para destino
    result = []
    count = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                count = count + 1
                fdir = os.path.join(root, name)
                # print(fdir, ' | arquivo ', name , ' # ' ,count )
                try:
                    shutil.copy(fdir, dest )
                except:
                    print("Erro de copia de ", fdir, " ou arquivo existente ", dest)

              #  result.append(os.path.join(root, name))
    if count == 0:
       print('Nao encontrou arquivo ', pattern, ' em ' , path  )
    return  # result

def pesqListaCopia(filepath, dirpesq, dirdestino):
    # pesquisa lista de arquivos,  montar a lista, busca e copia arquivos para destino
    print('Pesquisando arquivos de ', filepath, ' em ', dirpesq)
    file = open(filepath, 'r' )
    count = 0
    for line in file:
        count+=1
        # remove linebreak
        nomeArquivo =line.rstrip('\n')
        nomeArquivo = '*' + nomeArquivo + '*'
        findMatchCopy(nomeArquivo, dirpesq, dirdestino)
    return count

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    listaArquivo = './lista.txt'
    ###sourcedir= 'D:/DIR/2016';
    sourcedir = 'C:/Users/leandro.leao/OneDrive';
    destination = './dest'
    print('----------------------')
    print('Procurar arquivos de ', listaArquivo, ' copia para ', destination )
    print('----------------------')
    c = 0
#   c = pesqLista(listaArquivo, notasdir)
#   findMatchCopy('lista.txt', 'D:/RD/NF2016', notasdest)
    c = pesqListaCopia(listaArquivo, sourcedir, sourcedir)
    print('Concluido! Linhas #', c)

    """
    find_all('*95104*.pdf', sourcedir)
    findm('*17127*', sourcedir)
    """
    print('Fim')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
