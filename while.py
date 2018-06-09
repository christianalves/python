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
qtd = int(input("digite um inteiro:"))

for z in range(qtd): 
	if z == 100:
		break
else: 
	print("nao encontrei")
