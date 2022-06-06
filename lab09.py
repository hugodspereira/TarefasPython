#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 23:32:30 2020

@author: hugo
"""

def tupla_float_int(x) :
    x = x[1:-1]       # remove parenteses
    x = x.split(",")  # separa em duas strings
    f = float(x[0])   # converte primeiro elemento para float
    i = int(x[1])     # converte segundo elemento para int
    return (f,i)      # retorna tupla

def media_tarefas(lista):
    media = 0
    soma = 0
    for i in range(len(lista)):
        media = media + lista[i][0]*lista[i][1]
        soma = soma + lista[i][1]
    media = float(media/float(soma))
    return(media)


notas_lab = [tupla_float_int(x) for x in input().split()]
prova1, prova2 = [float(x) for x in input().split()]

mediatarefas = media_tarefas(notas_lab)
mediaprovas = (prova1*3.0 + prova2*4.0)/7.0
 

print("Media das tarefas de laboratorio: {:.1f}".format(mediatarefas))
print("Media das provas: {:.1f}".format(mediaprovas))

if mediatarefas >=5.0 and mediaprovas >= 5.0:
    mediafinal = 0.7*mediaprovas + 0.3*mediatarefas
    print("Aprovado(a) por nota e frequencia")
else:
    if mediatarefas >= 2.5 and mediaprovas >= 2.5:
        mediapreliminar = min(4.9, 0.7 * mediaprovas + 0.3 * mediatarefas)
        exame = float(input())
        print("Media preliminar: {:.1f}".format(mediapreliminar))
        print("Nota no exame: {:.1f}".format(exame))
        mediafinal = (mediapreliminar + exame)/2.0
        if mediafinal >= 5.0:
            print("Aprovado(a) por nota e frequencia")
        else:
            print("Reprovado(a) por nota")
    else:
        mediafinal = min(mediaprovas, mediatarefas)
        print("Reprovado(a) por nota")



print("Media final: {:.1f}".format(mediafinal))