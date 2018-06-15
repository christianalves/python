#!/usr/bin/python3
print("Sistema de Nota")
aluno = input("qual o nome do aluno:")
nota1 = int(input("digite a nota do primeiro bimestre:"))
nota2 = int(input("digite a nota do segundo bimestre:"))
nota3 = int(input("digite a nota do terceiro bimestre:"))
nota4 = int(input("digite a nota do quarto bimestre:"))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 7:
	result = "aprovado"
else:
	result = "reprovado" 
print("O aluno {} ficou com a media {} e foi {}".format(aluno, media, result))
