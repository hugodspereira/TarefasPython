#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:11:07 2020

@author: hugo
"""


def busca_amigo(seq, nome):
    for i in range(len(seq)):
        if seq[i] == nome:
            return nome

pessoas = {}
nomes = []
nome = input()

while nome.isalpha():
    nomes = nomes + [nome]
    nome = input()

nomes.sort()

for i in range(len(nomes)):
    pessoas[nomes[i]] = []


amizade = input()
while amizade != "--":
    amizade = amizade.split()
    pessoas[amizade[0]] = pessoas[amizade[0]] + [amizade[1]]
    pessoas[amizade[1]] = pessoas[amizade[1]] + [amizade[0]]
    amizade = input()

for i in range(len(nomes)):
    pessoas[nomes[i]].sort()



inomes = 0
while inomes < len(nomes):
    for j in range(inomes+1,len(nomes)):
        amizade = [nomes[inomes],nomes[j]]
        lista = []
        for k in range(len(pessoas[nomes[inomes]])):
            amigo = pessoas[nomes[inomes]][k]
            emcomum = busca_amigo(pessoas[nomes[j]], amigo)
            if amigo == emcomum:
                lista = lista + [emcomum]
        if len(lista) == 0:
            print(nomes[inomes], nomes[j],':')
        else:
            print(nomes[inomes], nomes[j],':', ', '.join(lista))        
    inomes = inomes+1
            
            
        
        
        
