# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:49:21 2020

@author: Emiliano
"""
import numpy as np
import sympy as sy
sy.init_printing()

a=int(input("ingrese la cantidad de filas:"))
b=int(input("ingrese la cantidad de columnas:"))

print("necesito que ingrese los elementos en el orden pertinente, es decir siguiendo sus indices , a11 a12 a13 ..")


vcm1=[]
vcm2=[]


for i in range (a*b): 
        variableit=input("elemento de matriz M: ")
        vcm1.append(variableit)

for j in range (a*b):
       variableit2=input("elemento de matriz V: ")
       vcm2.append(variableit2) 
       
NewM=sy.Matrix(a,b,vcm1)
NewV=sy.Matrix(a,b,vcm2)

w2=sy.symbols("w2")

m_v=w2*NewM-NewV

autovalor=sy.solve(m_v.det(),w2)

glist=list(sy.symarray("a",a))


vec=[0 for i in range (a)]
md0=sy.Matrix(vec)
M_x=[]

for i in range(len(autovalor)):
    z=autovalor[i]
    M_0=z*NewM-NewV
    sol=list(sy.linsolve((M_0,md0),glist))
    M_x.append(sol)
    print("autovalor :" , autovalor[i], ", autovector :" , sol)


#print (NewM) 

