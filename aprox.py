# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 12:59:08 2022

@author: josad
"""

#################################################
#variables str para la entrada y salida de datos#
#################################################

explicación_al_usu="Este programa realiza una aproximación a la función \
f(x)=(a0*x^0, a1*x^1,..., an*x^n) por el método Newton Raphson.\
 El coeficiente de la funcón f(x) podrá definirlo usted. Al definir este\
 coeficiente el programa arrojara 4 aproximaciones para la función f(x)\
 el caso de llegar a la aproximación sólo arrojara el resultado.\
 Después de los ´:´ podrá agregar un número para el coeficiente: "
aprox_final="Se llegó a la solución y la aproximación es {}"
aproximaciones="La aproximación {} es {}"

A_usu= int(input(explicación_al_usu))

#########################
#Definición de funcoines#
#########################

def polinomio(x):
    """La función <polinomio>, realiza dos listas de la forma A=[an*x^n] y
    B=[(an*n*x^(n-1)]con n ingresado por el usuario y x definido al utilizar 
    la función. Esta función retorna la divicón entre la suma de los elemtos de
    A sobre la suma de los elemetos de B.
    """
    A_usu_X= A_usu+1 #corrije el conteo del for de la computadora x=6, 0->5
    #realiza una lista para f(x)=(anX^n)
    A_X=[]
    for i in range(A_usu_X):
        A_X.append(i*x**i) 
        
    #realiza una lista para f`(x)=(an*n*X^(n-1)) es decir la derivada de f(x)
    B_X=[]
    for i in range(A_usu_X):
        B_X.append(i*i*x**(i-1))
        
    #Suma de los elementos de las listas
    suma_A_X=sum(A_X)
    suma_B_X=sum(B_X)

    return(suma_A_X/suma_B_X) 

    
def aprox(x_n):
    """
    La función <aprox> realiza la aprocimación a la función dada por el
    método de Newton Raphson. Está función toma la función <polinomio>
    para realicar la aproximación. Esta función retorna un flotante de 4 
    cifras decimales que es la aproximación segun x que se da a la función.
    """
    x_b=x_n - polinomio(x_n) #Se aplica el método de aproximación Newton Raphson
    return(x_b)
    
###############################################
#Aplicación de las funciones y salida de datos# 
###############################################

x_0=round(aprox(1),4)
x_1=round(aprox(x_0),4)
contador=0
j=[x_1]

while contador <4:
    """
    Este ciclo tiene la función de aplicar la aproximación 4 veces cambiando 
    el valor con el que se hace la aproximación por el anterior que haya pasado,
    es decir, aproximación con X_0 para X_1, luego aproximación con X_1 para 
    X_2, ... , x_4.
    """
    x_n=round(aprox(j[contador]),4)
    j.append(x_n)
    contador+=1
    if x_n == 0:
        print((aprox_final).format(x_n))
        break
if x_n != 0:
    """
    Imprime las 4 aproximaciones en el caso de que no se haya llegado a la 
    aproximación resultado.
    """
    for i in range(contador):
        k=j[i+1]
        print(aproximaciones.format(i+1,k))











