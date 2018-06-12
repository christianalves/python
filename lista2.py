#!/usr/bin/python3
letras = [ 'a', 'b', 'c', 'd', 'e', 'a', 'b' ]
print(len(letras))
#print(sorted(set(letras)))
letras = sorted(set(letras))
print(letras)
letras.pop()
print(letras)
