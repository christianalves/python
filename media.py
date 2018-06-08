#!/usr/bin/python3
#nome = input('digite seu nome: ')
#print("Seja Bem Vindo".upper(), nome.title()) 
#number_1= int(input("digite um numero: "))
#number_2= int(input("digite um segundo numero: ")) 
#print(number_1 + number_2)
nome = input("digite o nome do aluno: ")
nota1 = int(input("digite a primeira nota: "))
nota2 = int(input("digite a segunda nota: "))
falta = int(input("digite a quantidade de falta: "))
media = (nota1 + nota2) / 2  
#print("A media do aluno {} foi {}".format(nome.title(),media))
if media >= 7 and falta < 4:
    resultado = "aprovado"
else:
    resultado = "reprovado" 
print("O aluno {} teve a media {} e {} faltas => foi {}".format(nome, media, falta, resultado))
