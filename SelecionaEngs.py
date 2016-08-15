#-*- coding:utf-8 -*-
'''
Função: selecionar as disciplinas já cursadas para gerar um grafo mais simples no gephi

Requer: duas planilhas(vertices e arestas) 

saida_r: um arquivo de texto formatado nos padrões de entrada dos algoritmos
'''
nome_engenharia = "" #insira o nome da engenharia aqui


dir_in="./"+nome_engenharia+"_V.csv" #Planilha constante
dir_out_r="./"+nome_engenharia+"_V_restantes.csv" #Planilha variavel
dir_out_c="./"+nome_engenharia+"_V_concluidas.csv" #Planilha variavel

#abre arquivos
entrada = open(dir_in,'r') 
saida_r = open(dir_out_r,'w')
saida_c = open(dir_out_c,'w')

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
	saida_r.write(linha)

#Grava no arquivo
saida_c.write("id;label;créditos;ch;categoria;quad. ideal\n")
for n in range(len(disc_concl)):
	linha = ("%s;%s;%s;%s;%s;%s" %(str(disc_concl[n][0]),str(disc_concl[n][1]),str(disc_concl[n][2]),str(disc_concl[n][3]),str(disc_concl[n][4]),str(disc_concl[n][5])))
	saida_c.write(linha)


#Fecha os arquivos
entrada.close()
saida_r.close()
saida_c.close()