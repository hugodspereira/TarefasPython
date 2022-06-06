#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:32:31 2020

@author: hugo

Duvidas ate agora:Uma ideia que é, passar a string de entrada para uma matriz
e depois fazer essa dinamica. A ideia da dinamica seria fazer as contagens atraves das posicoes na matriz,
porem nao sei como transformar o string de entrada em uma matriz
se nao for para fazer desse jeito nao sei qual seria a forma de fazer.

for x in lista:
print(''.join(map(str, x))) a funcao join percorre a lista e imprimi, entao tenho que colocar dentro do for para imprimir
linha por linha.

dei print no codigo dele da monitoria


"""
import copy

espaco = []
a = input()

while (not a.isdigit()):
    espaco.append(list(a))
    a = input()
    
  

def sobrevive(espaco):
    # Colocar aqui a funcao cria matriz da aula
    espaco2 = copy.deepcopy(espaco)    
    
    for idy in range(1, len(espaco)-1):
        for idx in range(1, len(espaco[idy])-1):
            py = [idy-1,idy, idy+1]
            px = [idx - 1, idx, idx+1]
            n = 0
            for y in py:
                for x in px:
                    if y != idy or x != idx:
                        if espaco[y][x] == '@':
                            n = n + 1
            if n > 3 or n < 2:
                espaco2[idy][idx] = ' '
            else:
                if n == 3:
                    espaco2[idy][idx] = '@'
                        
    return(espaco2)

for j in range(len(espaco)):
    print(*espaco[j], sep = "")
  
i = 0
a=int(a)
while i < a:
    espaco = sobrevive(espaco)
    for j in range(len(espaco)):
        print(*espaco[j], sep = "")
    i=i+1
    
    
    
            