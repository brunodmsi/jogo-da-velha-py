import random
import arquivos.arquivo as a

def pega_jogada():
    if a.contar_jogadas()==0: return None
    if a.contar_jogadas()<15:
        return pega_ultima_jogada()
    else:
        return pega_jogada_rand()

def jogada_aleatoria(jogo):
    check='!'
    while check=='!':
        jogada=num_aleatorios(jogo)
        check=checar_ocupado(jogo,jogada)
        if check==1:
            jogo[jogada[0]][jogada[1]]='o'
    return jogo

def checar_ocupado(jogo,jogada):
    if jogo[jogada[0]][jogada[1]]==' ':
        return 1
    else:
        return '!'

def num_aleatorios(jogo):
    tmp=[]
    rand_x=random.randrange(0,3)
    rand_y=random.randrange(0,3)
    return (rand_x,rand_y)

def pega_ultima_jogada():
    linha=None
    cont=0
    num=a.contar_jogadas()
    with open('jogadas.txt','r') as f:
        for l in f:
            cont+=1
            if cont==num:
                linha=l
    return str_to_list(linha)

def pega_jogada_rand():
    linha=None
    num=random.randrange(0, a.contar_jogadas())
    cont=0
    with open('jogadas.txt','r') as f:
        for l in f:
            cont+=1
            if cont==num:
                linha=l
    return str_to_list(linha)

def limpa_lista(linha):
    tmp=''
    for char in range(len(linha)):
        if linha[char]=='0' or linha[char]=='1':
            tmp+=linha[char]
    return tmp

def str_to_list(linha):
    jogada=limpa_lista(linha)
    tmp=[[' ']*3,[' ']*3,[' ']*3]
    i=0
    for l in range(len(tmp)):
        for c in range(len(tmp[0])):
            tmp[l][c]=int(jogada[i])
            i+=1
    return tmp
