#!/usr/bin/python3
#nome = input('digite seu nome: ')
#print("Seja Bem Vindo".upper(), nome.title()) 
#number_1= int(input("digite um numero: "))
#number_2= int(input("digite um segundo numero: ")) 
#print(number_1 + number_2)
#nome = input("digite o nome do aluno: ")
#nota1 = int(input("digite a primeira nota: "))
#nota2 = int(input("digite a segunda nota: "))
#falta = int(input("digite a quantidade de falta: "))
#media = (nota1 + nota2) / 2  
#print("A media do aluno {} foi {}".format(nome.title(),media))
#if media >= 7 and falta < 4:
#    resultado = "aprovado"
#else:
#    resultado = "reprovado" 
#print("O aluno {} teve a media {} e {} faltas => foi {}".format(nome, media, falta, resultado))


#numeros = list(range(0,100))
#for i in numeros:
#	if i % 2 != 0:
#		print(i)	


#qtd = int(input("digite um inteiro: "))
#or z in range(qtd):
#if z % 2 != 0:
#	print(z)
#pessoas = [
#	{"nome":"christian", "idade": 42},
#	{"nome":"camila", "idade": 35},
#	{"nome":"caio", "idade": 7},
#	{"nome":"roque", "idade": 4},
#
#]
##print(pessoas)
#for pessoa in pessoas:
#	nome = (pessoa['nome'])
#	idade = (pessoa['idade'])
###	print("O(A) {} tem {} anos".format(nome,idade))


#contador = 0
#while contador < 10:
#	print('ola')
#	contador = contador + 1
#while True:
#	variavel = input("digite 0 para sair")
#	if variavel == '0':	
#		continue
#	elif	variavel == 'sair':
#		break
#	print("teste continue")


#qtd = int(input("digite um inteiro:"))
#
#for z in range(qtd): 
#	if z == 100:
#		break
#else: 
#	print("nao encontrei")


#arquivo = open('frutas.txt','r')
#for x in arquivo.readlines():
#	print(x.replace('\n', ''))
#print(arquivo.readline())
#print(arquivo.readline())
#with open('frutas.txt', 'a+') as arquivo:
#for x in arquivo.readlines():
#	print(x)

#with open('frutas.txt', 'a+') as arquivo:
#	fruta = input("digite a fruta: ")
#	arquivo.write(fruta + '\n')	

#with open('nomeloop.txt', 'a') as arquivo:
#	while True:
#		nome = input("digite um nome:")
#		if nome == 'sair':
#			break
#		arquivo.write(nome + '\n')


#
#nomes = [ 'joao', 'camila', 'christian', 'roque' ]
#nomes[0] = 'carolina'
#addappend = input("digite o nome de uma nova pessoa append:")
#nomes.append(addappend)
#addinsert = input("digite o nome de uma nova pessoa para adicionar:")
#nomes.insert(0, addinsert)
#for nomes_var in nomes:
#	print("Bem vindo {}".format(nomes_var.title()))
#while len(nomes) > 0:
#	print(nomes)
#	nomes.pop()
#print(nomes)
#with open('lista_nomes.txt', 'r') as file:
#	print(file.readlines())
#from sub
