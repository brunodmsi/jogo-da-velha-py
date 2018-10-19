import arquivos.arquivo as a
import random
import jogadas.comandos_pc as comando

def user(jogo):
    posicao_ok=0
    while(posicao_ok==0):
        usuario_X_l=int(input("Usuario X -> Entre linha (1-3): "))
        usuario_X_c=int(input("Usuario X -> Entre coluna (1-3): "))

        if jogo[usuario_X_l-1][usuario_X_c-1] != ' ':
            print("Posicao ja usada! Escolha outra!")
        else:
            jogo[usuario_X_l-1][usuario_X_c-1]='x'
            posicao_ok=1
    return jogo

def pc(jogo,jogada=None):
    check='!'
    if a.contar_jogadas()==0:
        jogo=comando.jogada_aleatoria(jogo)

    if a.contar_jogadas()>=1:
        bool=False
        quebra_jogada=False
        check='!'
        tmp=''
        for l in range(len(jogada)):
            for c in range(len(jogada[0])):
                if jogada[l][c]==1:
                    tmp=(l,c)
                    jogada[l][c]=0
                    bool=True

                if bool==True:break
            if bool==True:break
        if(tmp!=''):
            check=comando.checar_ocupado(jogo,tmp)
        if check==1:
            jogo[tmp[0]][tmp[1]]='o'
        else:
            quebra_jogada=True
            jogo=comando.jogada_aleatoria(jogo)

    return jogo
