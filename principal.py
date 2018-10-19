import random
from os import system,name
import checar.checar as checar
import jogadas.jogada as jogada
import jogadas.comandos_pc as comando
import arquivos.arquivo as arquivo

def clear():
	if name=='nt':
		_=system('cls')
	else:
		_=system('clear')

def tem_ganhador():
	clear()
	arquivo.salvar_vitoria(jogo,ganhador)
	printa(jogo)
	print()
	print("FIM DE JOGO!\nO GANHADOR FOI: ")
	if ganhador=='x': print("->>> USUARIO")
	else: print("->>> CPU")

	print()
	b=jogar_novamente()
	jogada_pronta=None
	if b==1:
		return 1
	if b==2: return 2

def printa(jogo):
	for l in jogo:
		print(l)

def jogar_novamente():
	b=int(input("Gostaria de jogar novamente?\n  1 - Sim\n  2 - Nao\n-> "))
	return b

condicao=True
espacos=9
ganhador=''
jogada_pronta=None

jogo=[[' ']*3,[' ']*3,[' ']*3]

while(condicao):

	if jogada_pronta==None:
		jogada_pronta=comando.pega_jogada()

	jogo=jogada.pc(jogo,jogada_pronta)
	espacos=espacos-1
	ganhador=checar.checar_vitoria(jogo)

	if(ganhador!=0):
		b=tem_ganhador()
		if b==1:
			jogo=[[' ']*3,[' ']*3,[' ']*3]
			espacos=9
		if b==2: break

	if(espacos==0):
		clear()
		print("Jogo terminou EMPATADO!\nResultado final:")
		printa(jogo)
		b=jogar_novamente()
		jogada_pronta=None
		jogo=[[' ']*3,[' ']*3,[' ']*3]
		if b==2:break

	clear()
	printa(jogo)
	jogo=jogada.user(jogo)
	espacos=espacos-1
	ganhador=checar.checar_vitoria(jogo)

	if(ganhador!=0):
		b=tem_ganhador()
		if b==1:
			jogo=[[' ']*3,[' ']*3,[' ']*3]
			espacos=9
		if b==2: break
