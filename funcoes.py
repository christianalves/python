#!/usr/bin/python3
#def soma(x, y):
#	return x + y
#
#soma(4, 4)
#soma(3, 2)
#result = soma('daniel', 'prata')
#print(result)

#def boas_vindas(nome):
#	nome = nome.replace('a', '@')
#
#	return 'Seja bem vindo {}'.format(nome.title())
#
#nomes = ['christian', 'caio', 'camila']
#
#for nome in nomes:
#	print(boas_vindas(nome))

def ler_arquivo(nome):
	with open(nome, 'r') as arquivo:
		conteudo = arquivo.read()
	return conteudo

def escrever_arquivo(nome):
	with open(nome, 'a') as arquivo:
		conteudo = input('Digite uma fruta: ')
		arquivo.write(conteudo + '\n')
	return True

def subscrever_arquivo(nome):
	with open(nome, 'w') as arquivo:
		conteudo = input('Digite uma fruta: ')
		arquivo.write(conteudo + '\n')
	return True

escrever_arquivo('frutas.txt')
print(ler_arquivo('frutas.txt'))
