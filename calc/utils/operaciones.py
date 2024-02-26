"""
Funciones que calculan el area de un circulo, cuadrado asi tambien como el volumen de un cubo

Funciones:
=========

areaCirculo() : Calcula el area de un circulo, se envia como parametro la radio
areaCuadrado(): Calcula el area de un cuadrado, se envia como parametro los lados
volCubo(): Calcula el volumen de un cubo, se envia como parametro el lado.

Ejemplo:
========

>>> import operaciones.py
>>> resultado = operaciones.areaCirculo(valor)


"""

import math
"""
Importamos la libreria de python math para utiliza la funcion PI
"""
def areaCirculo(val):
    """
     Inputs:
        val: es el valor de la radio del circulo
     Ouputs:
        retorna la area del circulo redondeado a dos decimales
    """
    return round(math.pi * val**2,2)

def areaCuadrado(val):
    """
     Inputs:
        val: es el valor del lado del cuadrado
     Ouputs:
        retorna la area del cuadrado redondeado a dos decimales
    """
    return round(val**2,2)

def volCubo(val):
    """
     Inputs:
        val: es el valor del lado del cubo
     Ouputs:
        retorna el volumen del cubo redondeado a dos decimales
    """
    return round(val**3,2)
