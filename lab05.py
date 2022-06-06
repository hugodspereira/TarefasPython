#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 23:01:49 2020

@author: hugo
"""

massa = float(input())
idade = int(input())
documento = input()
febre = input()
viagem =  input()
covid = input()
primeira = input()
doacoes = int(input())
ultima = int(input())
sexo = input()

if sexo == "F":
    gravida = input()



print("Massa corporal:", massa)
print("Idade:", idade)
print("Documento de autorizacao:",documento)
print("Febre ou sintomas gripais:",febre)
print("Viagem recente ao exterior:", viagem)
print("Contato com caso de COVID-19:", covid)
print("Primeira doacao:",primeira)
print("Doacoes nos ultimos 12 meses:", doacoes)
print("Meses desde ultima doacao:", ultima)
print("Sexo biologico:", sexo)

if sexo == "F":
    print("Gravida ou amamentando:")

if massa >= 50:
    if febre == "N":
        if viagem == "N":
            if covid == "N":
                if sexo == "M":
                    if doacoes < 4:
                        if ultima > 2:
                            if idade > 18:
                                if idade < 60:
                                    print("Agende um horario para triagem completa")
                                else:
                                    if primeira == "N":
                                        print("Agende um horario para triagem completa")
                            else:
                                if idade > 16:
                                    if documento > "S":
                                        print("Agende um horario para triagem completa")
                        
                    
                else:
                    if doacoes < 3:
                        if ultima > 3:
                            print("Agende um horario para triagem completa")
                            
                            
                            
if massa < 50:
    print("Impedimento: abaixo da massa corporal minima")
    
if idade < 16:
    print("Impedimento: menor de 16 anos")
else:
    if idade < 18:
        if documento == "N":
            print("Impedimento: menor de 18 anos sem consentimento dos responsaveis")
            
if idade > 69:
    print("Impedimento: maior de 69 anos")
else:
    if idade > 60:
        if primeira == "S":
            print("Impedimento: maior de 60 anos e primeira doacao")

if febre == "S":
    print("Impedimento: febre ou sintomas gripais")
    
if viagem == "S":
    print("Impedimento: viagem recente ao exterior")

if covid == "S":
    print("Impedimento: contato com caso de COVID-19")

if sexo == "M":                  
                    

        
        
    
