# -*- coding: iso8859-1 -*-

from collections import namedtuple

import menu


alunoReg = namedtuple("alunoReg", "id, nome")
listaAlunos = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaAlunos)):
        if listaAlunos[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_aluno():
    cod = input("Qual o codigo? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "C�digo j� existe"
        return

    #ler dados
    nome = raw_input("Qual o nome? ")
    
    registo = alunoReg(cod, nome)
    listaAlunos.append(registo)


def pesquisar_aluno():
    cod = input("Qual o codigo do aluno a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "N�o existe aluno com esse c�digo"
        return

    print "C�digo: ", listaAlunos[pos].id
    print "Nome: ", listaAlunos[pos].nome
    


def listar_alunos():
    
    print "  C�digo  |          Nome"
    print "-"*50
    for i in range (len(listaAlunos)):        
        print "%6d    | %s " % (listaAlunos[i].id, listaAlunos[i].nome)
        print "-"*50
        
        
  

def eliminar_aluno():
    cod = input ("C�digo do aluno a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "N�o existe aluno com esse c�digo"
        return

    # TODO: Confirmar elimina��o
    listaAlunos.pop(pos)


    
def alterar_aluno():
    cod = input ("C�digo do aluno a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "N�o existe aluno com esse c�digo"
        return

    # s� altera o nome
    novonome = raw_input("Qual o nome? ")
    listaAlunos[pos] = listaAlunos[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.alunos()

        if op == '1':
            inserir_aluno()
        elif op =='2':
            listar_alunos()
        elif op == '3':
            pesquisar_aluno()
        elif op == '4':
            alterar_aluno()
        elif op == '5':
            eliminar_aluno()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa n�o deve ser executado diretamente"










