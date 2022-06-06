#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 22:54:03 2020

@author: hugo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 09:59:44 2020

@author: hugo
"""

tipo = input()
caractere = input()
dimensao = int(input())

def triangulo(caractere,d):
    altura = 
    for i in range(1,d):
        print()

    
def quadrado(caractere, d):

    
def losango(caractere, d):

        
def hexagono(caractere, d):

def octogono (caractere, d):
 
if tipo != "Q" and  tipo != "T" and  tipo != "L" and  tipo != "H" and tipo != "O":
    print("Identificador invalido.")
else:
    if dimensao < 3:
        print("Dimensao invalida.")

if tipo == "T":
    triangulo(caractere, dimensao)
    
if tipo == "Q":
    quadrado(caractere, dimensao)
    
if tipo == "L":
    losango(caractere, dimensao)
    
if tipo == "H":
    hexagono(caractere, dimensao)
    
if tipo == "O":
    octogono(caractere, dimensao)