#!/usr/bin/python3
soma = 0
for x in range(4):
	nota = int(input("digite a nota {}: ".format(x+1)))
	soma += nota
print("A media e igual {}".format(soma/4)) 
