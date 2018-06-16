#!/usr/bin/python3
pessoas = [
	{ "nome": "christian", "idade": 42}, 
	{"nome": "caio", "idade": 7},
	{"nome": "camila", "idade": 24},
	{"nome": "roque", "idade": 3}
]
print(len(pessoas))
#print(pessoas[3])
for pessoa in pessoas:
	print(pessoa["nome"], pessoa["idade"])
