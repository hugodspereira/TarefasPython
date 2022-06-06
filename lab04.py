#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:41:47 2020

@author: hugo
"""

a = float(input())
b = float(input())
c = float(input())

def ordem_lados(lados):
    ordem = lados
    for i in range(len(lados)):
        for j in range(i + 1, len(lados)):
            
            if ordem[i] < ordem[j]:
                ordem[i], ordem[j] = ordem[j],ordem[i]
           
        
    return(ordem)

lados = ordem_lados([a, b, c])

if lados[0] >= lados[1] + lados[2]:
    print("Valores invalidos na entrada")
else:
    if a == b == c:
        print("Triangulo equilatero")
    
    else:
        if a == b != c or a == c != b or a != b == c:
            print("Triangulo isosceles")
        
        else:
            print("Triangulo escaleno")
            

    soma_quadrados = lados[1]**2 + lados[2]**2

    if lados[0]**2 < soma_quadrados:
        print("Triangulo acutangulo")
        
    else:
        if lados[0]**2 == soma_quadrados:
            print("Triangulo retangulo")
            
        else:
            print("Triangulo obtusangulo")
    
    
    

    
    
    
    