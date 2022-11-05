# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:17:55 2022

@author: josad
"""

from random import randint
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
#########################
#Definición de funcoines#
#########################

def lista_tuplas(a,b):
    """
    La función <lista_tuplas> utiliza la función interna de python que es zip()
    acepta múltiples objetos iterables como listas y tuplas y devuelve un objeto 
    iterable por lo que el objeto zip almacena elementos como una lista de tuplas.
    Esta función retorna una lista de tuplas de la amnera l=[(a,b),(c,d)]
    """
    result = zip(a, b) #se implementa la función zip().
    lista=[] #se crea la lista vacia.
    for x in result:
        lista.append(x) #se agrega lo que realizo zip() a la lista vacia.
    return(lista)
    


def lista_aleatoria(a,b):
    """
    La función <lista_aleatoria> genera una lista de números aleatorios entre 
    a y b, siendo a el rango menor a y b el rango mayor. La lista de manera
    automatica genera 1000 datos en el rango asignado.
    """
    listado_numeros = [] #se crea la lista que guardará los datos.
    contador = 0 # un contador que empieza en 0 y llegará hasta 1000.
    while contador < 1000:
        numero_random = randint(a,b) #genera un numero rondón de a y b.
        listado_numeros.append(numero_random) #agrega el número a la lista.
        contador = contador + 1 # suma a cada vuelta
    return(listado_numeros)

def aleatorio_no_repetido (a,b,c):
    """
    La función <aleatorio_no_repetido> retorna una lista de números aletorios 
    los cuales no se repiten, esta función resibe 2 datos a y b, que son datos 
    int(), a el rango menor y b rango mayor de los números que se generan. El 
    tercer dato que recibe en otro int() el cual será las veces que se repirá 
    el ciclo, ese mismo número será la cantidad de elementos que tendra la lista.
    """
    lis_no_repetidos = [] 
    contador = 0 

    numero_random = randint(a,b) # genera un numero aletorio entre a y b.

    while contador < c: # El ciclo termina hasta que llegue a c, len() de lista
        numero_random = randint(a,b) 
        if numero_random in lis_no_repetidos: # verifica si el número ya existe.
                                                
            pass
        else:
            lis_no_repetidos.append(numero_random) # agrega el número a la lista
            contador = contador + 1 
    return(lis_no_repetidos)



#################################################
#variables str para la entrada y salida de datos#
#################################################
escoger_funcion="escoger entre 1 y 3: "
funciones_trigonometricas="1=sin(),2=cos(),3=tan()"
funciones_hiperbolicas="1=sinh(x),2=cosh(x),3=tanh(x)"
escoger_tri_hiper="Escoge funciones trigonómetricas=1 o hiperbólicas=2: "
a="Escoge un valor para empezar las x debe ser un número: "
b="Escoge un valor para terminar las x, debe ser mayor que el número \
anterior: "
c="Escoge un valor para empezar las y debe ser un número: "
d="Escoge un valor para terminar las y, debe ser mayor que el número \
anterior: "

#INGRESO DEL USUARIO LOS VALORES SIGUIENTES
explicacio="Hola este es un programa que graficará una función que tú escojas\
 en el rango de x y y que tu decidas, comencemos."

print(explicacio)
usu_a=int(input(a))
usu_b=int(input(b))
usu_c=int(input(c))
usu_d=int(input(d))
lista_x=lista_aleatoria(usu_a, usu_b)
lista_y=lista_aleatoria(usu_c, usu_d)


###################################################################
#generación de lista con los datos por arriba y por debajo de f(x)# 
###################################################################

lista_xy=lista_tuplas(lista_x, lista_y) #se crea la lista de 1000 tuplas

lista_xy_eval=[]
for i in lista_xy:
    for i in i:
        lista_xy_eval.append(i)
        """  cambiar """
       # lista_evaluada.append(fraccio(i))


usu=int(input(escoger_tri_hiper))

##################################################################
#Función auxiliar para verificar la función que el usuario escoje#
##################################################################
if usu==1:
    print(funciones_trigonometricas)
    j= int(input(escoger_funcion ))
else:
    print(funciones_hiperbolicas,)
    j= int(input(escoger_funcion ))
def funcion_usu(a):  
    lista_eval=[]
    if usu ==1:
        if j ==1:
            lista_seno=[]
            for i in a:
                
                k=np.sin(i)
            
                lista_seno.append(k)
            lista_eval=lista_eval+lista_seno
            
        if j==2:
            lista_coseno=[]
            for i in a:
        
                k=np.cos(i)
            
                lista_coseno.append(k)
            lista_eval=lista_eval+lista_coseno
            
        if j==3:
            lista_tangente=[]
            for i in a:
        
                k=np.tan(i)
            
                lista_tangente.append(k)
            lista_eval=lista_eval+lista_tangente
            
   
    if usu == 2:
        if j ==1:
            lista_senoh=[]
            for i in a:
       
                k=np.sinh(i)
                
                lista_senoh.append(k)
            lista_eval=lista_eval+lista_senoh
            
        if j==2:
            lista_cosenoh=[]
            for i in a:
                
                k=np.cosh(i)
           
                lista_cosenoh.append(k)
            lista_eval=lista_eval+lista_cosenoh
            
        if j==3:
            lista_tangenteh=[]
            for i in a:
                
                k=np.tanh(i)
                
                lista_tangenteh.append(k)
            lista_eval=lista_eval+lista_tangenteh
            
    return(lista_eval)
           
           
           
lista_evaluada=funcion_usu(lista_xy_eval)           
           

########################################################################
#Tratamiento sobre las listas, se obtine al final la lista de 100 datos#
########################################################################


lista_positivo=[] #se genera lista que tendrá los valores por arriba de f(x) positivos
lista_negativo=[] #se genera lista que tendrá los valores por arriba de f(x) positivos
for i in lista_evaluada:
    if i>0:    
        lista_positivo.append(i)
    else:
        lista_negativo.append(i)

#se genera el porcentaje de valores positivos y negativos que habia al evaluar f(x)

porcentaje_x=(len(lista_positivo)/2000)*100
porcentaje_y=(len(lista_negativo)/2000)*100


porcentaje_x_entero=int(porcentaje_x)
porcentaje_y_entero=int(porcentaje_y)

# se generan 2 listas de números aletorios segun los parametros de las listas

lis_posit_alea=aleatorio_no_repetido(1, len(lista_positivo), porcentaje_x_entero)
lis_nega_alea=aleatorio_no_repetido(1, len(lista_negativo), porcentaje_y_entero)

lista_posit_porcentaje=[]
r=[]
for i in range(porcentaje_x_entero):
    r.append(lis_posit_alea[i])
    lista_posit_porcentaje.append(lista_positivo[r[i]])
        
lista_nega_porcentaje=[]
d=[]
for i in range(porcentaje_y_entero):
    d.append(lis_nega_alea[i])
    lista_nega_porcentaje.append(lista_negativo[d[i]])
        
lista_graficar=lista_posit_porcentaje+lista_nega_porcentaje

###############################################################
#verificación de la función escogida y graficación de la misma#
###############################################################


if usu ==1:
    if j ==1:
        style.use("classic")
        x=np.linspace(lista_graficar,0.0001)
        t=np.sin(x)
        plt.plot(x,t)
        plt.title("Función seno")
        plt.xlabel("valores de X")
        plt.ylabel("Valores de y")
        plt.grid(True)
        plt.show()
    if j==2:
        style.use("classic")
        x=np.linspace(lista_graficar,0.0001)
        t=np.cos(x)
        plt.plot(x,t)
        plt.title("Función coseno")
        plt.xlabel("valores de X")
        plt.ylabel("Valores de y")
        plt.grid(True)
        plt.show()
    if j==3:
        style.use("classic")
        x=np.linspace(lista_graficar,0.0001)
        t=np.tan(x)
        plt.plot(x,t)
        plt.title("Función tangente")
        plt.xlabel("valores de X")
        plt.ylabel("Valores de y")
        plt.grid(True)
        plt.show()
   
if usu == 2:
    if j ==1:
        style.use("classic")
        x=np.linspace(lista_graficar,0.0001)
        t=np.sinh(x)
        plt.plot(x,t)
        plt.title("Función seno hiperbólico")
        plt.xlabel("valores de X")
        plt.ylabel("Valores de y")
        plt.grid(True)
        plt.show()
    if j==2:
        style.use("classic")
        x=np.linspace(lista_graficar,0)
        t=np.cosh(x)
        plt.plot(x,t)
        plt.title("Función coseno hiperbólico")
        plt.xlabel("valores de X")
        plt.ylabel("Valores de y")
        plt.grid(True)
        plt.show()
    if j==3:
        style.use("classic")
        x=np.linspace(lista_graficar,0.0001)
        t=np.tanh(x)
        plt.plot(x,t)
        plt.title("Función tangente hiperbólica")
        plt.xlabel("valores de X")
        plt.ylabel("Valores de y")
        plt.grid(True)
        plt.show()
    
                                    #######
                                    #final#
                                    #######




