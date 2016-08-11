#-*- coding:utf-8 -*-
'''
O programa tem como entrada a planilha de vértices completa e como saida uma planilha de vértices processada.

A planilha deve vir ordenada pela coluna Quad. Ideal em ordem crescente.
'''
dir_in="./Matriz_Energia_V.csv" #Planilha constante
dir_out="./Matriz_Entegia_V_tmp.csv" #Planilha variavel

#abre arquivos
entrada = open(dir_in,'r') 
saida = open(dir_out,'w')

disciplinas = []
disc_concl = [] #Disciplinas concluidas(ainda não implementado)
for lista in entrada:
	disciplinas.append(lista.split(";"))
disc_rest = disciplinas #Disciplinas restantes

#testa quad
n=1
brk= True #Condição de parada do loop
while n<=len(disc_rest) and brk:
	ok = False #Condição teste do loop
	while not(ok):
		txt = ""
		for i in range(0,2):
			txt=txt+" "+disciplinas[n][i]
		resp = raw_input("\n\nVoce ja cursou a disciplina %s ?[S/N/FIM]\nDigite FIM se nao houver mais nenhuma disciplina que voce cursou.\n" %txt).lower()
		if (resp=="s" or resp=="sim"):
			ok=True
			disc_concl.append(disciplinas[n]) #ainda não utilizado
			disc_rest.pop(n) #Remove disciplinas ja cursadas
		elif (resp=="n" or resp=="nao"):
			ok=True
			n+=1
		elif(resp=="fim"):
			brk = False
			break
		else:
			print "Digite uma resposta válida"

#Grava no arquivo
for n in range(len(disc_rest)):
	linha = ("%s;%s;%s;%s;%s;%s" %(str(disc_rest[n][0]),str(disc_rest[n][1]),str(disc_rest[n][2]),str(disc_rest[n][3]),str(disc_rest[n][4]),str(disc_rest[n][5])))
	saida.write(linha)

#Fecha os arquivos
entrada.close()
saida.close()