#!/usr/bin/python3
def alteracao(nome, origin, destino):
	with open(nome, "r") as arquivo:
		conteudo = arquivo.readlines()
		novo_conteudo = [] #cria uma lista vazia primeiro
		for x in conteudo:
			novo_conteudo.append(x.replace(origin, destino))
	return novo_conteudo

conteudo =  alteracao("requerimentos2.txt", "e", "&")
with open("requerimentos4.txt", "a") as arquivo: #cria e add coisas novas
	for x in conteudo:
		arquivo.write(x)
