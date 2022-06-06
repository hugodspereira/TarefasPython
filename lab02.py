#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:42:48 2020

@author: hugo
"""

valor = float(input())
dias_atraso = int(input())

multa = valor * 0.02
juros = valor * 0.00033 * dias_atraso
valor_total = valor + multa + juros
minimo = 0.1 * valor_total

print("Valor: R$", format(valor, '.2f'))
print("Multa: R$", format(multa, '.2f'))
print("Juros: R$", format(juros, '.2f'))
print("Valor total: R$", format(valor_total, '.2f'))
print("Valor minimo para renegociacao: R$", format(minimo, '.2f'))