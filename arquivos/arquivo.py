import pickle
import random

def jogada_vitoriosa(jogo,ganhador):
    tmp=[]
    for l in range(len(jogo)):
        for c in range(len(jogo[0])):
            if jogo[l][c]==ganhador:
                tmp.append(1)
            else:
                tmp.append(0)
    return tmp

def salvar_vitoria(jogo,ganhador):
    jogada=jogada_vitoriosa(jogo,ganhador)
    with open('jogadas.txt','a') as f:
        f.write(str(jogada)+"\n")
    f.close()

def contar_jogadas():
    num=0
    f=open('jogadas.txt','r')
    for l in f:
        num+=1
    return num

def aleatorio():
    linhas=open('jogadas.txt').read().splitlines()
    linha=random.choice(linhas)
    return linha
