#-*- coding:utf-8 -*-

nome_engenharia = ""  #insira o nome da engenharia aqui

def ProcessaVertices(x,n = None): #OK
		vertices = []
		if n!=None:
			n=0
		for lista in x:
			vertices.append(lista.split(";"))
			if n!=None:
				n+=1

		if n!=None:
			return (vertices,n-1)
		else:
			return vertices

def TemDependencia(disci,arestas): #OK
	'''
	Retorna:
		True 	- existe dependencia
		False 	- nao existe dependencia
	'''
	nome_disci = str(disci)
	TemDep = False
	for i in range(1,len(arestas)):
		if str(arestas[i][1]) == nome_disci:
			TemDep = True
	return TemDep

def ProcuraDependencia(disci,arestas): #OK
	nome_disci = str(disci)
	dep = []
	for i in range(1,len(arestas)):
		if str(arestas[i][1]) == nome_disci:
			dep.append(arestas[i])
	return dep

def ContaQuad(disciplinas,quad): #OK
	n = 0
	for i in range(1,len(disciplinas)):
		tmp = str(disciplinas[i][5].strip())
		if tmp.isdigit():
			if int(tmp) == int(quad):
				n+=1
	return n

def QuadIdeal(disciplinas,quad): #OK
	quadri = []
	for i in range( 1 , (len(disciplinas)) ):
		tmp = str(disciplinas[i][5].strip())
		if tmp.isdigit():
			if int(tmp) == int(quad):
				quadri.append(disciplinas[i])
	return quadri

def CheckPilha(disci, pilha): #OK
	Chck = True
	for i in range(len(pilha)):
		if pilha[i] == disci:
			Chck = False
	return Chck

def AddPilha(dependencia,pilha): #OK
	for i in range(len(dependencia)):
		if CheckPilha(dependencia[i],pilha):
			pilha.append(dependencia[i])
	return pilha

def GeraAresta(v_remove,pilha):
	novas_a = []
	for i in range(len(pilha)):
		if pilha[i][1] == v_remove[0]:
			for j in range(len(pilha)):
				if pilha[j][0] == v_remove[0]:
					novas_a.append([pilha[i][0],pilha[j][1],"Directed",'','','','1.0\n'])
	return novas_a

def GeraVSimp(quad): #OK
	vsimp = []
	vsimp.append(disciplinas[0])
	for i in range( 1 , (len(disciplinas)) ):
		tmp = str(disciplinas[i][5].strip())
		if tmp.isdigit():
			if int(tmp) <= int(quad):
				vsimp.append(disciplinas[i])
	return vsimp

def OutDeg(disc,pilha):
	n=0
	for i in range(len(pilha)):
		if pilha[i][0]==disc:
			n+=1
	return n

def MelhorOpcao(restantes,pilha):
	#retorna a materia presente em restantes com maior out degree relativo
	m = 0
	max = [0,None,None]
	nova_dep = None
	for n in range(1,len(restantes)):
		if OutDeg(restantes[n][0],pilha)>m:
			m = OutDeg(restantes[n][0],pilha)
			max = [restantes[n][5],n,restantes[n]]
	if max[0]>0:
		restantes.pop(max[1])
		nova_dep = max[2]
	return [nova_dep,restantes]

###############################################
############### Inicio programa ###############	
###############################################

vertice_in="./"+nome_engenharia+"_V_restantes.csv" 		#Planilha constante
vertice2_in="./"+nome_engenharia+"_V_concluidas.csv" 	#Planilha constante
vertice3_in="./"+nome_engenharia+"_V.csv" 				#Planilha constante
aresta_in="./"+nome_engenharia+"_A.csv"  				#Planilha constante
vertice_out="./"+nome_engenharia+"_V_simp.csv"	 		#Planilha variavel
aresta_out="./"+nome_engenharia+"_A_simp.csv"  			#Planilha variavel
vertice_ideal_out="./"+nome_engenharia+"_V_ideal.csv"

print "\nIniciando o programa: Organiza\n"
print "Arquivos de entrada:"
print "\t"+vertice_in
print "\t"+vertice2_in
print "\t"+vertice3_in
print "\t"+aresta_in+"\n"
print "Arquivos de saida:"
print "\t"+vertice_out
print "\t"+aresta_out+"\n"

v_r_in = open(vertice_in,'r')
v_c_in = open(vertice2_in,'r')
v_in = open(vertice3_in,'r')
a_in = open(aresta_in,'r')
v_out = open(vertice_out,'w')
a_out = open(aresta_out,'w')
v_ideal_out = open(vertice_ideal_out,'w')

disciplinas = ProcessaVertices(v_in)
disc_r = ProcessaVertices(v_r_in) #Disciplinas restantes
disc_c = ProcessaVertices(v_c_in) #Disciplinas concluidas
depe = ProcessaVertices(a_in)

last_a_id = len(depe)

#Quad atual
quad = 6 # int(raw_input("Qual quadrimestre voce esta?  "))
disc_s = GeraVSimp(quad)
pilha = []
quad_ideal = QuadIdeal(disciplinas, quad) #Matérias recomendadas
quad_disc = quad_ideal
quad_size = ContaQuad(disciplinas, quad) #Quantidade de matérias recomendadas
for i in range(len(quad_disc)):
	if TemDependencia(quad_disc[i][0],depe):
		pilha = AddPilha(ProcuraDependencia(quad_disc[i][0],depe),pilha)

#Gera Pilha de dependencias(P/ quad ideal)
TemD = True
n=0
while(TemD):
	TemD = None
	for i in range(len(pilha)):
		if TemDependencia(pilha[i][0],depe):
			n+=1
			len_pilha_antes = len(pilha)
			pilha = AddPilha(ProcuraDependencia(pilha[i][0],depe),pilha)
			len_pilha_depois = len(pilha)
			if len_pilha_antes<len_pilha_depois:
				TemD = True
	if TemD != True:
		TemD = False



#Gera Pilha de dependencias(P/ quad ideal)
j=5
while(j>0):
	quad_disc = QuadIdeal(disciplinas, j)
	for i in range(len(quad_disc)):
		if TemDependencia(quad_disc[i][0],depe):
			pilha = AddPilha(ProcuraDependencia(quad_disc[i][0],depe),pilha)
	TemD = True
	n=0
	while(TemD):
		TemD = None
		for i in range(len(pilha)):
			if TemDependencia(pilha[i][0],depe):
				n+=1
				len_pilha_antes = len(pilha)
				pilha = AddPilha(ProcuraDependencia(pilha[i][0],depe),pilha)
				len_pilha_depois = len(pilha)
				if len_pilha_antes<len_pilha_depois:
					TemD = True
		if TemD != True:
			TemD = False
	j=j-1


for i in range(1,len(disc_c)):
	novas = GeraAresta(disc_c[i],pilha)
	for j in range(len(novas)):
		pilha.append(novas[j])

#Remove as concluidas dos vert. simpl.
for i in range(1, len(disc_c)):
	j = 1
	while(j<len(disc_s)):
		if (str(disc_c[i][0]) == str(disc_s[j][0])):
			disc_s.pop(j)
		else:
			j+=1


#Remove as concluidas da pilha
for i in range(1, len(disc_c)):
	j = 0
	while(j<len(pilha)):
		if (str(disc_c[i][0]) == str(pilha[j][0])) or (str(disc_c[i][0]) == str(pilha[j][1])):
			pilha.pop(j)
		else:
			j+=1

#Disc_s->_V_simp
for n in range(0,len(disc_s)):
	linha = ("%s;%s;%s;%s;%s;%s" %(str(disc_s[n][0]),str(disc_s[n][1]),str(disc_s[n][2]),str(disc_s[n][3]),str(disc_s[n][4]),str(disc_s[n][5])))
	v_out.write(linha)
print "\nPlanilha de vertices gerada"

#Pilha->_A_simp
a_out.write("Source;Target;Type;id;label;timeset;weight\n")
for n in range(0,len(pilha)):
	linha = ("%s;%s;%s;%s;%s;%s;%s" %(pilha[n][0],pilha[n][1],pilha[n][2],pilha[n][3],pilha[n][4],pilha[n][5],pilha[n][6]))
	a_out.write(linha)
print "\nPlanilha de arestas gerada\n"

disc_simpl_rest = GeraVSimp(quad)
for i in range(1, len(disc_c)):
	j = 1
	while(j<len(disc_simpl_rest)):
		if (str(disc_c[i][0]) == str(disc_simpl_rest[j][0])):
			disc_simpl_rest.pop(j)
		else:
			j+=1


for i in range(len(quad_ideal)):
	if TemDependencia(quad_ideal[i][0],pilha):
		quad_ideal[i]=MelhorOpcao(disc_simpl_rest,pilha)[0]
		disc_simpl_rest = MelhorOpcao(disc_simpl_rest,pilha)[1]

print "\nO quadrimestre ideal seria:"
for i in range(len(quad_ideal)):
	print "\t"+quad_ideal[i][0]+" - "+quad_ideal[i][1]

v_ideal_out.write("id;label;créditos;ch;categoria;quad. ideal\n")
for n in range(0,len(quad_ideal)):
	linha = ("%s;%s;%s;%s;%s;%s" %(str(quad_ideal[n][0]),str(quad_ideal[n][1]),str(quad_ideal[n][2]),str(quad_ideal[n][3]),str(quad_ideal[n][4]),str(quad_ideal[n][5])))
	v_ideal_out.write(linha)

v_r_in.close()
v_c_in.close()
v_in.close()
a_in.close()
v_out.close()
a_out.close()
v_ideal_out.close()