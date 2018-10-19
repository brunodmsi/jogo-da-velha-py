def checar_vetor(vetor):
	if vetor[0]==vetor[1]==vetor[2]=='x':
		return 'x'
	if vetor[0]==vetor[1]==vetor[2]=='o':
		return 'o'
	return 0

def checar_diagonais(jogo):
	diag=[]
	for l in range(len(jogo)):
		for c in range(len(jogo[0])):
			if l==c:
				diag.append(jogo[l][c])
	r=checar_vetor(diag)
	if r!=0:
		return r

	diag=[]
	i=0
	for l in range(len(jogo)):
		j=0
		for c in range(len(jogo[0])):
			if i==3-1-j:
				diag.append(jogo[l][c])
			j=j+1
		i=i+1
	r=checar_vetor(diag)
	if r!=0:
		return r

	return 0

def checar_horizontais(jogo):
	for l in jogo:
		if l[0]=='x' and l[1]=='x' and l[2]=='x':
			return 'x'
		if l[0]=='o' and l[1]=='o' and l[2]=='o':
			return 'o'
	return 0

def checar_verticais(jogo):
	if jogo[0][0]=='x' and jogo[1][0]=='x' and jogo[2][0]=='x':
		return 'x'
	if jogo[0][1]=='x' and jogo[1][1]=='x' and jogo[2][1]=='x':
		return 'x'
	if jogo[0][2]=='x' and jogo[1][2]=='x' and jogo[2][2]=='x':
		return 'x'

	if jogo[0][0]=='o' and jogo[1][0]=='o' and jogo[2][0]=='o':
		return 'o'
	if jogo[0][1]=='o' and jogo[1][1]=='o' and jogo[2][1]=='o':
		return 'o'
	if jogo[0][2]=='o' and jogo[1][2]=='o' and jogo[2][2]=='o':
		return 'o'
	return 0


def checar_vitoria(jogo):
	diag=checar_diagonais(jogo)
	if diag!=0:
		return diag

	vert=checar_verticais(jogo)
	if vert!=0:
		return vert

	hor=checar_horizontais(jogo)
	if hor!=0:
		return hor

	return 0
