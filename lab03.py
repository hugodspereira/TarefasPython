#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:38:39 2020

@author: hugo
"""

Tosse = input()
Febre = input()
respirar = input()
sint1 = Tosse == "True"
sint2 = Febre == "True"
sint3 = respirar == "True"


print("Tosse:", sint1)
print("Febre:", sint2)
print("Dificuldade para respirar:", sint3)
print("Provavelmente eh COVID-19:", sint1 and sint2 and sint3)

